import devfx.os as os
import devfx.databases.hdf5 as hdf5
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv
from devfx_samples.neural_networks.tensorflow.mnist.data.mnist_dataset import MnistDataset

"""------------------------------------------------------------------------------------------------
"""
class MnistModel(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        # hypothesis

        x = cg.placeholder(shape=[None, 28, 28, 1], name='x')

        w = cg.create_variable(name='w', shape=[10, 28, 28, 1], initializer=cg.random_truncated_normal_initializer(stddev=1e-3, dtype=cg.float32))
        b = cg.create_variable(name='b', shape=[10], initializer=cg.random_truncated_normal_initializer(stddev=1e-3, dtype=cg.float32))
        z = cg.tensordot(x, w, axes=([1, 2, 3], [1, 2, 3])) + b

        h = nn.activation.softmax(z, axis=1)

        y_pred = cg.cast_to_int32(cg.reshape(tensor=cg.argmax(h, axis=1), shape=[None, 1]))
        self.register_evaluator(name='output_pred', evaluatee=y_pred, feeds=[x])

        # cost function
        y = cg.placeholder(shape=[None, 1], dtype=cg.int32, name='y')
        y_one_hot = cg.one_hot(indices=y[:,0], depth=10, on_value=1, off_value=0)
        J = -cg.reduce_mean(cg.reduce_sum(cg.cast_to_float32(y_one_hot)*cg.log(h+1e-16), axis=1))

        # accuracy
        accuracy = cg.reduce_mean(cg.cast_to_float32(cg.equal(y_pred[:,0], y[:,0])))
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

    def _on_append_to_training_log(self, training_log, context):
        training_log.last_item.training_data_cost = self.run_cost_evaluator(input_data=context.training_data_sample[0], output_data=context.training_data_sample[1])
        training_log.last_item.test_data_cost = self.run_cost_evaluator(input_data=context.test_data_sample[0], output_data=context.test_data_sample[1])
        training_log.last_item.accuracy = self.run_evaluator(name='accuracy', feeds_data=[context.test_data_sample[0], context.test_data_sample[1]])

        print(training_log.last_item)

        figure, chart = dv.PersistentFigure(id='status', size=(8, 6), chart_fns=[lambda _: dv.Chart2d(figure=_)])
        chart.plot(training_log.training_data_cost_list, color='green')
        figure.refresh()

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass
    
"""------------------------------------------------------------------------------------------------
"""
def main():
    data_path = 'i:/Dev.Databases/mnist'

    training_data_file = hdf5.File(os.path.join(data_path, 'mnist_train.hdf5'))
    training_dataset = MnistDataset(data=[list(range(training_data_file['/images'].shape[0]))],
                                    hparams=[training_data_file])

    test_data_file = hdf5.File(os.path.join(data_path, 'mnist_test.hdf5'))
    test_dataset = MnistDataset(data=[list(range(test_data_file['/images'].shape[0]))],
                                hparams=[test_data_file])

    model = MnistModel()
    model.train(training_data=training_dataset, batch_size=64,
                training_data_sample=training_dataset.random_select(256)[:],
                test_data_sample=test_dataset.random_select(256)[:])
    model.close()

    test_data_file.close()
    training_data_file.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()