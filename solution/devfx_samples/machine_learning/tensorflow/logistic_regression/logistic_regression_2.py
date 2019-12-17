import numpy as np
import devfx.core as core
import devfx.math as math
import devfx.statistics as stats
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class LogisticRegression2DataGenerator(object):
    def __init__(self):
        pass

    def generate(self):
        M = 1024*2
        w0 = 3.0
        w1 = 0.75
        a = -16
        b = +16

        x = stats.distributions.uniform(a=a, b=b).rvs(M)
        p = math.logistic(w0 + w1*x)
        y = np.random.binomial(1, p, M)

        return [x, y, p]

"""------------------------------------------------------------------------------------------------
"""
class LogisticRegression2Model(ml.Model):
    # ----------------------------------------------------------------
    # @ml.build_graph(x=(ml.float32, (None,)))
    @ml.output_as_tensor((ml.float32, (None, 2)))
    @ml.input_as_tensor(x=(ml.float32, (None,)))
    def h(self, x):
        w0 = ml.get_or_create_variable(name='w0', shape=(), dtype=ml.float32, initializer=ml.random_truncated_normal_initializer())
        w1 = ml.get_or_create_variable(name='w1', shape=(), dtype=ml.float32, initializer=ml.random_truncated_normal_initializer())
        r = ml.stack([
            ml.exp(w0 + w1*x)/(1.0 + ml.exp(w0 + w1*x)),
                          1.0/(1.0 + ml.exp(w0 + w1*x))
        ], axis=1)
        return r

    # @ml.build_graph(x=(ml.float32, (None,)), y=(ml.int32, (None,)))
    @ml.output_as_tensor((ml.float32, ()))
    @ml.input_as_tensor(x=(ml.float32, (None,)), y=(ml.int32, (None,)))
    def J(self, x, y):
        hr = self.h(x)
        r = -ml.reduce_mean(ml.reduce_sum(ml.one_hot(indices=y, depth=2, on_value=1.0, off_value=0.0, axis=1)*ml.log(hr), axis=1))
        return r

    @ml.output_as_tensor((ml.int32, (None,)))
    @ml.input_as_tensor(x=(ml.float32, (None,)))
    def y_pred(self, x):
        hr = self.h(x)
        r = ml.argmax(hr, axis=1)
        return r

    @ml.output_as_tensor((ml.float32, ()))
    @ml.input_as_tensor(x=(ml.float32, (None,)), y=(ml.int32, (None,)))
    def accuracy(self, x, y):
        y_predr = self.y_pred(x)
        r = ml.reduce_mean(ml.kronecker(y_predr, y, dtype=ml.float32))
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
            training_log[-1].training_data_cost_trend = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=64)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].training_data_cost_trend) <= 1e-3))
        training_log[-1].test_data_cost = self.J(*context.test_data_sample)
        
        training_log[-1].accuracy = self.accuracy(*context.test_data_sample)

        print(training_log[-1])

        figure = core.persistent_variable('figure', lambda: dv.Figure(size=(8, 6)))
        chart = core.persistent_variable('chart', lambda: dv.Chart2d(figure=figure))
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
    generated_data = LogisticRegression2DataGenerator().generate()
    
    # shuffle
    generated_data = stats.mseries.shuffle(generated_data)

    # chart
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(generated_data[0], generated_data[1], color='red')
    chart.scatter(generated_data[0], generated_data[2], color='blue')
    figure.show()

    # splitting data
    (training_data, test_data) = stats.mseries.split(generated_data[:2], 0.75)
    # print(training_data, test_data)

    model = LogisticRegression2Model()
    model.train(training_data=training_data, batch_size=64,
                test_data=test_data,
                training_data_sample=stats.mseries.sample(training_data, 256),
                test_data_sample=stats.mseries.sample(test_data, 256))

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()

