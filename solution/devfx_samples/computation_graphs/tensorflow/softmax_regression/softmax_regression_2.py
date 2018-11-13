import numpy as np
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class SoftmaxRegression1DataGenerator(object):
    def __init__(self):
        pass

    def generate(self, M):
        x11 = stats.normal(mu=2.0, sigma=1.0).rvs(M)
        x12 = stats.normal(mu=6.0, sigma=1.0).rvs(M)
        x21 = stats.normal(mu=2.0, sigma=1.0).rvs(M)
        x22 = stats.normal(mu=6.0, sigma=1.0).rvs(M)
        # print(x11, x12, x21, x22)

        xs11 = np.array([x11, x21]).T
        ys11 = np.array([[1] for _ in np.arange(0, M)])
        # print(xs11, ys11)

        xs12 = np.array([x12, x21]).T
        ys12 = np.array([[2] for _ in np.arange(0, M)])
        # print(xs12, ys12)

        xs21 = np.array([x11, x22]).T
        ys21 = np.array([[3] for _ in np.arange(0, M)])
        # print(xs21, ys21)

        xs22 = np.array([x12, x22]).T
        ys22 = np.array([[4] for _ in np.arange(0, M)])
        # print(xs22, ys22)

        x = np.vstack((xs11, xs12, xs21, xs22))
        y = np.vstack((ys11, ys12, ys21, ys22))
        # print(x, y)

        permutation = np.random.permutation(np.arange(start=0, stop=4*M, step=1))
        # print(permutation)

        x = x[permutation]
        y = y[permutation]
        # print(x, y)

        return [x, y]

"""------------------------------------------------------------------------------------------------
"""
class SoftmaxRegression1ModelTrainer(cg.models.DeclarativeModelTrainer):
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

    def _on_append_to_training_log(self, training_log, context):
        training_log.last_item.cost_on_training_data = self.run_cost_evaluator(input_data=context.training_data[0], output_data=context.training_data[1])
        if(len(training_log.nr_list) >= 2):
            training_log.last_item.trend_of_cost_on_training_data = stats.normalized_trend(x=training_log.nr_list, y=training_log.cost_on_training_data_list, n_max=32)[0]*360/(2.0*np.pi)
            context.cancellation_token.request_cancellation(condition=(abs(training_log.last_item.trend_of_cost_on_training_data) <= 1e-2))
        training_log.last_item.cost_on_test_data = self.run_cost_evaluator(input_data=context.test_data[0], output_data=context.test_data[1])
        output_pred, output = (self.run_evaluator(name='output_pred', feeds_data=[context.test_data[0]]), context.test_data[1])
        training_log.last_item.accuracy = np.mean([output_pred[:,0] == output[:,0]])

        print(training_log.last_item)

        figure, chart = dv.PersistentFigure(id='status', size=(8, 6), chart_fns=[lambda _: dv.Chart2d(figure=_)])
        chart.plot(training_log.cost_on_training_data_list, color='green')
        figure.refresh()

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass

"""------------------------------------------------------------------------------------------------
"""
# generating data
data_generator = SoftmaxRegression1DataGenerator()
data = data_generator.generate(M=16)

# splitting data
(training_data, test_data) = stats.Splitter().split(data)
print(training_data, test_data)

# learning from data
model_trainer = SoftmaxRegression1ModelTrainer()
model_trainer.train(training_data=training_data, batch_size=64,
                    test_data=test_data)


model_trainer.close()

