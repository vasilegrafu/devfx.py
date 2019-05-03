# import os as os2
import devfx.os as os
import tensorflow as tf
import devfx.databases.hdf5 as hdf5
import devfx.data_containers as dc
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv
from devfx_samples.neural_networks.tensorflow.mnist.data.mnist_dataset import MnistDataset

"""------------------------------------------------------------------------------------------------
"""
class MnistModel(cg.models.DeclarativeModel):
    # def __init__(self):
    #     # os2.environ["OMP_NUM_THREADS"] = "16"
    #     # os2.environ["KMP_BLOCKTIME"] = "30"
    #     # os2.environ["KMP_SETTINGS"] = "1"
    #     # os2.environ["KMP_AFFINITY"]= "granularity=fine,verbose,compact,1,0"

    #     config = tf.ConfigProto(intra_op_parallelism_threads=16,
    #                             inter_op_parallelism_threads=16,  
    #                             allow_soft_placement=True, 
    #                             device_count={"CPU": 8})
    #     super().__init__(config=config)

    # ----------------------------------------------------------------
    def _build_model(self):
        # hparams
        is_training = cg.placeholder(shape=[], name='is_training')

        # hypothesis
        x = cg.placeholder(shape=[None, 28, 28, 1], name='x')

        conv1 = nn.layers.conv2d(name='conv1',
                                 input=x,
                                 filters=64,
                                 kernel_size=(4, 4),
                                 activation_fn=lambda z: nn.activation.relu(z))
        print(conv1.shape)
        pool1 = nn.layers.max_pooling2d(name='pool1',
                                        input=conv1)
        print(pool1.shape)

        conv2 = nn.layers.conv2d(name='conv2',
                                 input=pool1,
                                 filters=128,
                                 kernel_size=(4, 4),
                                 activation_fn=lambda z: nn.activation.relu(z))
        pool2 = nn.layers.max_pooling2d(name='pool2',
                                        input=conv2)
        linear = nn.layers.linearize(pool2)

        fc1 = nn.layers.fully_connected(name='fc1',
                                        input=linear,
                                        n=64,
                                        normalizer=nn.normalization.batch_normalizer(is_training=is_training),
                                        activation_fn=lambda z: nn.activation.relu(z))

        fc2 = nn.layers.fully_connected(name='fc2',
                                        input=fc1,
                                        n=32,
                                        normalizer=nn.normalization.batch_normalizer(is_training=is_training),
                                        activation_fn=lambda z: nn.activation.relu(z))

        fco = nn.layers.fully_connected(name='fco',
                                        input=fc2,
                                        n=10,
                                        activation_fn=lambda z: nn.activation.softmax(z, axis=1))

        h = fco
        y_pred = cg.cast_to_int32(cg.reshape(tensor=cg.argmax(h, axis=1), shape=[None, 1]))
        self.register_evaluator(name='output_pred', evaluatee=y_pred, feeds=[x], hparams=[is_training])

        # cost function
        y = cg.placeholder(shape=[None, 1], dtype=cg.int32, name='y')
        y_one_hot = cg.one_hot(indices=y[:, 0], depth=10, on_value=1, off_value=0)
        J = -cg.reduce_mean(cg.reduce_sum(cg.cast(y_one_hot, h.dtype)*cg.log(h + 1e-16), axis=1))

        # accuracy
        accuracy = cg.reduce_mean(cg.cast_to_float32(cg.equal(y_pred[:, 0], y[:, 0])))
        self.register_evaluator(name='accuracy', evaluatee=accuracy, feeds=[x, y], hparams=[is_training])

        # learning rate
        initial_learning_rate = cg.constant(value=1e-2)
        learning_rate = cg.create_variable('learning_rate', initializer=initial_learning_rate, trainable=False)

        self.register_evaluator(name='initial_learning_rate', evaluatee=initial_learning_rate)
        self.register_evaluator(name='learning_rate', evaluatee=learning_rate)

        update_learning_rate_input = cg.placeholder(shape=[], name='update_learning_rate_input')
        update_learning_rate = learning_rate.assign(update_learning_rate_input)
        self.register_evaluator(name='update_learning_rate', evaluatee=update_learning_rate, feeds=[update_learning_rate_input])

        # evaluators
        self.register_input_evaluator(input=input, hparams=[is_training])
        self.register_output_evaluator(output=y, hparams=[is_training])
        self.register_hypothesis_evaluator(hypothesis=h, input=x, hparams=[is_training])
        self.register_cost_evaluator(cost=J, input=x, output=y, hparams=[is_training])

        # cost minimizer
        self.register_cost_optimizer_applier_evaluator(cost=J, input=x, output=y, hparams=[is_training], optimizer=cg.train.AdamOptimizer(learning_rate=learning_rate))


    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 10 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        training_log.last_item.accuracy = self.run_evaluator(name='accuracy', feeds_data=[*context.test_data.random_select(1024)], hparams_values=[False])
        training_log.last_item.initial_learning_rate = self.run_evaluator(name='initial_learning_rate')
        training_log.last_item.learning_rate = self.run_evaluator(name='learning_rate')
        if(training_log.last_item.accuracy < 0.95):
            self.run_evaluator(name='update_learning_rate', feeds_data=[training_log.last_item.initial_learning_rate])
        elif(training_log.last_item.accuracy < 0.99):
            self.run_evaluator(name='update_learning_rate', feeds_data=[training_log.last_item.initial_learning_rate*(1.0/2.0)**((training_log.last_item.accuracy-0.95)*100)])
        else:
            context.cancellation_token.request_cancellation()

        print(training_log.last_item)

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
test_dataset = MnistDataset(data=[list(range(test_data_file['/images'].shape[0]))], hparams=[test_data_file])

results = []
i = 1
while(i <= 20):
    model = MnistModel()
    result = model.train(hparams_values=[True],
                         training_data=dc.Dataset(training_dataset[:]), batch_size=64,
                         test_data=dc.Dataset(test_dataset[:]))
    model.close()

    results.append(result)
    print([_.iteration for _ in results], stats.mean([_.iteration for _ in results]))

    i += 1

test_data_file.close()
training_data_file.close()
