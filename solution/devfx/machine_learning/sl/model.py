import types as tp
import inspect as insp
import itertools as it
import datetime as dt
import numpy as np
import tensorflow as tf
import devfx.exceptions as excs
import devfx.core as core
import devfx.diagnostics as dgn
from . import variables

class Model(tf.Module):
    @staticmethod
    def current_model():
        stack = insp.stack()
        for frameinfo in stack:
            f_locals = frameinfo.frame.f_locals
            if('self' in f_locals):
                self = f_locals['self']
                if(core.is_instance(self, Model)):
                    return self
        return None

    @staticmethod
    def is_called_by_apply_cost_optimizer():
        stack = insp.stack()
        for frameinfo in stack:
            if(frameinfo.function == '__apply_cost_optimizer'):
                return True
        return False

    """------------------------------------------------------------------------------------------------
    """
    def __init__(self):
        pass

    """------------------------------------------------------------------------------------------------
    """
    class TrainingContext(object):
        pass

    class TrainingResult(object):
        pass

    """------------------------------------------------------------------------------------------------
    """
    class TrainingCancellationToken(object):
        def __init__(self):
            self.__is_cancellation_requested = False

        def request_cancellation(self, condition=None):
            if (condition is None):
                self.__is_cancellation_requested = True
            elif (condition is not None):
                if(condition):
                    self.__is_cancellation_requested = True
            else:
                raise excs.NotSupportedError()

        def is_cancellation_requested(self):
            return (self.__is_cancellation_requested == True)

    """------------------------------------------------------------------------------------------------
    """
    class TrainingLogItem(object):
        def __init__(self, nr, time_elapsed, time_delta, iteration, epoch):
            self.__attr_list__ = []

            self.nr = int(nr)
            self.time_elapsed = time_elapsed
            self.time_delta = time_delta
            self.iteration = iteration
            self.epoch = epoch

        def __setattr__(self, name, value):
            if(name == '__attr_list__'):
                super().__setattr__(name, value)
            else:
                super().__setattr__(name, value)
                self.__attr_list__.append((name, value))

        def __str__(self):
            name_value_list = []
            for attr in self.__attr_list__:
                name = attr[0]
                value = attr[1]

                if(name == 'time_elapsed'):
                    name_value_list.append("{name}={value}".format(name=name, value=value))
                elif(name == 'time_delta'):
                    name_value_list.append("{name}={value}".format(name=name, value=value))
                elif (name == 'iteration'):
                    name_value_list.append("{name}={value}".format(name=name, value=value))
                elif (name == 'epoch'):
                    name_value_list.append("{name}={value:.3f}".format(name=name, value=value))
                elif(value is None):
                    name_value_list.append("{name}={value}".format(name=name, value=None))
                elif(core.is_typeof(value, str)):
                    name_value_list.append("{name}={value}".format(name=name, value=value))
                elif (core.is_typeof(value, int)):
                    name_value_list.append("{name}={value}".format(name=name, value=value))
                else:
                    try:
                        value = float(value)
                        name_value_list.append("{name}={value:.6f}".format(name=name, value=value))
                    except:
                        name_value_list.append("{name}={value}".format(name=name, value=value))
            return ', '.join(name_value_list)

        def __repr__(self):
            raise excs.NotSupportedError()

    """------------------------------------------------------------------------------------------------
    """
    class TrainingLog(object):
        def __init__(self):
            self.__items = []

        def append(self, item):
            self.__items.append(item)

        def remove(self, index_or_indices):
            del self.__items[index_or_indices]

        def __delitem__(self, index_or_indices):
            self.remove(index_or_indices)

        def clear(self):
            self.__items.clear()

        def get(self, index_or_indices):
            class __TrainingLogItemsProxy(object):
                def __init__(self, items):
                    self.__items = items

                def __getattr__(self, name):
                    return [getattr(_, name) for _ in self.__items]

            item_or_items = self.__items[index_or_indices]
            if(not core.is_iterable(item_or_items)):
                return item_or_items
            else:
                return __TrainingLogItemsProxy(item_or_items)

        def __getitem__(self, index_or_indices):
            return self.get(index_or_indices)

        def __len__(self):
            return len(self.__items)

    """------------------------------------------------------------------------------------------------
    """
    def train(self, training_data, batch_size=None, iterations=None, epochs=None, hparams=None, **kwargs):
        # ----------------------------------------------------------------
        if(not core.is_iterable(training_data)):
            raise excs.ArgumentError()
        if(len(training_data) != 2):
            raise excs.ArgumentError()
        if(not core.is_iterable(training_data[0])):
            raise excs.ArgumentError()
        if(not core.is_iterable(training_data[1])):
            raise excs.ArgumentError()
        if(len(training_data[0]) != len(training_data[1])):
            raise excs.ArgumentError()
        # ----------------------------------------------------------------

        # ----------------------------------------------------------------
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

        # ----------------------------------------------------------------
        stopwatch = dgn.stopwatch().start()

        cancellation_token = Model.TrainingCancellationToken()

        training_log = Model.TrainingLog()

        append_to_training_log_condition = lambda context: True

        apply_cost_optimizer = None
        def register_apply_cost_optimizer_function(self, cost_fn, cost_optimizer):
            if(cost_fn is None):
                raise excs.ArgumentError()
            if(cost_optimizer is None):
                raise excs.ArgumentError()
            def __apply_cost_optimizer(*args, **kwargs):
                with tf.GradientTape() as gradient_tape:
                    cost = cost_fn(*args, **kwargs)
                gradients = gradient_tape.gradient(cost, variables.get_trainable_variables())
                cost_optimizer.apply_gradients(zip(gradients, variables.get_trainable_variables()))
            self.apply_cost_optimizer = __apply_cost_optimizer
        # ----------------------------------------------------------------

        # ----------------------------------------------------------------
        context = Model.TrainingContext()
        context.time_elapsed = stopwatch.elapsed
        context.training_data = training_data
        context.batch_size = batch_size
        context.iterations = iterations
        context.epochs = epochs
        context.hparams = hparams
        for key in kwargs: setattr(context, key, kwargs[key])
        context.training_log = training_log
        context.cancellation_token = cancellation_token
        context.append_to_training_log_condition = append_to_training_log_condition
        context.register_apply_cost_optimizer_function = tp.MethodType(register_apply_cost_optimizer_function, context)
        context.apply_cost_optimizer = apply_cost_optimizer
        self._on_training_begin(context)
        apply_cost_optimizer = context.apply_cost_optimizer
        append_to_training_log_condition = context.append_to_training_log_condition
        batch_size = context.batch_size
        hparams = context.hparams
        # ----------------------------------------------------------------

        # ----------------------------------------------------------------
        training_data_row_indices = np.random.permutation(training_data_row_count)
        # ----------------------------------------------------------------

        iteration = 0
        epoch = 0
        while((iteration <= iterations) and (epoch < epochs) and  (not cancellation_token.is_cancellation_requested())):
            # ----------------------------------------------------------------
            training_data_row_indices_iterator = iter(training_data_row_indices)
            # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            context = Model.TrainingContext()
            context.time_elapsed = stopwatch.elapsed
            context.training_data = training_data
            context.batch_size = batch_size
            context.iteration = iteration
            context.iterations = iterations
            context.epoch = epoch
            context.epochs = epochs
            context.hparams = hparams
            for key in kwargs: setattr(context, key, kwargs[key])
            context.training_log = training_log
            context.cancellation_token = cancellation_token
            context.append_to_training_log_condition = append_to_training_log_condition
            context.register_apply_cost_optimizer_function = tp.MethodType(register_apply_cost_optimizer_function, context)
            context.apply_cost_optimizer = apply_cost_optimizer
            self._on_training_epoch_begin(epoch, context)
            apply_cost_optimizer = context.apply_cost_optimizer
            append_to_training_log_condition = context.append_to_training_log_condition
            batch_size = context.batch_size
            hparams = context.hparams
            # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            training_data_epoch_position = 0
            # ----------------------------------------------------------------
            
            # ----------------------------------------------------------------
            while ((iteration <= iterations) and (not cancellation_token.is_cancellation_requested())):
                # ----------------------------------------------------------------
                training_data_row_indices_batch = list(it.islice(training_data_row_indices_iterator, batch_size))
                if(len(training_data_row_indices_batch) == 0):
                    break

                batch = []
                training_data_batch_column0 = [training_data[0][_] if (not core.is_function(training_data[0][_])) else training_data[0][_]() for _ in training_data_row_indices_batch]
                batch.append(training_data_batch_column0)
                training_data_batch_column1 = [training_data[1][_] if (not core.is_function(training_data[1][_])) else training_data[1][_]() for _ in training_data_row_indices_batch]
                batch.append(training_data_batch_column1)

                iteration += 1

                training_data_epoch_position += len(training_data_row_indices_batch)
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                context = Model.TrainingContext()
                context.time_elapsed = stopwatch.elapsed
                context.training_data = training_data
                context.batch_size = batch_size
                context.batch = batch
                context.iteration = iteration
                context.iterations = iterations
                context.epoch = epoch
                context.epochs = epochs
                context.hparams = hparams
                for key in kwargs: setattr(context, key, kwargs[key])
                context.training_log = training_log
                context.cancellation_token = cancellation_token
                context.append_to_training_log_condition = append_to_training_log_condition
                context.register_apply_cost_optimizer_function = tp.MethodType(register_apply_cost_optimizer_function, context)
                context.apply_cost_optimizer = apply_cost_optimizer
                self._on_training_iteration_begin(iteration, context)
                apply_cost_optimizer = context.apply_cost_optimizer
                append_to_training_log_condition = context.append_to_training_log_condition
                batch_size = context.batch_size
                hparams = context.hparams
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                if (apply_cost_optimizer is not None):
                    if(hparams is None):
                        apply_cost_optimizer(batch[0], batch[1])
                    else:
                        apply_cost_optimizer(batch[0], batch[1], hparams)
                else:
                    context = Model.TrainingContext()
                    context.time_elapsed = stopwatch.elapsed
                    context.training_data = training_data
                    context.batch_size = batch_size
                    context.batch = batch
                    context.iteration = iteration
                    context.iterations = iterations
                    context.epoch = epoch
                    context.epochs = epochs
                    context.hparams = hparams
                    for key in kwargs: setattr(context, key, kwargs[key])
                    context.training_log = training_log
                    context.cancellation_token = cancellation_token
                    context.append_to_training_log_condition = append_to_training_log_condition
                    context.register_apply_cost_optimizer_function = tp.MethodType(register_apply_cost_optimizer_function, context)
                    context.apply_cost_optimizer = apply_cost_optimizer
                    self._on_training_apply_cost_optimizer(context)
                    apply_cost_optimizer = context.apply_cost_optimizer
                    append_to_training_log_condition = context.append_to_training_log_condition
                    batch_size = context.batch_size
                    hparams = context.hparams
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                context = Model.TrainingContext()
                context.time_elapsed = stopwatch.elapsed
                context.iteration = iteration
                context.epoch = epoch
                append_to_training_log_condition_result = append_to_training_log_condition(context=context)
                if(append_to_training_log_condition_result):
                    time_elapsed = stopwatch.elapsed
                    training_log_item = Model.TrainingLogItem(nr=(len(training_log) + 1),
                                                              time_elapsed=time_elapsed,
                                                              time_delta=((time_elapsed - training_log[-1].time_elapsed) if (len(training_log) >= 1) else dt.timedelta(0)),
                                                              iteration=iteration,
                                                              epoch=(epoch + training_data_epoch_position / training_data_row_count))
                    training_log.append(training_log_item)

                    context = Model.TrainingContext()
                    context.time_elapsed = stopwatch.elapsed
                    context.training_data = training_data
                    context.batch_size = batch_size
                    context.batch = batch
                    context.iteration = iteration
                    context.iterations = iterations
                    context.epoch = epoch
                    context.epochs = epochs
                    context.hparams = hparams
                    for key in kwargs: setattr(context, key, kwargs[key])
                    context.training_log = training_log
                    context.cancellation_token = cancellation_token
                    context.append_to_training_log_condition = append_to_training_log_condition
                    context.register_apply_cost_optimizer_function = tp.MethodType(register_apply_cost_optimizer_function, context)
                    context.apply_cost_optimizer = apply_cost_optimizer
                    self._on_append_to_training_log(training_log, context)
                    apply_cost_optimizer = context.apply_cost_optimizer
                    append_to_training_log_condition = context.append_to_training_log_condition
                    batch_size = context.batch_size
                    hparams = context.hparams
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                context = Model.TrainingContext()
                context.time_elapsed = stopwatch.elapsed
                context.training_data = training_data
                context.batch_size = batch_size
                context.batch = batch
                context.iteration = iteration
                context.iterations = iterations
                context.epoch = epoch
                context.epochs = epochs
                context.hparams = hparams
                for key in kwargs: setattr(context, key, kwargs[key])
                context.training_log = training_log
                context.cancellation_token = cancellation_token
                context.append_to_training_log_condition = append_to_training_log_condition
                context.register_apply_cost_optimizer_function = tp.MethodType(register_apply_cost_optimizer_function, context)
                context.apply_cost_optimizer = apply_cost_optimizer
                self._on_training_iteration_end(iteration, context)
                apply_cost_optimizer = context.apply_cost_optimizer
                append_to_training_log_condition = context.append_to_training_log_condition
                batch_size = context.batch_size
                hparams = context.hparams
                # ----------------------------------------------------------------
            # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            context = Model.TrainingContext()
            context.time_elapsed = stopwatch.elapsed
            context.training_data = training_data
            context.batch_size = batch_size
            context.iteration = iteration
            context.iterations = iterations
            context.epoch = epoch
            context.epochs = epochs
            context.hparams = hparams
            for key in kwargs: setattr(context, key, kwargs[key])
            context.training_log = training_log
            context.cancellation_token = cancellation_token
            context.append_to_training_log_condition = append_to_training_log_condition
            context.register_apply_cost_optimizer_function = tp.MethodType(register_apply_cost_optimizer_function, context)
            context.apply_cost_optimizer = apply_cost_optimizer
            self._on_training_epoch_end(epoch, context)
            apply_cost_optimizer = context.apply_cost_optimizer
            append_to_training_log_condition = context.append_to_training_log_condition
            batch_size = context.batch_size
            hparams = context.hparams
            # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            epoch += 1
            # ----------------------------------------------------------------

        # ----------------------------------------------------------------
        context = Model.TrainingContext()
        context.time_elapsed = stopwatch.elapsed
        context.training_data = training_data
        context.batch_size = batch_size
        context.iteration = iteration
        context.iterations = iterations
        context.epoch = epoch
        context.epochs = epochs
        context.hparams = hparams
        for key in kwargs: setattr(context, key, kwargs[key])
        context.training_log = training_log
        self._on_training_end(context)
        # ----------------------------------------------------------------

        stopwatch.stop()

        result = Model.TrainingResult()
        result.time_elapsed = stopwatch.elapsed
        result.training_data = training_data
        result.batch_size = batch_size
        result.iteration = iteration
        result.iterations = iterations
        result.epoch = epoch
        result.epochs = epochs
        result.hparams = hparams
        for key in kwargs: setattr(result, key, kwargs[key])
        result.training_log = training_log
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

    def export_to(self, path):
        tf.saved_model.save(obj=self, export_dir=path)

