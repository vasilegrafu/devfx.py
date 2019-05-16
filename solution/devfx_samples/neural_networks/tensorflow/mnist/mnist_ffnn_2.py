import numpy as np
import devfx.exceptions as exceps
import devfx.os as os
import devfx.databases.hdf5 as hdf5
import devfx.data_containers as dc
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv
from devfx_samples.neural_networks.tensorflow.mnist.data.mnist_dataset import MnistDataset

cg.enable_imperative_execution_mode()

"""------------------------------------------------------------------------------------------------
"""
class MnistModel(cg.models.ImperativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        def h(x):
            w = cg.create_or_get_variable(name='w', shape=[10, 28, 28, 1], initializer=cg.random_truncated_normal_initializer(stddev=1e-3, dtype=cg.float32))
            b = cg.create_or_get_variable(name='b', shape=[10], initializer=cg.random_truncated_normal_initializer(stddev=1e-3, dtype=cg.float32))
            z = cg.tensordot(cg.cast(x, cg.float32), w, axes=([1, 2, 3], [1, 2, 3])) + b
            r = nn.activation.softmax(z, axis=1)
            return r

        def J(x, y):
            y_one_hot = cg.one_hot(indices=y[:, 0], depth=10, on_value=1, off_value=0)
            hr = h(x)
            r = -cg.reduce_mean(cg.reduce_sum(cg.cast_to_float32(y_one_hot)*cg.log(hr+1e-16), axis=1))
            return r

        optimizer = cg.train.AdamOptimizer(learning_rate=1e-5)
        def apply_cost_optimizer(x, y):
            grads_and_vars = cg.train.implicit_gradients(J)(x, y)
            optimizer.apply_gradients(grads_and_vars)

        def accuracy(x, y):
            hr = h(x)
            y_pred = cg.cast_to_int32(cg.reshape(tensor=cg.argmax(hr, axis=1), shape=[None, 1]))
            r = cg.reduce_mean(cg.cast_to_float32(cg.equal(y_pred[:, 0], y[:, 0])))
            return r

        self.register_hypothesis_function(fn=h)
        self.register_cost_function(fn=J)
        self.register_function(name='apply_cost_optimizer', fn=apply_cost_optimizer)
        self.register_function(name='accuracy', fn=accuracy)

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_training_apply_cost_optimizer(self, context):
        self.run_function('apply_cost_optimizer', context.iteration_training_data[0], context.iteration_training_data[1])

    def _on_append_to_training_log(self, training_log, context):
        training_log.last_item.training_data_cost = self.run_cost_function(context.training_data_sample[0], context.training_data_sample[1])
        training_log.last_item.test_data_cost = self.run_cost_function(context.test_data_sample[0], context.test_data_sample[1])
        training_log.last_item.accuracy = self.run_function('accuracy', context.test_data_sample[0], context.test_data_sample[1])

        print(training_log.last_item)

        # figure, chart = dv.PersistentFigure(id='status', size=(8, 6), chart_fns=[lambda _: dv.Chart2d(figure=_)])
        # chart.plot(training_log.training_data_cost_list, color='green')
        # figure.refresh()

    def _on_training_iteration_end(self, iteration, context):
        pass

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass

"""------------------------------------------------------------------------------------------------
"""
data_path = 'i:/Dev.Databases/mnist'

training_data_file = hdf5.File(os.path.join(data_path, 'mnist_train.hdf5'))
training_dataset = MnistDataset(data=[list(range(training_data_file['/images'].shape[0]))],
                                hparams=[training_data_file])

test_data_file = hdf5.File(os.path.join(data_path, 'mnist_test.hdf5'))
test_dataset = MnistDataset(data=[list(range(test_data_file['/images'].shape[0]))],
                            hparams=[test_data_file])

results = []
i = 1
while(i <= 20):
    model = MnistModel()
    result = model.train(training_data=training_dataset, batch_size=64,
                         test_data=test_dataset,
                         training_data_sample=training_dataset.random_select(256)[:],
                         test_data_sample=test_dataset.random_select(256)[:])
    model.close()

    results.append(result)
    print([_.iteration for _ in results], stats.series.mean([_.iteration for _ in results]))

    i += 1

test_data_file.close()
training_data_file.close()