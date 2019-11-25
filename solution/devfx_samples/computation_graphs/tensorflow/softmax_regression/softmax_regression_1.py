import numpy as np
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.data_vizualization.seaborn as dv
import devfx.statistics.mseries as mseries

"""------------------------------------------------------------------------------------------------
"""
class SoftmaxRegression1DataGenerator(object):
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
class SoftmaxRegression1Model(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        # hypothesis
        x = cg.placeholder(shape=[None, 2], dtype=cg.float32, name='x')

        w10 = cg.create_variable(name='w10', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        w11 = cg.create_variable(name='w11', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        w12 = cg.create_variable(name='w12', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        z1 = w10 + w11*x[:, 0] + w12*x[:, 1]

        w20 = cg.create_variable(name='w20', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        w21 = cg.create_variable(name='w21', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        w22 = cg.create_variable(name='w22', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        z2 = w20 + w21*x[:, 0] + w22*x[:, 1]

        w30 = cg.create_variable(name='w30', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        w31 = cg.create_variable(name='w31', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        w32 = cg.create_variable(name='w32', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        z3 = w30 + w31*x[:, 0] + w32*x[:, 1]

        w40 = cg.create_variable(name='w40', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        w41 = cg.create_variable(name='w41', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        w42 = cg.create_variable(name='w42', shape=[1], dtype=cg.float32, initializer=cg.zeros_initializer())
        z4 = w40 + w41*x[:, 0] + w42*x[:, 1]

        h = cg.convert_to_tensor([
            cg.exp(z1)/(cg.exp(z1) + cg.exp(z2) + cg.exp(z3) + cg.exp(z4)),
            cg.exp(z2)/(cg.exp(z1) + cg.exp(z2) + cg.exp(z3) + cg.exp(z4)),
            cg.exp(z3)/(cg.exp(z1) + cg.exp(z2) + cg.exp(z3) + cg.exp(z4)),
            cg.exp(z4)/(cg.exp(z1) + cg.exp(z2) + cg.exp(z3) + cg.exp(z4)),
        ], dtype=cg.float32, name='h')
        y_pred = cg.reshape(tensor=cg.argmax(h, axis=0) + 1, shape=[None, 1])

        # cost function
        y = cg.placeholder(shape=[None, 1], dtype=cg.int32, name='y')
        j1 = cg.iverson(cg.equal(y[:, 0], 1), cg.float32)*cg.log(h[0])
        j2 = cg.iverson(cg.equal(y[:, 0], 2), cg.float32)*cg.log(h[1])
        j3 = cg.iverson(cg.equal(y[:, 0], 3), cg.float32)*cg.log(h[2])
        j4 = cg.iverson(cg.equal(y[:, 0], 4), cg.float32)*cg.log(h[3])
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
        training_log[-1].training_data_cost = self.run_cost_evaluator(*context.training_data)
        if(len(training_log) >= 2):
            training_log[-1].trend_of_training_data_cost = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].trend_of_training_data_cost) <= 1e-1))

        training_log[-1].test_data_cost = self.run_cost_evaluator(*context.test_data)

        predicted_output, output = (self.run_evaluator(name='output_pred', feeds_data=[context.test_data[0]]), context.test_data[1])
        training_log[-1].accuracy = np.mean([predicted_output[:, 0] == output[:, 0]])

        print(training_log[-1])

        x = training_log[:].training_data_cost[-1]

        figure, chart = dv.PersistentFigure(id='status', size=(8, 6), chart_fns=[lambda _: dv.Chart2d(figure=_)])
        chart.plot(training_log[:].training_data_cost, color='green')
        chart.plot(training_log[:].test_data_cost, color='red')
        figure.refresh()

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass


"""------------------------------------------------------------------------------------------------
"""
def main():
    # generating data
    generated_data = SoftmaxRegression1DataGenerator().generate(M=1024*4)
    
    # shuffle
    generated_data = mseries.shuffle(generated_data)

    # splitting data
    (training_data, test_data) = mseries.split(generated_data, int(0.75*mseries.rows_count(generated_data)))
    # print(training_data, test_data)

    # learning from data
    model = SoftmaxRegression1Model()
    model.train(training_data=training_data, batch_size=64,
                test_data=test_data)

    model.close()


"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()