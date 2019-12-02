import numpy as np
import devfx.core as core
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class SoftmaxRegression2DataGenerator(object):
    def __init__(self):
        pass

    def generate(self, M):
        cmin = stats.distributions.normal(mu=2.0, sigma=1.0).rvs(M)
        cmax = stats.distributions.normal(mu=8.0, sigma=1.0).rvs(M)
        # print(cmin, cmax)

        """ |21(3) 22(4)|
            |11(1) 12(2)|
        """
        
        xs11 = np.array([np.random.permutation(cmin), np.random.permutation(cmin)]).T
        ys11 = np.repeat([[1]], [M], axis=0)
        # print(xs11, ys11)

        xs12 = np.array([np.random.permutation(cmax), np.random.permutation(cmin)]).T
        ys12 = np.repeat([[2]], [M], axis=0)
        # print(xs12, ys12)

        xs21 = np.array([np.random.permutation(cmin), np.random.permutation(cmax)]).T
        ys21 = np.repeat([[3]], [M], axis=0)
        # print(xs21, ys21)

        xs22 = np.array([np.random.permutation(cmax), np.random.permutation(cmax)]).T
        ys22 = np.repeat([[4]], [M], axis=0)
        # print(xs22, ys22)

        x = np.vstack((xs11, xs12, xs21, xs22))
        y = np.vstack((ys11, ys12, ys21, ys22))
        # print(x, y)
        # print(np.shape(x), np.shape(y))

        return [x, y]

"""------------------------------------------------------------------------------------------------
"""
class SoftmaxRegression2Model(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        # hypothesis
        x = cg.placeholder(shape=[None, 2], name='x')

        w0 = cg.create_variable(name='w0', shape=[4], initializer=cg.zeros_initializer())
        w = cg.create_variable(name='w', shape=[4,2], initializer=cg.zeros_initializer())

        """ |w10|  +  |x11 x12|  x  |w11 w12|  =  |(w10+x11*w11+x12*w12) (w20+x11*w21+x12*w22) (w30+x11*w31+x12*w32) (w40+x11*w41+x12*w42)| 
            |w20|     |x21 x22|     |w21 w22|     |(w10+x21*w11+x22*w12) (w20+x21*w21+x22*w22) (w30+x21*w31+x22*w32) (w40+x21*w41+x22*w42)| 
            |w30|     |x31 x32|     |w31 w32|     |(w10+x31*w11+x32*w12) (w20+x31*w21+x32*w22) (w30+x31*w31+x32*w32) (w40+x31*w41+x32*w42)| 
            |w40|     |x41 x42|     |w41 w42|     |(w10+x41*w11+x42*w12) (w20+x41*w21+x42*w22) (w30+x41*w31+x42*w32) (w40+x41*w41+x42*w42)|  
                      ...                         ...                     
                      |xm1 xm2|                   |(w10+xm1*w11+xm2*w12) (w20+xm1*w21+xm2*w22) (w30+xm1*w31+xm2*w32) (w40+xm1*w41+xm2*w42)|  
        """
        # z = w0 + cg.einsum('mj,ij->mi', x, w)
        z = w0 + cg.tensordot(x, w, ([1], [1]))

        h = nn.activation.softmax(z, axis=1)
        y_pred = cg.reshape(tensor=cg.argmax(h, axis=1) + 1, shape=[None, 1])

        # cost function
        y = cg.placeholder(shape=[None, 1], dtype=cg.int32, name='y')
        y_one_hot = cg.one_hot(indices=y[:,0]-1, depth=4, on_value=1, off_value=0)
        J = -cg.reduce_mean(cg.reduce_sum(cg.cast(y_one_hot, h.dtype)*cg.log(h+1e-16), axis=1))


        # evaluators
        self.register_input_evaluator(input=input)
        self.register_output_evaluator(output=y)
        self.register_hypothesis_evaluator(hypothesis=h, input=x)
        self.register_evaluator(name='output_pred', evaluatee=y_pred, feeds=[x])
        self.register_cost_evaluator(cost=J, input=x, output=y)

        # cost minimizer
        self.register_cost_optimizer_applier_evaluator(input=x, output=y, cost=J, optimizer=cg.train.AdamOptimizer(learning_rate=1e-2))

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 100 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].training_data_cost = self.run_cost_evaluator(*context.training_data)
        if(len(training_log) >= 2):
            training_log[-1].trend_of_training_data_cost = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].trend_of_training_data_cost) <= 1e-2))

        training_log[-1].test_data_cost = self.run_cost_evaluator(*context.test_data)

        predicted_output, output = (self.run_evaluator(name='output_pred', feeds_data=[context.test_data[0]]), context.test_data[1])
        training_log[-1].accuracy = np.mean([predicted_output[:, 0] == output[:, 0]])

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
    generated_data = SoftmaxRegression2DataGenerator().generate(M=1024*256)
    
    # shuffle
    generated_data = stats.mseries.shuffle(generated_data)

    # splitting data
    (training_data, test_data) = stats.mseries.split(generated_data, 0.75)
    # print(training_data, test_data)

    # learning from data
    model = SoftmaxRegression2Model()
    model.train(training_data=training_data, batch_size=64,
                test_data=test_data)

    model.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()