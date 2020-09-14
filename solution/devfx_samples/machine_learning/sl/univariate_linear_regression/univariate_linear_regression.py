import tensorflow as tf
import numpy as np
import devfx.core as core
import devfx.os as os
import devfx.statistics as stats
import devfx.machine_learning as ml
import devfx.data_vizualization as dv

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
class UnivariateLinearRegressionModel(ml.sl.Model):
    # ----------------------------------------------------------------
    @ml.build_graph(x=(ml.float32, (None,)))
    @ml.output_as_tensor((ml.float32, (None,)))
    @ml.input_as_tensor(x=(ml.float32, (None,)))
    def h(self, x):
        w0 = ml.sl.create_or_get_variable(name='w0', shape=(), dtype=ml.float32, initializer=ml.random_truncated_normal_initializer())
        w1 = ml.sl.create_or_get_variable(name='w1', shape=(), dtype=ml.float32, initializer=ml.random_truncated_normal_initializer())
        r = w0 + w1*x
        return r
    
    @ml.build_graph(x=(ml.float32, (None,)), y=(ml.float32, (None,)))
    @ml.output_as_tensor((ml.float32, (None,)))
    @ml.input_as_tensor(x=(ml.float32, (None,)), y=(ml.float32, (None,)))
    def J(self, x, y):
        hr = self.h(x)
        r = ml.reduce_mean(ml.square(hr - y))
        return r

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.register_apply_cost_optimizer_function(cost_fn=self.J, cost_optimizer=ml.AdamOptimizer(learning_rate=1e-2))
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].training_data_cost = self.J(*context.training_data_sample)
        if(len(training_log) >= 2):
            training_log[-1].training_data_cost_trend = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].training_data_cost_trend) <= 1e-2))
            
        training_log[-1].test_data_cost = self.J(*context.test_data_sample)

        print(training_log[-1])

        figure = core.ObjectStorage.intercept(self, 'figure', lambda: dv.Figure(size=(8, 6)))
        chart = core.ObjectStorage.intercept(self, 'chart', lambda: dv.Chart2d(figure=figure))
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
                test_data=test_data,
                training_data_sample=stats.mseries.sample(training_data, 64),
                test_data_sample=stats.mseries.sample(test_data, 64))

    # visual validation
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(test_data[0], test_data[1], color='blue')
    chart.scatter(test_data[0], model.h(test_data[0]), color='red')
    figure.show()

    # export_to
    model.export_to(path=f'{os.file_info.parent_directorypath(__file__)}/exports')

    # import_from
    model_executer = ml.sl.ModelExecuter.import_from(path=f'{os.file_info.parent_directorypath(__file__)}/exports')

    # visual validation
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(test_data[0], test_data[1], color='blue')
    chart.scatter(test_data[0], model_executer.h(ml.as_tensor(test_data[0], dtype=ml.float32, shape=(None,))), color='yellow')
    figure.show()




"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()