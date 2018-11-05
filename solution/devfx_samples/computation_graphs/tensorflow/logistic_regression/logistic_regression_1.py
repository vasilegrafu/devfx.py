import numpy as np
import devfx.mathematics as math
import devfx.data_containers as dc
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class LogisticRegression1DataGenerator(object):
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
            x = stats.uniform(a=a, b=b).rvs(block)
            y = stats.bernoulli(0.5).rvs(block)
            p = math.logistic(w0 + w1*x)

            to_accept = stats.bernoulli(p).rvs(block)
            _p = p[(y == 1) & (to_accept == 1)]
            _x = x[(y == 1) & (to_accept == 1)]
            _y = y[(y == 1) & (to_accept == 1)]
            for _ in zip(_p, _x, _y):
                data.append([_[0], _[1], _[2]])

            to_accept = stats.bernoulli(1-p).rvs(block)
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
class LogisticRegression1ModelTrainer(cg.models.DeclarativeModelTrainer):
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
        self.construct_input_evaluator(input=input)
        self.construct_evaluatee_evaluator(name='weight', evaluatee=[w0, w1])
        self.construct_output_evaluator(output=y)
        self.construct_hypothesis_evaluator(hypothesis=h, input=x)
        self.construct_cost_evaluator(cost=J, input=x, output=y)

        # cost minimizer
        self.construct_cost_optimizer_applier_evaluator(cost=J, input=x, output=y, optimizer=cg.train.AdamOptimizer(learning_rate=1e-4))

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
        training_log.last_item.w = [_[0] for _ in self.run_evaluator(name='weight')]

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
generated_data = LogisticRegression1DataGenerator().generate()
dataset = dc.Dataset(data=generated_data)

figure = dv.Figure(size=(8, 6))
chart = dv.Chart2d(figure=figure)
chart.scatter(dataset[1], dataset[0], color='red')
chart.scatter(dataset[1], dataset[2])
figure.show()

# splitting data
(training_dataset, test_dataset) = dataset.split()
print(training_dataset, test_dataset)

model_trainer = LogisticRegression1ModelTrainer()
model_trainer.train(training_data=training_dataset[1, 2], batch_size=64,
                    test_data=test_dataset[1, 2])

model_trainer.close()

