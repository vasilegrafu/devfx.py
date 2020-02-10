import numpy as np
import tensorflow as tf
import datetime as dt
import devfx.os as os
import devfx.core as core
import devfx.statistics as stats
import devfx.databases.hdf5 as db
import devfx.machine_learning as ml
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
class MnistModel(ml.sl.Model):
    # ----------------------------------------------------------------
    @ml.build_graph(x=(ml.float32, (None, 28, 28, 1)))
    @ml.output_as_tensor((ml.float32, (None, 10)))
    @ml.input_as_tensor(x=(ml.float32, (None, 28, 28, 1)))
    def h(self, x):
        conv1 = ml.nn.conv2d(name='conv1',
                             input=x,
                             filters_n=64,
                             kernel_size=(5, 5),
                             activation_fn=lambda z: ml.nn.relu(z),
                             z_normalizer=ml.nn.gauss_normalizer())

        pool1 = ml.nn.max_pool2d(name='pool1',
                                 input=conv1)

        conv2 = ml.nn.conv2d(name='conv2',
                             input=pool1,
                             filters_n=128,
                             kernel_size=(3, 3),
                             activation_fn=lambda z: ml.nn.relu(z),
                             z_normalizer=ml.nn.gauss_normalizer())

        pool2 = ml.nn.max_pool2d(name='pool2',
                                 input=conv2)

        linear = ml.nn.linearize(pool2)

        fc1 = ml.nn.dense(name="fc1",
                          input=linear,
                          n=64,
                          activation_fn=lambda z: ml.nn.relu(z),
                          z_normalizer=ml.nn.gauss_normalizer())

        fc2 = ml.nn.dense(name="fc2",
                          input=fc1,
                          n=32,
                          activation_fn=lambda z: ml.nn.relu(z),
                          z_normalizer=ml.nn.gauss_normalizer())

        fco = ml.nn.dense(name="fco",
                          input=fc2,
                          n=10,
                          activation_fn=lambda z: ml.nn.softmax(z, axis=1))

        r = fco
        return r

    @ml.build_graph(x=(ml.float32, (None, 28, 28, 1)), y=(ml.int32, (None,)))
    @ml.output_as_tensor((ml.float32, ()))
    @ml.input_as_tensor(x=(ml.float32, (None, 28, 28, 1)), y=(ml.int32, (None,)))
    def J(self, x, y):
        hr = self.h(x)
        r = -ml.reduce_mean(ml.reduce_sum(ml.one_hot(indices=y, depth=10, on_value=1.0, off_value=0.0, axis=1)*ml.log(hr+1e-16), axis=1))
        return r

    @ml.build_graph(x=(ml.float32, (None, 28, 28, 1)))
    @ml.output_as_tensor((ml.int32, (None,)))
    @ml.input_as_tensor(x=(ml.float32, (None, 28, 28, 1)))
    def y_pred(self, x):
        hr = self.h(x)
        r = ml.argmax(hr, axis=1)
        return r

    @ml.build_graph(x=(ml.float32, (None, 28, 28, 1)), y=(ml.int32, (None,)))
    @ml.output_as_tensor((ml.float32, ()))
    @ml.input_as_tensor(x=(ml.float32, (None, 28, 28, 1)), y=(ml.int32, (None,)))
    def accuracy(self, x, y):
        y_predr = self.y_pred(x)
        r = ml.reduce_mean(ml.kronecker(y_predr, y, dtype=ml.float32))
        return r

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.register_apply_cost_optimizer_function(cost_fn=self.J, cost_optimizer=ml.AdamOptimizer(learning_rate=1e-3))
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].accuracy = self.accuracy(*context.test_data_sample)
        if(training_log[-1].accuracy > 0.90):
            context.register_apply_cost_optimizer_function(cost_fn=self.J, cost_optimizer=ml.AdamOptimizer(learning_rate=1e-4))
            context.batch_size = 64

        if(len(training_log[:].time_delta) >= 2):
            training_log[-1].time_delta_average = sum(training_log[:].time_delta, dt.timedelta(0))/(len(training_log[:].time_delta)-1)

        print(training_log[-1])

        # context.cancellation_token.request_cancellation(condition=(training_log[-1].accuracy > 0.90))

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
    training_data = [training_data_file.get_dataset('/images')[:], training_data_file.get_dataset('/labels')[:]]
    training_data = [np.reshape(training_data[0], (*training_data[0].shape, 1)), training_data[1]]

    test_data_file = db.File(os.path.join(data_path, 'mnist_test.hdf5'))
    test_data = [test_data_file.get_dataset('/images')[:], test_data_file.get_dataset('/labels')[:]]
    test_data = [np.reshape(test_data[0], (*test_data[0].shape, 1)), test_data[1]]

    model = MnistModel()
    model.train(training_data=training_data, batch_size=32,
                test_data=test_data,
                training_data_sample = stats.mseries.sample(training_data, 512),
                test_data_sample = stats.mseries.sample(test_data, 512))

    test_data_file.close()
    training_data_file.close()

    # # export-import
    # model.export_to(path=f'{os.file_info.parent_directorypath(__file__)}/exports')

    # model_executer = ml.sl.ModelExecuter.import_from(path=f'{os.file_info.parent_directorypath(__file__)}/exports')

    # accuracy = model_executer.accuracy(ml.as_tensor(test_data[0], dtype=ml.float32, shape=((None, 28, 28, 1))),
    #                                    ml.as_tensor(test_data[1], dtype=ml.int32, shape=((None,))))
    # print(accuracy)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()