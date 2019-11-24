import numpy as np
import devfx.data_containers as dc
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv
import devfx.statistics.mseries as mseries

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
        training_log.last_item.batch_size = context.batch_size
        training_log.last_item.training_data_cost = self.run_cost_evaluator(*context.training_data_sample)
        if(len(training_log.nr_list) >= 2):
            training_log.last_item.trend_of_training_data_cost = stats.regression.normalized_trend(x=training_log.nr_list, y=training_log.training_data_cost_list, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log.last_item.trend_of_training_data_cost) <= 1e-2))

        training_log.last_item.test_data_cost = self.run_cost_evaluator(*context.test_data_sample)

        print(training_log.last_item)

        figure, chart1, chart2 = dv.PersistentFigure(id='status', size=(12, 4), chart_fns=[lambda _: dv.Chart2d(figure=_, position=121), lambda _: dv.Chart2d(figure=_, position=122)])
        chart1.plot(training_log.training_data_cost_list, color='green')
        chart2.scatter([_[0] for _ in context.test_data_sample[0]], [_[0] for _ in context.test_data_sample[1]], color='blue')
        chart2.plot([_[0] for _ in context.test_data_sample[0]], [_[0] for _ in self.run_hypothesis_evaluator(input_data=context.test_data_sample[0])], color='red')
        figure.refresh()

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
    generated_data = mseries.shuffle(generated_data)

    # chart
    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(*[[__[0] for __ in _] for _ in generated_data])
    figure.show()

    # splitting data
    (training_data, test_data) = mseries.split(generated_data, int(0.75*mseries.rows_count(generated_data)))
    # print(training_data, test_data)

    # samples
    sample_count = 512
    training_data_sample = mseries.get(training_data, slice(None, sample_count)) 
    test_data_sample = mseries.get(test_data, slice(None, sample_count)) 
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

