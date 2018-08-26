import numpy as np
import devfx.os as os
import devfx.databases.hdf5 as hdf5
import devfx.data_containers as dc
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv
from devfx_howto.neural_networks.tensorflow.mnist.data.mnist_dataset import MnistDataset

"""------------------------------------------------------------------------------------------------
"""
class MnistModelTrainer(cg.models.DeclarativeModelTrainer):
    # ----------------------------------------------------------------
    def _build_model(self):
        # hparams
        is_training = cg.placeholder(shape=[], name='is_training')

        # hypothesis
        x = cg.placeholder(shape=[None, 28, 28, 1], name='x')

        fc1 = nn.layers.fully_connected(name='fc1',
                                        input=x,
                                        n=256,
                                        normalizer=nn.normalization.batch_normalizer(is_training=is_training),
                                        activation_fn=lambda z: nn.activation.relu(z))
        fc2 = nn.layers.fully_connected(name='fc2',
                                        input=fc1,
                                        n=192,
                                        normalizer=nn.normalization.batch_normalizer(is_training=is_training),
                                        activation_fn=lambda z: nn.activation.relu(z))
        fc3 = nn.layers.fully_connected(name='fc3',
                                        input=fc2,
                                        n=128,
                                        normalizer=nn.normalization.batch_normalizer(is_training=is_training),
                                        activation_fn=lambda z: nn.activation.relu(z))
        fc4 = nn.layers.fully_connected(name='fc4',
                                        input=fc3,
                                        n=64,
                                        normalizer=nn.normalization.batch_normalizer(is_training=is_training),
                                        activation_fn=lambda z: nn.activation.relu(z))
        fco = nn.layers.fully_connected(name='fco',
                                        input=fc4,
                                        n=10,
                                        activation_fn=lambda z: nn.activation.softmax(z, axis=1))

        h = fco
        y_pred = cg.cast_to_int32(cg.reshape(tensor=cg.argmax(h, axis=1), shape=[None, 1]))
        self.construct_evaluatee_evaluator(name='output_pred', evaluatee=y_pred, feeds=[x], hparams=[is_training])

        # cost function
        y = cg.placeholder(shape=[None, 1], dtype=cg.int32, name='y')
        y_one_hot = cg.one_hot(indices=y[:, 0], depth=10, on_value=1, off_value=0)
        J = -cg.reduce_mean(cg.reduce_sum(cg.cast(y_one_hot, h.dtype)*cg.log(h + 1e-16), axis=1))

        # accuracy
        accuracy = cg.reduce_mean(cg.cast_to_float32(cg.equal(y_pred[:, 0], y[:, 0])))
        self.construct_evaluatee_evaluator(name='accuracy', evaluatee=accuracy, feeds=[x, y], hparams=[is_training])

        # learning rate
        initial_learning_rate = cg.constant(value=1e-2)
        learning_rate = cg.create_variable('learning_rate', initializer=initial_learning_rate, trainable=False)

        self.construct_evaluatee_evaluator(name='initial_learning_rate', evaluatee=initial_learning_rate)
        self.construct_evaluatee_evaluator(name='learning_rate', evaluatee=learning_rate)

        update_learning_rate_input = cg.placeholder(shape=[], name='update_learning_rate_input')
        update_learning_rate = learning_rate.assign(update_learning_rate_input)
        self.construct_evaluatee_evaluator(name='update_learning_rate', evaluatee=update_learning_rate, feeds=[update_learning_rate_input])

        # evaluators
        self.construct_input_evaluator(input=input, hparams=[is_training])
        self.construct_output_evaluator(output=y, hparams=[is_training])
        self.construct_hypothesis_evaluator(hypothesis=h, input=x, hparams=[is_training])
        self.construct_cost_evaluator(cost=J, input=x, output=y, hparams=[is_training])

        # cost minimizer
        self.construct_cost_optimizer_applier_evaluator(cost=J, input=x, output=y, hparams=[is_training], optimizer=cg.train.AdamOptimizer(learning_rate=learning_rate))

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        context.append_to_training_log_condition = lambda context: context.iteration % 20 == 0

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        # training_log.last_item.cost_on_training_data = self.run_cost_evaluator(*context.training_data.random_select(1024*4), hparams_values=[False])
        # if(len(training_log.nr_list) >= 2):
        #     training_log.last_item.trend_of_cost_on_training_data = stats.normalized_trend(x=training_log.nr_list, y=training_log.cost_on_training_data_list, n_max=64)[0]*360/(2.0*np.pi)
        # training_log.last_item.cost_on_test_data = self.run_cost_evaluator(*context.test_data.random_select(1024*4), hparams_values=[False])

        training_log.last_item.accuracy = self.run_evaluator(name='accuracy', feeds_data=[*context.test_data.random_select(1024*4)], hparams_values=[False])
        training_log.last_item.initial_learning_rate = self.run_evaluator(name='initial_learning_rate')
        training_log.last_item.learning_rate = self.run_evaluator(name='learning_rate')
        if(training_log.last_item.accuracy < 0.95):
            self.run_evaluator(name='update_learning_rate', feeds_data=[training_log.last_item.initial_learning_rate])
        elif(training_log.last_item.accuracy < 0.98):
            self.run_evaluator(name='update_learning_rate', feeds_data=[training_log.last_item.initial_learning_rate*(1.0/2.0)**((training_log.last_item.accuracy-0.95)*100)])
        else:
            context.cancellation_token.request_cancellation()

        print(training_log.last_item)

        # figure, chart = dv.PersistentFigure(id='status', size=(8, 6), chart_fns=[lambda _: dv.Chart2d(figure=_)])
        # chart.plot(training_log.cost_on_training_data_list, color='red')
        # chart.plot(training_log.cost_on_test_data_list, color='green')
        # figure.refresh()

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
    model_trainer = MnistModelTrainer()
    result = model_trainer.train(hparams_values=[True],
                                 training_data=dc.Dataset(training_dataset[:]), batch_size=64,
                                 test_data=dc.Dataset(test_dataset[:]))
    model_trainer.close()

    results.append(result)
    print([_.iteration for _ in results], stats.avg([_.iteration for _ in results]))

    i += 1

test_data_file.close()
training_data_file.close()