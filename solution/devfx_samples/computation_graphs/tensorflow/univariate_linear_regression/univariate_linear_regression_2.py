import numpy as np
import devfx.data_containers as dc
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class UnivariateLinearRegressionDataGenerator():
    def __init__(self):
        pass

    def generate(self):
        M = 1024*256
        a = 1.0
        b = 0.75
        x = np.random.normal(0.0, 0.5, size=M)
        y = a*x + b + np.random.normal(0.0, 0.1, size=M)
        return [x, y]

"""------------------------------------------------------------------------------------------------
"""
class UnivariateLinearRegressionModelTrainer(cg.models.DeclarativeModelTrainer):
    # ----------------------------------------------------------------
    def __build_model(self, name, x, y, device):
        with cg.scope(name):
            # hypothesis
            w0 = cg.create_or_get_variable(name='w0', shape=[1], initializer=cg.zeros_initializer(), device='/cpu:0')
            w1 = cg.create_or_get_variable(name='w1', shape=[1], initializer=cg.zeros_initializer(), device='/cpu:0')
            h = w0 + w1*x

            # cost function
            J = 0.5*cg.reduce_mean(cg.square(h-y))

            # evaluators
            self.register_evaluator(name=name+'_input', evaluatee=x, hparams=())
            self.register_evaluator(name=name+'_weight', evaluatee=[w0, w1], hparams=())
            self.register_evaluator(name=name+'_output', evaluatee=y, hparams=())
            self.register_evaluator(name=name+'_hypothesis', evaluatee=h, feeds=[x], hparams=())
            self.register_evaluator(name=name+'_cost', evaluatee=J, feeds=[x, y], hparams=())

        return J

    def _build_model(self):
        # --------------------------------
        x = cg.placeholder(shape=[None], name='x')
        y = cg.placeholder(shape=[None], name='y')

        # --------------------------------
        # device = '/cpu:0'
        # with cg.device(device):
        #     J = self.__build_model(name='cpu', x=x, y=y, device=device)
        # Js = [J]

        # --------------------------------
        devices = ['/cpu:0']
        x2 = cg.split(x, len(devices))
        y2 = cg.split(y, len(devices))
        Js = []
        for i, device in enumerate(devices):
            with cg.device(device):
                cost = self.__build_model(name='gpu_'+str(i+1), x=x2[i], y=y2[i], device=device)
                Js.append(cost)

        # --------------------------------
        self.register_cost_optimizer_applier_evaluator(cost=Js, input=x, output=y, optimizer=cg.train.AdamOptimizer(learning_rate=1e-2))

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log.last_item.cost_on_training_data = self.run_evaluator(name='gpu_1_cost', feeds_data=[context.training_data[0], context.training_data[1]])
        if(len(training_log.nr_list) >= 2):
            training_log.last_item.trend_of_cost_on_training_data = stats.normalized_trend(x=training_log.nr_list, y=training_log.cost_on_training_data_list, n_max=32)[0]*360/(2.0*np.pi)
            context.cancellation_token.request_cancellation(condition=(abs(training_log.last_item.trend_of_cost_on_training_data) <= 1e-2))
        training_log.last_item.cost_on_test_data = self.run_evaluator(name='gpu_1_cost', feeds_data=[context.test_data[0], context.test_data[1]])
        training_log.last_item.w = [_[0] for _ in self.run_evaluator(name='gpu_1_weight')]

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
generated_data = UnivariateLinearRegressionDataGenerator().generate()
dataset = dc.Dataset(data=generated_data)

figure = dv.Figure(size=(8, 6))
chart = dv.Chart2d(figure=figure)
chart.scatter(dataset[0], dataset[1])
figure.show()

# splitting data
(training_dataset, test_dataset) = dataset.split()
# print(training_dataset, test_dataset)

# learning from data
model_trainer = UnivariateLinearRegressionModelTrainer()
model_trainer.train(training_data=training_dataset, batch_size=256,
                    test_data=test_dataset)

# validation
figure = dv.Figure(size=(8, 6))
chart = dv.Chart2d(figure=figure)
chart.scatter(test_dataset[0], test_dataset[1], color='blue')
chart.scatter(test_dataset[0], model_trainer.run_evaluator(name='gpu_1_hypothesis', feeds_data=[test_dataset[0]]), color='red')
figure.show()

model_trainer.close()


