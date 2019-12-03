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
class MnistModel(cg.Model):
    # ----------------------------------------------------------------
    def _build_model(self):
        def h(x):
            w = cg.Variable(name='w', initial_value=cg.random_truncated_normal(shape=(10, 28, 28), stddev=1e-3))
            b = cg.Variable(name='b', initial_value=cg.random_truncated_normal(shape=(10,), stddev=1e-3))
            z = cg.tensordot(cg.cast_to_float32(x), w, axes=([1, 2], [1, 2])) + b
            r = nn.activation.softmax(z, axis=1)
            return r

        def J(x, y):
            y_one_hot = cg.one_hot(indices=y, depth=10, on_value=1, off_value=0)
            hr = h(x)
            r = -cg.reduce_mean(cg.reduce_sum(cg.cast_to_float32(y_one_hot)*cg.log(hr), axis=1))
            return r

        def y_pred(x):
            hr = h(x)
            r = cg.argmax(hr, axis=1)
            return r

        def accuracy(x, y):
            y_predr = y_pred(x)
            r = cg.reduce_mean(cg.cast_to_float32(cg.equal(y_predr, y)))
            return r

        self.register_hypothesis_function(fn=h)
        self.register_cost_function(fn=J)
        self.register_apply_cost_optimizer_function(optimizer=cg.train.AdamOptimizer(learning_rate=1e-5))
        self.register_function(name='y_pred', fn=y_pred)
        self.register_function(name='accuracy', fn=accuracy)

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].training_data_cost = self.run_cost_function(*context.training_data_sample)
        training_log[-1].test_data_cost = self.run_cost_function(*context.test_data_sample)
        training_log[-1].accuracy = self.run_function('accuracy', *context.test_data_sample)

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

    # model = MnistModel()
    # model.train(training_data=training_data, batch_size=32,
    #             test_data=test_data,
    #             training_data_sample = stats.mseries.sample(training_data, 256),
    #             test_data_sample = stats.mseries.sample(test_data, 256))
    # model.close()

    # results = []
    # i = 1
    # while(i <= 20):
    #     model = MnistModel()
    #     result = model.train(training_data=training_data, batch_size=16,
    #                 test_data=test_data,
    #                 training_data_sample = stats.mseries.sample(training_data, 1024),
    #                 test_data_sample = stats.mseries.sample(test_data, 1024))
    #     model.close()

    #     results.append(result)
    #     print([_.iteration for _ in results], stats.series.mean([_.iteration for _ in results]))

    #     i += 1

    test_data_file.close()
    training_data_file.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()