import itertools as it
import numpy as np
import tensorflow as tf
import devfx.exceptions as exceps
import devfx.reflection as refl
import devfx.diagnostics as dgn
from ... import variables
from ... import train
from ..training_log import TrainingLog

class DeclarativeModel(object):
    def __init__(self, target='', config=None):
        self.__graph = tf.Graph()

        self.__evaluators = {}

        with self.__graph.as_default():
            self._build_model()

        self.__session = tf.Session(target=target, graph=self.__graph, config=config)

        with self.__graph.as_default():
            self.register_initializer_evaluator()

        with self.__graph.as_default():
            self.run_initializer_evaluator()

        self.__training_log = TrainingLog()

    def close(self):
        self.__training_log = None

        self.__session.close()
        self.__session = None

        self.__evaluators = None

        self.__graph = None

    """------------------------------------------------------------------------------------------------
    """
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    """------------------------------------------------------------------------------------------------
    """
    @property
    def graph(self):
        return self.__graph

    @property
    def session(self):
        return self.__session

    @property
    def evaluators(self):
        return self.__evaluators

    """------------------------------------------------------------------------------------------------
    """
    def _build_model(self):
        raise exceps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def register_evaluator(self, name, evaluatee, feeds=(), hparams=()):
        if ((len(feeds) == 0) and (len(hparams) == 0)):
            self.__evaluators[name] = lambda: self.__session.run(evaluatee, feed_dict={})
        elif ((len(feeds) == 0) and (len(hparams) >= 1)):
            self.__evaluators[name] = lambda hparams_values: self.__session.run(evaluatee, feed_dict={hparam: hparams_value for (hparam, hparams_value) in zip(hparams, hparams_values)})
        elif ((len(feeds) >= 1) and (len(hparams) == 0)):
            self.__evaluators[name] = lambda feeds_data: self.__session.run(evaluatee, feed_dict={feed: feeds_data[i] for (i, feed) in enumerate(feeds)})
        elif ((len(feeds) >= 1) and (len(hparams) >= 1)):
            self.__evaluators[name] = lambda feeds_data, hparams_values: self.__session.run(evaluatee, feed_dict={**{feed: feeds_data[i] for (i, feed) in enumerate(feeds)}, **{hparam: hparams_value for (hparam, hparams_value) in zip(hparams, hparams_values)}})
        else:
            raise exceps.NotSupportedError()

    def get_evaluator(self, name):
        return self.__evaluators[name]

    def unregister_evaluator(self, name):
        del self.__evaluators[name]

    def exists_evaluator(self, name):
        return name in self.__evaluators

    def run_evaluator(self, name, feeds_data=None, hparams_values=()):
        with self.__graph.as_default():
            if((feeds_data is None) and (len(hparams_values) == 0)):
                result = self.__evaluators[name]()
            elif((feeds_data is None) and (len(hparams_values) >= 1)):
                result = self.__evaluators[name](hparams_values=hparams_values)
            elif((feeds_data is not None) and (len(hparams_values) == 0)):
                result = self.__evaluators[name](feeds_data=feeds_data)
            elif((feeds_data is not None) and (len(hparams_values) >= 1)):
                result = self.__evaluators[name](feeds_data=feeds_data, hparams_values=hparams_values)
            else:
                raise exceps.NotSupportedError()
            return result

    """------------------------------------------------------------------------------------------------
    """
    def register_initializer_evaluator(self):
        self.register_evaluator(name='__initializer', evaluatee=variables.global_variables_initializer())

    def get_initializer_evaluator(self):
        return self.get_evaluator(name='__initializer')

    def exists_initializer_evaluator(self):
        return self.exists_evaluator(name='__initializer')

    def run_initializer_evaluator(self):
        return self.run_evaluator(name='__initializer')

    """------------------------------------------------------------------------------------------------
    """
    def register_input_evaluator(self, input, hparams=()):
        self.register_evaluator(name='__input', evaluatee=input, hparams=hparams)

    def get_input_evaluator(self):
        return self.get_evaluator(name='__input')

    def exists_input_evaluator(self):
        return self.exists_evaluator(name='__input')

    def run_input_evaluator(self, input_data, hparams_values=()):
        return self.run_evaluator(name='__input', feeds_data=[input_data], hparams_values=hparams_values)


    def register_output_evaluator(self, output, hparams=()):
        self.register_evaluator(name='__output', evaluatee=output, hparams=hparams)

    def get_output_evaluator(self):
        return self.get_evaluator(name='__output')

    def exists_output_evaluator(self):
        return self.exists_evaluator(name='__output')

    def run_output_evaluator(self, output_data, hparams_values=()):
        return self.run_evaluator(name='__output', feeds_data=[output_data], hparams_values=hparams_values)


    def register_hypothesis_evaluator(self, hypothesis, input, hparams=()):
        self.register_evaluator(name='__hypothesis', evaluatee=hypothesis, feeds=[input], hparams=hparams)

    def get_hypothesis_evaluator(self):
        return self.get_evaluator(name='__hypothesis')

    def exists_hypothesis_evaluator(self):
        return self.exists_evaluator(name='__hypothesis')

    def run_hypothesis_evaluator(self, input_data, hparams_values=()):
        return self.run_evaluator(name='__hypothesis', feeds_data=[input_data], hparams_values=hparams_values)


    def register_cost_evaluator(self, cost, input, output, hparams=()):
        self.register_evaluator(name='__cost', evaluatee=cost, feeds=[input, output], hparams=hparams)

    def get_cost_evaluator(self):
        return self.get_evaluator(name='__cost')

    def exists_cost_evaluator(self):
        return self.exists_evaluator(name='__cost')

    def run_cost_evaluator(self, input_data, output_data, hparams_values=()):
        return self.run_evaluator(name='__cost', feeds_data=[input_data, output_data], hparams_values=hparams_values)

    """------------------------------------------------------------------------------------------------
    """
    def register_cost_optimizer_applier_evaluator(self, cost, input, output, hparams=(), optimizer=None, grad_clipping_values=None):
        if(optimizer is None):
            raise exceps.ArgumentError()
        cost_optimizer_applier = train.construct_optimizer_applier(optimizer=optimizer, fn=cost, grad_clipping_values=grad_clipping_values)
        self.register_evaluator(name='__cost_optimizer_applier', evaluatee=cost_optimizer_applier, feeds=[input, output], hparams=hparams)


    def get_cost_optimizer_applier_evaluator(self):
        return self.get_evaluator(name='__cost_optimizer_applier')

    def exists_cost_optimizer_applier_evaluator(self):
        return self.exists_evaluator(name='__cost_optimizer_applier')

    def run_cost_optimizer_applier_evaluator(self, input_data, output_data, hparams_values=()):
        return self.run_evaluator(name='__cost_optimizer_applier', feeds_data=[input_data, output_data], hparams_values=hparams_values)

    """------------------------------------------------------------------------------------------------
    """
    class CancellationToken(object):
        def __init__(self):
            self.__is_cancellation_requested = False

        def request_cancellation(self, condition=None, condition_fn=None):
            if (condition is None and condition_fn is None):
                self.__is_cancellation_requested = True
            elif (condition is not None and condition_fn is None):
                if(condition):
                    self.__is_cancellation_requested = True
            elif (condition is None and condition_fn is not None):
                if(condition_fn()):
                    self.__is_cancellation_requested = True
            elif (condition is not None and condition_fn is not None):
                raise exceps.ArgumentError()
            else:
                raise exceps.NotSupportedError()

        def is_cancellation_requested(self):
            return (self.__is_cancellation_requested == True)

    """------------------------------------------------------------------------------------------------
    """
    class TrainingContext(object):
        pass

    class TrainingResult(object):
        pass

    """------------------------------------------------------------------------------------------------
    """
    def train(self, hparams_values=(), training_data=None, batch_size=None, iterations=None, epochs=None, **kwargs):
        # ----------------------------------------------------------------
        if(not refl.is_iterable(training_data)):
            raise exceps.ArgumentError()
        if(len(training_data) != 2):
            raise exceps.ArgumentError()
        if(not refl.is_iterable(training_data[0])):
            raise exceps.ArgumentError()
        if(not refl.is_iterable(training_data[1])):
            raise exceps.ArgumentError()
        if(len(training_data[0]) != len(training_data[1])):
            raise exceps.ArgumentError()
        # ----------------------------------------------------------------

        # ----------------------------------------------------------------
        training_data_column_count = len(training_data)
        training_data_row_count = len(training_data[0])
        # ----------------------------------------------------------------

        # ----------------------------------------------------------------
        if(batch_size is None):
            batch_size = training_data_row_count
        if(iterations is None):
            iterations = 1024**4
        if (epochs is None):
            epochs = 1024**4
        # ----------------------------------------------------------------

        with self.graph.as_default():
            # ----------------------------------------------------------------
            stopwatch = dgn.stopwatch().start()

            cancellation_token = DeclarativeModel.CancellationToken()

            append_to_training_log_condition = lambda context: True
            # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            context = DeclarativeModel.TrainingContext()
            context.time_elapsed = stopwatch.elapsed
            context.iterations = iterations
            context.epochs = epochs
            context.hparams_values = hparams_values
            context.training_data = training_data
            context.batch_size = batch_size
            for key in kwargs: setattr(context, key, kwargs[key])
            context.training_log = self.__training_log
            context.cancellation_token = cancellation_token
            context.append_to_training_log_condition = append_to_training_log_condition
            self._on_training_begin(context)
            append_to_training_log_condition = context.append_to_training_log_condition
            batch_size = context.batch_size
            hparams_values = context.hparams_values
            iterations = context.iterations
            epochs = context.epochs
            # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            training_data_row_indexes = np.random.choice(np.arange(0, training_data_row_count), size=training_data_row_count, replace=False)
            # ----------------------------------------------------------------

            iteration = 0
            epoch = 0
            while((iteration < iterations) and (epoch < epochs) and  (not cancellation_token.is_cancellation_requested())):
                # ----------------------------------------------------------------
                training_data_row_indexes_iterator = iter(training_data_row_indexes)
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                context = DeclarativeModel.TrainingContext()
                context.time_elapsed = stopwatch.elapsed
                context.iteration = iteration
                context.iterations = iterations
                context.epoch = epoch
                context.epochs = epochs
                context.hparams_values = hparams_values
                context.training_data = training_data
                context.batch_size = batch_size
                for key in kwargs: setattr(context, key, kwargs[key])
                context.training_log = self.__training_log
                context.cancellation_token = cancellation_token
                self._on_training_epoch_begin(epoch, context)
                batch_size = context.batch_size
                hparams_values = context.hparams_values
                epochs = context.epochs
                epoch = context.epoch
                iterations = context.iterations
                iteration = context.iteration
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                training_data_epoch_position = 0
                # ----------------------------------------------------------------
                
                # ----------------------------------------------------------------
                while ((iteration < iterations) and (not cancellation_token.is_cancellation_requested())):
                    # ----------------------------------------------------------------
                    training_data_row_indexes_batch = list(it.islice(training_data_row_indexes_iterator, batch_size))
                    if(len(training_data_row_indexes_batch) == 0):
                        break

                    batch = []
                    for training_data_column_index in range(0, training_data_column_count):
                        training_data_batch_column = [training_data[training_data_column_index][training_data_row_index] for training_data_row_index in training_data_row_indexes_batch]
                        batch.append(training_data_batch_column)

                    iteration += 1

                    training_data_epoch_position += len(training_data_row_indexes_batch)
                    # ----------------------------------------------------------------

                    # ----------------------------------------------------------------
                    context = DeclarativeModel.TrainingContext()
                    context.time_elapsed = stopwatch.elapsed
                    context.iteration = iteration
                    context.iterations = iterations
                    context.epoch = epoch
                    context.epochs = epochs
                    context.hparams_values = hparams_values
                    context.training_data = training_data
                    context.batch_size = batch_size
                    context.batch = batch
                    for key in kwargs: setattr(context, key, kwargs[key])
                    context.training_log = self.__training_log
                    context.cancellation_token = cancellation_token
                    self._on_training_iteration_begin(iteration, context)
                    batch_size = context.batch_size
                    hparams_values = context.hparams_values
                    epochs = context.epochs
                    epoch = context.epoch
                    iterations = context.iterations
                    iteration = context.iteration
                    # ----------------------------------------------------------------

                    # ----------------------------------------------------------------
                    if(self.exists_cost_optimizer_applier_evaluator()):
                        self.run_cost_optimizer_applier_evaluator(input_data=batch[0], output_data=batch[1], hparams_values=hparams_values)
                    else:
                        context = DeclarativeModel.TrainingContext()
                        context.time_elapsed = stopwatch.elapsed
                        context.iteration = iteration
                        context.iterations = iterations
                        context.epoch = epoch
                        context.epochs = epochs
                        context.hparams_values = hparams_values
                        context.training_data = training_data
                        context.batch_size = batch_size
                        context.batch = batch
                        for key in kwargs: setattr(context, key, kwargs[key])
                        context.training_log = self.__training_log
                        context.cancellation_token = cancellation_token
                        self._on_training_apply_cost_optimizer(context)
                        batch_size = context.batch_size
                        hparams_values = context.hparams_values
                        epochs = context.epochs
                        epoch = context.epoch
                        iterations = context.iterations
                        iteration = context.iteration
                    # ----------------------------------------------------------------

                    # ----------------------------------------------------------------
                    context = DeclarativeModel.TrainingContext()
                    context.time_elapsed = stopwatch.elapsed
                    context.iteration = iteration
                    context.epoch = epoch
                    append_to_training_log_condition_result = append_to_training_log_condition(context=context)
                    # ----------------------------------------------------------------
                    if(append_to_training_log_condition_result):
                        self.__training_log.append_item(time_elapsed=stopwatch.elapsed, iteration=iteration, epoch=epoch+training_data_epoch_position/training_data_row_count)
                        # ----------------------------------------------------------------
                        context = DeclarativeModel.TrainingContext()
                        context.time_elapsed = stopwatch.elapsed
                        context.iteration = iteration
                        context.iterations = iterations
                        context.epoch = epoch
                        context.epochs = epochs
                        context.hparams_values = hparams_values
                        context.training_data = training_data
                        context.batch_size = batch_size
                        context.batch = batch
                        for key in kwargs: setattr(context, key, kwargs[key])
                        context.training_log = self.__training_log
                        context.cancellation_token = cancellation_token
                        self._on_append_to_training_log(self.__training_log, context)
                        batch_size = context.batch_size
                        hparams_values = context.hparams_values
                        epochs = context.epochs
                        epoch = context.epoch
                        iterations = context.iterations
                        iteration = context.iteration
                        # ----------------------------------------------------------------

                    # ----------------------------------------------------------------
                    context = DeclarativeModel.TrainingContext()
                    context.time_elapsed = stopwatch.elapsed
                    context.iteration = iteration
                    context.iterations = iterations
                    context.epoch = epoch
                    context.epochs = epochs
                    context.hparams_values = hparams_values
                    context.training_data = training_data
                    context.batch_size = batch_size
                    context.batch = batch
                    for key in kwargs: setattr(context, key, kwargs[key])
                    context.training_log = self.__training_log
                    context.cancellation_token = cancellation_token
                    self._on_training_iteration_end(iteration, context)
                    batch_size = context.batch_size
                    hparams_values = context.hparams_values
                    epochs = context.epochs
                    epoch = context.epoch
                    iterations = context.iterations
                    iteration = context.iteration
                    # ----------------------------------------------------------------
                 # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                context = DeclarativeModel.TrainingContext()
                context.time_elapsed = stopwatch.elapsed
                context.iteration = iteration
                context.iterations = iterations
                context.epoch = epoch
                context.epochs = epochs
                context.hparams_values = hparams_values
                context.training_data = training_data
                context.batch_size = batch_size
                for key in kwargs: setattr(context, key, kwargs[key])
                context.training_log = self.__training_log
                context.cancellation_token = cancellation_token
                self._on_training_epoch_end(epoch, context)
                batch_size = context.batch_size
                hparams_values = context.hparams_values
                epochs = context.epochs
                epoch = context.epoch
                iterations = context.iterations
                iteration = context.iteration
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                epoch += 1
                # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            context = DeclarativeModel.TrainingContext()
            context.time_elapsed = stopwatch.elapsed
            context.iteration = iteration
            context.iterations = iterations
            context.epoch = epoch
            context.epochs = epochs
            context.hparams_values = hparams_values
            context.training_data = training_data
            context.batch_size = batch_size
            for key in kwargs: setattr(context, key, kwargs[key])
            context.training_log = self.__training_log
            self._on_training_end(context)
            # ----------------------------------------------------------------

            stopwatch.stop()

        result = DeclarativeModel.TrainingResult()
        result.time_elapsed = stopwatch.elapsed
        result.iteration = iteration
        result.iterations = iterations
        result.epoch = epoch
        result.epochs = epochs
        result.hparams_values = hparams_values
        result.training_data = training_data
        result.batch_size = batch_size
        for key in kwargs: setattr(result, key, kwargs[key])
        result.training_log = self.__training_log
        return result

    """
    """
    def _on_training_begin(self, context):
        pass

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_training_iteration_begin(self, iteration, context):
        pass

    def _on_training_apply_cost_optimizer(self, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        pass

    def _on_training_iteration_end(self, iteration, context):
        pass

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass

    """------------------------------------------------------------------------------------------------
    """
    def export_meta_data_to(self, path):
        with self.__graph.as_default():
            tf.train.export_meta_graph(filename=path+'.graph', as_text=True)

    def import_meta_data_from(self, path):
        with self.__graph.as_default():
            tf.train.import_meta_graph(meta_graph_or_file=path+'.graph')

    #
    def export_variables_data_to(self, path):
        with self.__graph.as_default():
            tf.train.Saver(max_to_keep=1).save(sess=self.__session, save_path=path+'.variables', write_meta_graph=False, write_state=False)

    def import_variables_data_from(self, path):
        with self.__graph.as_default():
            tf.train.Saver(max_to_keep=1).restore(sess=self.__session, save_path=path+'.variables')

    #
    def export_to(self, path):
        self.export_meta_data_to(path=path)
        self.export_variables_data_to(path=path)

    def import_from(self, path):
        self.import_meta_data_from(path=path)
        self.import_variables_data_from(path=path)


