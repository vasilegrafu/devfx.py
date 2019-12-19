import numpy as np
import devfx.core as core
import devfx.statistics as stats
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class SoftmaxRegression2DataGenerator(object):
    def __init__(self):
        pass

    def generate(self):
        M=1024*4

        cmin = stats.distributions.normal(mu=2.0, sigma=1.0).rvs(M)
        cmax = stats.distributions.normal(mu=8.0, sigma=1.0).rvs(M)
        # print(cmin, cmax)

        """ |21(3) 22(4)|
            |11(1) 12(2)|
        """
        
        xs11 = np.array([np.random.permutation(cmin), np.random.permutation(cmin)]).T
        ys11 = np.repeat([1], [M], axis=0)
        # print(xs11, ys11)

        xs12 = np.array([np.random.permutation(cmax), np.random.permutation(cmin)]).T
        ys12 = np.repeat([2], [M], axis=0)
        # print(xs12, ys12)

        xs21 = np.array([np.random.permutation(cmin), np.random.permutation(cmax)]).T
        ys21 = np.repeat([3], [M], axis=0)
        # print(xs21, ys21)

        xs22 = np.array([np.random.permutation(cmax), np.random.permutation(cmax)]).T
        ys22 = np.repeat([4], [M], axis=0)
        # print(xs22, ys22)

        x = np.vstack((xs11, xs12, xs21, xs22))
        y = np.hstack((ys11, ys12, ys21, ys22))
        # print(x, y)
        print(np.shape(x), np.shape(y))

        return [x, y]


"""------------------------------------------------------------------------------------------------
"""
class SoftmaxRegression2Model(ml.Model):
    # ----------------------------------------------------------------
    # @ml.build_graph(x=(ml.float32, (None, 2)))
    @ml.output_as_tensor((ml.float32, (None, 4)))
    @ml.input_as_tensor(x=(ml.float32, (None, 2)))
    def h(self, x):
        """ |x11 x12|  x  |w11 w12| + |b1|  =  |(x11*w11 + x12*w12 + b1) (x11*w21 + x12*w22 + b2) (x11*w31 + x12*w32 + b3) (x11*w41 + x12*w42 + b4)| 
            |x21 x22|     |w21 w22|   |b2|     |(x21*w11 + x22*w12 + b1) (x21*w21 + x22*w22 + b2) (x21*w31 + x22*w32 + b3) (x21*w41 + x22*w42 + b4)| 
            |x31 x32|     |w31 w32|   |b3|     |(x31*w11 + x32*w12 + b1) (x31*w21 + x32*w22 + b2) (x31*w31 + x32*w32 + b3) (x31*w41 + x32*w42 + b4)| 
            |x41 x42|     |w41 w42|   |b4|     |(x41*w11 + x42*w12 + b1) (x41*w21 + x42*w22 + b2) (x41*w31 + x42*w32 + b3) (x41*w41 + x42*w42 + b4)|  
              ...                                 ...                     
            |xm1 xm2|                          |(xm1*w11 + xm2*w12 + b1) (xm1*w21 + xm2*w22 + b2) (xm1*w31 + xm2*w32 + b3) (xm1*w41 + xm2*w42 + b4)|  
        """
        w = ml.create_or_get_variable(name='w', shape=(4, 2), dtype=ml.float32, initializer=ml.random_truncated_normal_initializer())
        b = ml.create_or_get_variable(name='b', shape=(4,), dtype=ml.float32, initializer=ml.random_truncated_normal_initializer())
        z = ml.tensordot(x, w, ([1], [1])) + b

        r = ml.softmax(z, axis=1)
        return r

    # @ml.build_graph(x=(ml.float32, (None, 2)), y=(ml.int32, (None,)))
    @ml.output_as_tensor((ml.float32, ()))
    @ml.input_as_tensor(x=(ml.float32, (None, 2)), y=(ml.int32, (None,)))
    def J(self, x, y):
        hr = self.h(x)
        r = -ml.reduce_mean(ml.reduce_sum(ml.one_hot(indices=(y-1), depth=4, on_value=1.0, off_value=0.0, axis=1)*ml.log(hr), axis=1))
        return r

    # @ml.build_graph(x=(ml.float32, (None, 2)))
    @ml.output_as_tensor((ml.int32, (None,)))
    @ml.input_as_tensor(x=(ml.float32, (None, 2)))
    def y_pred(self, x):
        hr = self.h(x)
        r = ml.argmax(hr, axis=1) + 1
        return r

    # @ml.build_graph(x=(ml.float32, (None, 2)), y=(ml.int32, (None,)))
    @ml.output_as_tensor((ml.float32, ()))
    @ml.input_as_tensor(x=(ml.float32, (None,2)), y=(ml.int32, (None,)))
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
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].training_data_cost_trend) <= 1e-1))
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
    generated_data = SoftmaxRegression2DataGenerator().generate()
    
    # shuffle
    generated_data = stats.mseries.shuffle(generated_data)

    # splitting data
    (training_data, test_data) = stats.mseries.split(generated_data, 0.75)
    # print(training_data, test_data)

    model = SoftmaxRegression2Model()
    model.train(training_data=training_data, batch_size=64,
                test_data=test_data,
                training_data_sample=stats.mseries.sample(training_data, 256),
                test_data_sample=stats.mseries.sample(test_data, 256))


"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()