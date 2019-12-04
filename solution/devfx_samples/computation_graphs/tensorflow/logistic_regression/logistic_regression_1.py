import numpy as np
import devfx.core as core
import devfx.mathematics as math
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class LogisticRegression1DataGenerator(object):
    def __init__(self):
        pass

    def generate(self):
        M = 1024*256
        w0 = 3.0
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

        return [data[:M,0], data[:M,1], data[:M,2]]

"""------------------------------------------------------------------------------------------------
"""
class LogisticRegression1Model(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        # hypothesis
        x = cg.placeholder(shape=[None], name='x')
        w0 = cg.create_variable(name='w0', shape=[1], initializer=cg.zeros_initializer())
        w1 = cg.create_variable(name='w1', shape=[1], initializer=cg.zeros_initializer())
        h = 1.0/(1.0 + cg.exp(-(w0 + w1*x)))

        # cost function
        y = cg.placeholder(shape=[None], name='y')
        J = -cg.reduce_mean(y*cg.log(h)+(1-y)*cg.log(1-h))

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

    def _on_training_iteration_begin(self, iteration, context):
        pass


    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].training_data_cost = self.run_cost_evaluator(*context.training_data)
        if(len(training_log) >= 2):
            training_log[-1].trend_of_training_data_cost = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].trend_of_training_data_cost) <= 1e-2))

        training_log[-1].test_data_cost = self.run_cost_evaluator(*context.test_data)
        
        training_log[-1].w = [_[0] for _ in self.run_evaluator(name='weight')]

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
    generated_data = LogisticRegression1DataGenerator().generate()
    
    # shuffle
    generated_data = stats.mseries.shuffle(generated_data)

    # chart
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(generated_data[1], generated_data[0], color='red')
    chart.scatter(generated_data[1], generated_data[2])
    figure.show()

    # splitting data
    (training_data, test_data) = stats.mseries.split(generated_data[1:3], 0.75)
    # print(training_data, test_data)

    model = LogisticRegression1Model()
    model.train(training_data=training_data, batch_size=256,
                test_data=test_data)

    model.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()

