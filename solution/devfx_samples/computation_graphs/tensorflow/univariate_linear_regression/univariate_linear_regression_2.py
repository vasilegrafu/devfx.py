import numpy as np
import tensorflow as tf
import devfx.core as core
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class UnivariateLinearRegressionDataGenerator():
    def __init__(self):
        pass

    def generate(self):
        M = 1024
        a = 1.0
        b = 0.75
        x = np.random.normal(0.0, 0.5, size=M)
        y = a*x + b + np.random.normal(0.0, 0.1, size=M)
        return [x, y]

"""------------------------------------------------------------------------------------------------
"""
class UnivariateLinearRegressionModel(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def __build_model(self, name, x, y):
        # hypothesis
        w0 = cg.create_or_get_variable(name='w0', shape=[1], initializer=cg.zeros_initializer())
        w1 = cg.create_or_get_variable(name='w1', shape=[1], initializer=cg.zeros_initializer())
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

    def __init__(self):
        self.devices = ['/cpu:0', '/cpu:1']

        config = tf.ConfigProto(intra_op_parallelism_threads=2,
                                inter_op_parallelism_threads=2,  
                                allow_soft_placement=True, 
                                device_count={"CPU": 2})
        super().__init__(config=config)

    def _build_model(self):
        # --------------------------------
        x = cg.placeholder(shape=[None], name='x')
        y = cg.placeholder(shape=[None], name='y')

        # --------------------------------
        xs = cg.split(x, len(self.devices))
        ys = cg.split(y, len(self.devices))
        Js = []
        for i, device in enumerate(self.devices):
            with cg.device(device):
                cost = self.__build_model(name=device, x=xs[i], y=ys[i])
                Js.append(cost)

        # --------------------------------
        self.register_cost_optimizer_applier_evaluator(cost=Js, input=x, output=y, optimizer=cg.train.AdamOptimizer(learning_rate=1e-2))

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].training_data_cost = self.run_evaluator(name=self.devices[0]+'_cost', feeds_data=[*context.training_data])
        if(len(training_log) >= 2):
            training_log[-1].trend_of_training_data_cost = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].trend_of_training_data_cost) <= 1e-2))

        training_log[-1].test_data_cost = self.run_evaluator(name=self.devices[0]+'_cost', feeds_data=[*context.test_data])

        training_log[-1].w = [_[0] for _ in self.run_evaluator(name=self.devices[0]+'_weight')]

        print(training_log[-1])

        figure = core.persistentvariable('figure', lambda: dv.Figure(size=(8, 6)))
        chart = core.persistentvariable('chart', lambda: dv.Chart2d(figure=figure))
        figure.clear_charts()
        chart.plot(training_log[:].training_data_cost, color='green')
        chart.plot(training_log[:].test_data_cost, color='red')
        figure.show(block=False)

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass

"""------------------------------------------------------------------------------------------------
"""
def main():
    # generating data
    generated_data = UnivariateLinearRegressionDataGenerator().generate()
    
    # shuffle
    generated_data = stats.mseries.shuffle(generated_data)

    # chart
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(generated_data[0], generated_data[1])
    figure.show()

    # splitting data
    (training_data, test_data) = stats.mseries.split(generated_data, 0.75)
    # print(training_data, test_data)

    # learning from data
    model = UnivariateLinearRegressionModel()
    model.train(training_data=training_data, batch_size=256,
                test_data=test_data)

    # validation
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(test_data[0], test_data[1], color='blue')
    chart.scatter(test_data[0], model.run_evaluator(name=model.devices[0]+'_hypothesis', feeds_data=[test_data[0]]), color='red')
    figure.show()

    model.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()
