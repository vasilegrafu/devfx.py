import numpy as np
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class SoftmaxRegression1DataGenerator(object):
    def __init__(self):
        pass

    def generate(self, M):
        x11 = stats.distributions.normal(mu=2.0, sigma=1.0).rvs(M)
        x12 = stats.distributions.normal(mu=6.0, sigma=1.0).rvs(M)
        x21 = stats.distributions.normal(mu=2.0, sigma=1.0).rvs(M)
        x22 = stats.distributions.normal(mu=6.0, sigma=1.0).rvs(M)
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
class SoftmaxRegression1Model(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        # hypothesis
        x = cg.placeholder(shape=[None, 2], name='x')

        w10 = cg.create_variable(name='w10', shape=[1], initializer=cg.zeros_initializer())
        w11 = cg.create_variable(name='w11', shape=[1], initializer=cg.zeros_initializer())
        w12 = cg.create_variable(name='w12', shape=[1], initializer=cg.zeros_initializer())

        w20 = cg.create_variable(name='w20', shape=[1], initializer=cg.zeros_initializer())
        w21 = cg.create_variable(name='w21', shape=[1], initializer=cg.zeros_initializer())
        w22 = cg.create_variable(name='w22', shape=[1], initializer=cg.zeros_initializer())

        w30 = cg.create_variable(name='w30', shape=[1], initializer=cg.zeros_initializer())
        w31 = cg.create_variable(name='w31', shape=[1], initializer=cg.zeros_initializer())
        w32 = cg.create_variable(name='w32', shape=[1], initializer=cg.zeros_initializer())

        w40 = cg.create_variable(name='w40', shape=[1], initializer=cg.zeros_initializer())
        w41 = cg.create_variable(name='w41', shape=[1], initializer=cg.zeros_initializer())
        w42 = cg.create_variable(name='w42', shape=[1], initializer=cg.zeros_initializer())

        z1 = w10 + w11*x[:, 0] + w12*x[:, 1]
        z2 = w20 + w21*x[:, 0] + w22*x[:, 1]
        z3 = w30 + w31*x[:, 0] + w32*x[:, 1]
        z4 = w40 + w41*x[:, 0] + w42*x[:, 1]

        h = cg.convert_to_tensor([
            cg.exp(z1)/(cg.exp(z1) + cg.exp(z2) + cg.exp(z3) + cg.exp(z4)),
            cg.exp(z2)/(cg.exp(z1) + cg.exp(z2) + cg.exp(z3) + cg.exp(z4)),
            cg.exp(z3)/(cg.exp(z1) + cg.exp(z2) + cg.exp(z3) + cg.exp(z4)),
            cg.exp(z4)/(cg.exp(z1) + cg.exp(z2) + cg.exp(z3) + cg.exp(z4)),
        ])
        y_pred = cg.reshape(tensor=cg.argmax(h, axis=0) + 1, shape=[None, 1])

        # cost function
        y = cg.placeholder(shape=[None, 1], dtype=cg.int32, name='y')
        j1 = cg.cast(cg.iverson(cg.equal(y[:, 0], 1)), h.dtype)*cg.log(h[0])
        j2 = cg.cast(cg.iverson(cg.equal(y[:, 0], 2)), h.dtype)*cg.log(h[1])
        j3 = cg.cast(cg.iverson(cg.equal(y[:, 0], 3)), h.dtype)*cg.log(h[2])
        j4 = cg.cast(cg.iverson(cg.equal(y[:, 0], 4)), h.dtype)*cg.log(h[3])
        J = -cg.reduce_mean(j1 + j2 + j3 + j4)

        # evaluators
        self.register_input_evaluator(input=input)
        self.register_output_evaluator(output=y)
        self.register_hypothesis_evaluator(hypothesis=h, input=x)
        self.register_evaluator(name='output_pred', evaluatee=y_pred, feeds=[x])
        self.register_cost_evaluator(cost=J, input=x, output=y)

        # cost minimizer
        self.register_cost_optimizer_applier_evaluator(cost=J, input=x, output=y, optimizer=cg.train.AdamOptimizer(learning_rate=1e-2))

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 100 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log.last_item.training_data_cost = self.run_cost_evaluator(input_data=context.training_data[0], output_data=context.training_data[1])
        if(len(training_log.nr_list) >= 2):
            training_log.last_item.trend_of_training_data_cost = stats.regression.normalized_trend(x=training_log.nr_list, y=training_log.training_data_cost_list, n_max=32)[0]*360/(2.0*np.pi)
            context.cancellation_token.request_cancellation(condition=(abs(training_log.last_item.trend_of_training_data_cost) <= 1e-2))
        training_log.last_item.test_data_cost = self.run_cost_evaluator(input_data=context.test_data[0], output_data=context.test_data[1])
        predicted_output, output = (self.run_evaluator(name='output_pred', feeds_data=[context.test_data[0]]), context.test_data[1])
        training_log.last_item.accuracy = np.mean([predicted_output[:, 0] == output[:, 0]])

        print(training_log.last_item)

        figure, chart = dv.PersistentFigure(id='status', size=(8, 6), chart_fns=[lambda _: dv.Chart2d(figure=_)])
        chart.plot(training_log.training_data_cost_list, color='green')
        figure.refresh()

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass

"""------------------------------------------------------------------------------------------------
"""
# generating data
data_generator = SoftmaxRegression1DataGenerator()
data = data_generator.generate(M=1024*256)

# splitting data
(training_data, test_data) = stats.preprocessing.Splitter().split(data)
# print(training_data, test_data)

# learning from data
model = SoftmaxRegression1Model()
model.train(training_data=training_data, batch_size=64,
            test_data=test_data)

model.close()
