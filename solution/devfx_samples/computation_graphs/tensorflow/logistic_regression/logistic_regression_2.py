import numpy as np
import devfx.mathematics as math
import devfx.data_containers as dc
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class LogisticRegression2DataGenerator(object):
    def __init__(self):
        pass

    def generate(self):
        M = 1024*4
        w0 = 2.0
        w1 = 0.75
        a = -16
        b = +16

        data = []
        block = M//2
        while (len(data) < M):
            x = stats.distributions.uniform(a=a, b=b).rvs(block)
            y = stats.distributions.bernoulli(0.5).rvs(block)
            p = math.logistic(w0 + w1*x)

            to_accept = stats.distributions.bernoulli(p).rvs(block)
            _p = p[(y == 1) & (to_accept == 1)]
            _x = x[(y == 1) & (to_accept == 1)]
            _y = y[(y == 1) & (to_accept == 1)]
            for _ in zip(_p, _x, _y):
                data.append([_[0], _[1], _[2]])

            to_accept = stats.distributions.bernoulli(1-p).rvs(block)
            _p = p[(y == 0) & (to_accept == 1)]
            _x = x[(y == 0) & (to_accept == 1)]
            _y = y[(y == 0) & (to_accept == 1)]
            for _ in zip(_p, _x, _y):
                data.append([_[0], _[1], _[2]])

        data = np.asarray(data).astype(dtype=np.float32)
        np.random.shuffle(data)

        return [data[:M,0], data[:M,1], data[:M,2]]

"""------------------------------------------------------------------------------------------------
"""
class LogisticRegression2Model(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        # hypothesis
        x = cg.placeholder(shape=[None], name='x')
        w0 = cg.create_variable(name='w0', shape=[1], initializer=cg.zeros_initializer())
        w1 = cg.create_variable(name='w1', shape=[1], initializer=cg.zeros_initializer())
        h = cg.stack([
            cg.exp(w0 + w1*x)/(1 + cg.exp(w0 + w1*x)),
                            1/(1 + cg.exp(w0 + w1*x))
        ])

        # cost function
        y = cg.placeholder(shape=[None], name='y')

        j1 = cg.cast(cg.iverson(cg.equal(y, 1)), h.dtype)*cg.log(h[0])
        j2 = cg.cast(cg.iverson(cg.equal(y, 0)), h.dtype)*cg.log(h[1])
        J = -cg.reduce_mean(j1 + j2)

        # evaluators
        self.register_input_evaluator(input=input)
        self.register_evaluator(name='weight', evaluatee=[w0, w1])
        self.register_output_evaluator(output=y)
        self.register_hypothesis_evaluator(hypothesis=h, input=x)
        self.register_cost_evaluator(cost=J, input=x, output=y)

        # cost minimizer
        self.register_cost_optimizer_applier_evaluator(cost=J, input=x, output=y, optimizer=cg.train.AdamOptimizer(learning_rate=1e-4))

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 100 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log.last_item.training_data_cost = self.run_cost_evaluator(*context.training_data)
        if(len(training_log.nr_list) >= 2):
            training_log.last_item.trend_of_training_data_cost = stats.regression.normalized_trend(x=training_log.nr_list, y=training_log.training_data_cost_list, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log.last_item.trend_of_training_data_cost) <= 1e-2))

        training_log.last_item.test_data_cost = self.run_cost_evaluator(*context.test_data)

        training_log.last_item.w =  [_[0] for _ in self.run_evaluator(name='weight')]

        print(training_log.last_item)

        figure, chart = dv.PersistentFigure(id='status', size=(8, 6), chart_fns=[lambda _: dv.Chart2d(figure=_)])
        chart.plot(training_log.training_data_cost_list, color='green')
        chart.plot(training_log.test_data_cost_list, color='red')
        figure.refresh()

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass

"""------------------------------------------------------------------------------------------------
"""
def main():
    # generating data
    generated_data = LogisticRegression2DataGenerator().generate()

    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(generated_data[1], generated_data[0], color='red')
    chart.scatter(generated_data[1], generated_data[2])
    figure.show()

    # splitting data
    split_bound = int(0.75*len(generated_data[0]))
    training_data = [generated_data[1][:split_bound], generated_data[2][:split_bound]]
    test_data = [generated_data[1][split_bound:], generated_data[2][split_bound:]]
    # print(training_data, test_data)

    # learning from data
    model = LogisticRegression2Model()
    model.train(training_data=training_data, batch_size=64,
                test_data=test_data)

    model.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()

