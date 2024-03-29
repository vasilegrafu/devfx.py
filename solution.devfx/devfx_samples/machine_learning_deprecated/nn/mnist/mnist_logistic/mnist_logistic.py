import numpy as np
import devfx.os as os
import devfx.core as core
import devfx.statistics as stats
import devfx.databases.hdf5 as db
import devfx.machine_learning_deprecated as ml
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
class MnistModel(ml.sl.Model):

    # ----------------------------------------------------------------
    # @ml.build_graph(x=(ml.float32, (None, 28, 28)))
    @ml.output_as_tensor((ml.float32, (None, 10)))
    @ml.input_as_tensor(x=(ml.float32, (None, 28, 28)))
    def h(self, x):
        w = ml.sl.create_or_get_variable(name='w', shape=(10, 28, 28), dtype=ml.float32, initializer=ml.random_truncated_normal_initializer())
        b = ml.sl.create_or_get_variable(name='b', shape=(10,), dtype=ml.float32, initializer=ml.random_truncated_normal_initializer())
        z = ml.tensordot(x, w, axes=([1, 2], [1, 2])) + b
 
        r = ml.softmax(z, axis=1)
        return r

    # @ml.build_graph(x=(ml.float32, (None, 28, 28)), y=(ml.int32, (None,)))
    @ml.output_as_tensor((ml.float32, ()))
    @ml.input_as_tensor(x=(ml.float32, (None, 28, 28)), y=(ml.int32, (None,)))
    def J(self, x, y):
        hr = self.h(x)
        r = -ml.reduce_mean(ml.reduce_sum(ml.one_hot(indices=y, depth=10, on_value=1.0, off_value=0.0, axis=1)*ml.log(hr+1e-16), axis=1))
        return r

    # @ml.build_graph(x=(ml.float32, (None, 28, 28)))
    @ml.output_as_tensor((ml.int32, (None,)))
    @ml.input_as_tensor(x=(ml.float32, (None, 28, 28)))
    def y_pred(self, x):
        hr = self.h(x)
        r = ml.argmax(hr, axis=1)
        return r

    # @ml.build_graph(x=(ml.float32, (None, 28, 28)), y=(ml.int32, (None,)))
    @ml.output_as_tensor((ml.float32, ()))
    @ml.input_as_tensor(x=(ml.float32, (None, 28, 28)), y=(ml.int32, (None,)))
    def accuracy(self, x, y):
        y_predr = self.y_pred(x)
        r = ml.reduce_mean(ml.kronecker(y_predr, y, dtype=ml.float32))
        return r

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.register_apply_cost_optimizer_function(cost_fn=self.J, cost_optimizer=ml.AdamOptimizer(learning_rate=1e-6))
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log[-1].training_data_cost = self.J(*context.training_data_sample)
        if(len(training_log) >= 2):
            training_log[-1].training_data_cost_trend = stats.regression.normalized_trend(x=training_log[:].nr, y=training_log[:].training_data_cost, n_max=32)[0][1]
            context.cancellation_token.request_cancellation(condition=(abs(training_log[-1].training_data_cost_trend) <= 1e-1))
        training_log[-1].test_data_cost = self.J(*context.test_data_sample)
        
        training_log[-1].accuracy = self.accuracy(*context.test_data_sample)

        print(training_log[-1])

        figure = core.ObjectStorage.intercept(self, 'figure', lambda: dv.Figure(size=(8, 6)))
        chart = core.ObjectStorage.intercept(self, 'chart', lambda: dv.Chart2d(figure=figure))
        figure.clear_charts()
        chart.plot(training_log[:].training_data_cost, color='green')
        chart.plot(training_log[:].test_data_cost, color='red')
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
    training_data = [training_data_file.get_dataset('/images')[:], training_data_file.get_dataset('/labels')[:]]

    test_data_file = db.File(os.path.join(data_path, 'mnist_test.hdf5'))
    test_data = [test_data_file.get_dataset('/images')[:], test_data_file.get_dataset('/labels')[:]]

    model = MnistModel()
    model.train(training_data=training_data, batch_size=64,
                test_data=test_data,
                training_data_sample = stats.mseries.sample(training_data, 512),
                test_data_sample = stats.mseries.sample(test_data, 512))

    test_data_file.close()
    training_data_file.close()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()