import numpy as np
import tensorflow as tf
import devfx.core as core
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.data_vizualization.seaborn as dv

cg.enable_imperative_execution_mode()

"""------------------------------------------------------------------------------------------------
"""
class UnivariateLinearRegressionDataGenerator():
    def __init__(self):
        pass

    def generate(self):
        M = 1024
        a = 1.0
        b = 0.75
        x = np.random.normal(0.0, 0.5, size=M)
        y = a*x + b + np.random.normal(0.0, 0.1, size=M)
        return [x, y]

"""------------------------------------------------------------------------------------------------
"""
class UnivariateLinearRegressionModel(cg.models.ImperativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        def h(x):
            w0 = cg.create_or_get_variable(name='w0', dtype=cg.float32, shape=(), initializer=cg.zeros_initializer())
            w1 = cg.create_or_get_variable(name='w1', dtype=cg.float32, shape=(), initializer=cg.zeros_initializer())
            r = w0 + w1*x
            return r

        def J(x, y):
            hr = h(x)
            r = cg.reduce_mean(cg.square(hr - y))
            return r

        self.register_hypothesis_function(fn=h)
        self.register_cost_function(fn=J)
        self.register_apply_cost_optimizer_function(optimizer=cg.train.AdamOptimizer(learning_rate=1e-2))

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].training_data_cost = self.run_cost_function(*context.training_data)
        if(len(training_log) >= 2):
            training_log[-1].trend_of_training_data_cost = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].trend_of_training_data_cost) <= 1e-2))
            
        training_log[-1].test_data_cost = self.run_cost_function(*context.test_data)

        print(training_log[-1])

        figure = core.persistentvariable('figure', lambda: dv.Figure(size=(8, 6)))
        chart = core.persistentvariable('chart', lambda: dv.Chart2d(figure=figure))
        figure.clear_charts()
        chart.plot(training_log[:].training_data_cost, color='green')
        chart.plot(training_log[:].test_data_cost, color='red')
        figure.show(block=False)

    def _on_training_iteration_end(self, iteration, context):
        pass

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass

"""------------------------------------------------------------------------------------------------
"""
def main():
    # generating data
    generated_data = UnivariateLinearRegressionDataGenerator().generate()
    
    # shuffle
    generated_data = stats.mseries.shuffle(generated_data)

    # chart
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(generated_data[0], generated_data[1])
    figure.show()

    # splitting data
    (training_data, test_data) = stats.mseries.split(generated_data, 0.75)
    # print(training_data, test_data)

    # learning from data
    model = UnivariateLinearRegressionModel()
    model.train(training_data=training_data, batch_size=64,
                test_data=test_data)

    # validation
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(test_data[0], test_data[1], color='blue')
    chart.scatter(test_data[0], model.run_hypothesis_function(test_data[0]), color='red')
    figure.show()

    model.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()