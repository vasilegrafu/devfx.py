import tensorflow as tf
import numpy as np
import devfx.core as core
import devfx.os as os
import devfx.statistics as stats
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv


"""------------------------------------------------------------------------------------------------
"""
class FunctionAproximationDataGenerator():
    def __init__(self):
        pass

    def generate(self):
        M = 1024*8

        x = stats.distributions.uniform(a=-4*3.14, b=+4.0*3.14).rvs(M)
        y = np.cos(x)*x + np.random.normal(0.0, 1.0, size=M)

        x = [[_] for _ in x]
        y = [[_] for _ in y]

        return [x, y]
"""------------------------------------------------------------------------------------------------
"""
class FunctionAproximationModel(ml.Model):
    # ----------------------------------------------------------------
    @ml.build_graph(x=(ml.float32, (None, 1)))
    @ml.output_as_tensor((ml.float32, (None, 1)))
    @ml.input_as_tensor(x=(ml.float32, (None, 1)))
    def h(self, x):
        fc1 = ml.nn.fully_connected(name="fc1",
                                    input=x,
                                    n=64,
                                    dtype=ml.float32,
                                    initializer=ml.random_glorot_normal_initializer(),
                                    activation_fn=lambda z: ml.nn.relu(z, s0=2.0, a=0.25))

        fc2 = ml.nn.fully_connected(name="fc2",
                                    input=fc1,
                                    n=64,
                                    dtype=ml.float32,
                                    initializer=ml.random_glorot_normal_initializer(),
                                    activation_fn=lambda z: ml.nn.relu(z, s0=2.0, a=0.25))


        fco = ml.nn.fully_connected(name="fco",
                                    input=fc2,
                                    n=1,
                                    dtype=ml.float32,
                                    initializer=ml.random_glorot_normal_initializer())

        r = fco
        return r
    
    @ml.build_graph(x=(ml.float32, (None, 1)), y=(ml.float32, (None, 1)))
    @ml.output_as_tensor((ml.float32, (None,)))
    @ml.input_as_tensor(x=(ml.float32, (None, 1)), y=(ml.float32, (None, 1)))
    def J(self, x, y):
        hr = self.h(x)
        r = ml.reduce_mean(ml.square(hr - y))
        return r

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.register_apply_cost_optimizer_function(cost_fn=self.J, cost_optimizer=ml.AdamOptimizer(learning_rate=1e-3))
        context.append_to_training_log_condition = lambda context: context.iteration % 100 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].training_data_cost = self.J(*context.training_data)
        if(len(training_log) >= 2):
            training_log[-1].training_data_cost_trend = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].training_data_cost_trend) <= 1e-2))
            
        training_log[-1].test_data_cost = self.J(*context.test_data)

        print(training_log[-1])

        figure = core.persistent_variable('figure', lambda: dv.Figure(size=(12, 4)))
        chart1 = core.persistent_variable('chart1', lambda: dv.Chart2d(figure=figure, position=121))
        chart2 = core.persistent_variable('chart2', lambda: dv.Chart2d(figure=figure, position=122))
        figure.clear_charts()
        chart1.plot(training_log[:].training_data_cost, color='green')
        chart2.scatter([_[0] for _ in context.test_data[0]], [_[0] for _ in context.test_data[1]], color='blue')
        chart2.plot([_[0] for _ in context.test_data[0]], [_[0] for _ in self.h(context.test_data[0])], color='red')
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
    generated_data = FunctionAproximationDataGenerator().generate()
    
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
    model = FunctionAproximationModel()
    model.train(training_data=training_data, batch_size=64,
                test_data=test_data)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()