import numpy as np
import devfx.core as core
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class FunctionAproximationDataGenerator(object):
    def __init__(self):
        pass

    def generate(self, M):
        x = stats.distributions.uniform(a=-4*3.14, b=+4.0*3.14).rvs(M)
        y = np.cos(x)*x + np.random.normal(0.0, 1.0, size=M)

        x = [[_] for _ in x]
        y = [[_] for _ in y]

        return [x, y]

"""------------------------------------------------------------------------------------------------
"""
class FunctionAproximationModel(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        # hypothesis
        x = cg.placeholder(shape=[None, 1], name='x')

        fc1 = nn.layers.fully_connected(name="fc1",
                                        input=x,
                                        n=64,
                                        initializer=nn.initialization.random_truncated_normal_initializer(),
                                        activation_fn=nn.activation.sigmoid)

        fc2 = nn.layers.fully_connected(name="fc2",
                                        input=fc1,
                                        n=64,
                                        initializer=nn.initialization.random_truncated_normal_initializer(),
                                        activation_fn=nn.activation.sigmoid)

        fc3 = nn.layers.fully_connected(name="fc3",
                                        input=fc2,
                                        n=64,
                                        initializer=nn.initialization.random_truncated_normal_initializer(),
                                        activation_fn=nn.activation.sigmoid)

        fco = nn.layers.fully_connected(name="fco",
                                        input=fc3,
                                        initializer=nn.initialization.random_truncated_normal_initializer(),
                                        n=1)

        h = fco

        # cost function
        y = cg.placeholder(shape=[None, 1], name='y')
        J = cg.sqrt(cg.reduce_mean(cg.square(h - y)))

        # evaluators
        self.register_input_evaluator(input=x)
        self.register_output_evaluator(output=y)
        self.register_hypothesis_evaluator(hypothesis=h, input=x)
        self.register_cost_evaluator(cost=J, input=x, output=y)

        # cost minimizer
        self.register_cost_optimizer_applier_evaluator(cost=J, input=x, output=y, optimizer=cg.train.AdamOptimizer(learning_rate=1e-3))

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 100 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        if (context.iteration % 500 == 0):
            context.batch_size = int(context.batch_size + 0) if context.batch_size < 1024 else 1024

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].batch_size = context.batch_size
        training_log[-1].training_data_cost = self.run_cost_evaluator(*context.training_data_sample)
        if(len(training_log) >= 2):
            training_log[-1].trend_of_training_data_cost = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].trend_of_training_data_cost) <= 1e-2))

        training_log[-1].test_data_cost = self.run_cost_evaluator(*context.test_data_sample)

        print(training_log[-1])

        figure = core.persistentvariable('figure', lambda: dv.Figure(size=(12, 4)))
        chart1 = core.persistentvariable('chart1', lambda: dv.Chart2d(figure=figure, position=121))
        chart2 = core.persistentvariable('chart2', lambda: dv.Chart2d(figure=figure, position=122))
        figure.clear_charts()
        chart1.plot(training_log[:].training_data_cost, color='green')
        chart2.scatter([_[0] for _ in context.test_data_sample[0]], [_[0] for _ in context.test_data_sample[1]], color='blue')
        chart2.plot([_[0] for _ in context.test_data_sample[0]], [_[0] for _ in self.run_hypothesis_evaluator(input_data=context.test_data_sample[0])], color='red')
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
    generated_data = FunctionAproximationDataGenerator().generate(M=1024*4)

    # shuffle
    generated_data = stats.mseries.shuffle(generated_data)

    # chart
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter([_[0] for _ in generated_data[0]], [_[0] for _ in generated_data[1]])
    figure.show()

    # splitting data
    (training_data, test_data) = stats.mseries.split(generated_data, 0.75)
    # print(training_data, test_data)

    # samples
    sample_count = 256
    training_data_sample = stats.mseries.sample(training_data, sample_count) 
    test_data_sample = stats.mseries.sample(test_data, sample_count) 
    # print(training_data_sample, test_data_sample)

    # learning from data
    model = FunctionAproximationModel()
    model.train(training_data=training_data, batch_size=32,
                training_data_sample = training_data_sample,
                test_data_sample = test_data_sample)

    model.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()

