import numpy as np
import devfx.os as os
import devfx.core as core
import devfx.statistics as stats
import devfx.databases.hdf5 as db
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class MnistModel(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        # hypothesis
        x = cg.placeholder(shape=[None, 28, 28], name='x')

        w = cg.create_variable(name='w', shape=[10, 28, 28], initializer=cg.random_truncated_normal_initializer(stddev=1e-3, dtype=cg.float32))
        b = cg.create_variable(name='b', shape=[10], initializer=cg.random_truncated_normal_initializer(stddev=1e-3, dtype=cg.float32))
        z = cg.tensordot(x, w, axes=([1, 2], [1, 2])) + b

        h = nn.activation.softmax(z, axis=1)

        y_pred = cg.cast_to_uint8(cg.argmax(h, axis=1))
        self.register_evaluator(name='output_pred', evaluatee=y_pred, feeds=[x])

        # cost function
        y = cg.placeholder(shape=[None], dtype=cg.uint8, name='y')
        y_one_hot = cg.one_hot(indices=y, depth=10, on_value=1, off_value=0)
        J = -cg.reduce_mean(cg.reduce_sum(cg.cast_to_float32(y_one_hot)*cg.log(h+1e-16), axis=1))

        # accuracy
        accuracy = cg.reduce_mean(cg.cast_to_float32(cg.equal(y_pred, y)))
        self.register_evaluator(name='accuracy', evaluatee=accuracy, feeds=[x, y])

        # evaluators
        self.register_input_evaluator(input=input)
        self.register_output_evaluator(output=y)
        self.register_hypothesis_evaluator(hypothesis=h, input=x)
        self.register_cost_evaluator(cost=J, input=x, output=y)

        # cost minimizer
        self.register_cost_optimizer_applier_evaluator(cost=J, input=x, output=y, optimizer=cg.train.AdamOptimizer(learning_rate=1e-5))

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].training_data_cost = self.run_cost_evaluator(*context.training_data_sample)
        training_log[-1].test_data_cost = self.run_cost_evaluator(*context.test_data_sample)
        training_log[-1].accuracy = self.run_evaluator(name='accuracy', feeds_data=context.test_data_sample)

        print(training_log[-1])

        figure = core.persistentvariable('figure', lambda: dv.Figure(size=(8, 6)))
        chart = core.persistentvariable('chart', lambda: dv.Chart2d(figure=figure))
        figure.clear_charts()
        chart.plot(training_log[:].training_data_cost, color='green')
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
    data_path = 'i:/Dev.Databases/mnist'

    training_data_file = db.File(os.path.join(data_path, 'mnist_train.hdf5'))
    training_data = [training_data_file.get_dataset('/images'), training_data_file.get_dataset('/labels')]

    test_data_file = db.File(os.path.join(data_path, 'mnist_test.hdf5'))
    test_data = [test_data_file.get_dataset('/images'), test_data_file.get_dataset('/labels')]

    model = MnistModel()
    model.train(training_data=training_data, batch_size=32,
                test_data=test_data,
                training_data_sample = stats.mseries.sample(training_data, 1024),
                test_data_sample = stats.mseries.sample(test_data, 1024))
    model.close()

    test_data_file.close()
    training_data_file.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()

