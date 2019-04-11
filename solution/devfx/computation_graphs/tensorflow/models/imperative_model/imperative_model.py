import tensorflow as tf
import devfx.exceptions as exceptions
import devfx.reflection as refl
import devfx.diagnostics as dgn
import devfx.data_containers as dc
from ..training_log import TrainingLog

class ImperativeModel(object):
    def __init__(self):
        self.__functions = {}

        self._build_model()

        self.__training_log = TrainingLog()

    def close(self):
        self.__training_log = None

    """------------------------------------------------------------------------------------------------
    """
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    """------------------------------------------------------------------------------------------------
    """
    @property
    def functions(self):
        return self.__functions

    """------------------------------------------------------------------------------------------------
    """
    def _build_model(self):
        raise exceptions.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def register_function(self, name, fn):
        self.__functions[name] = fn

    def get_function(self, name):
        return self.__functions[name]

    def unregister_function(self, name):
        del self.__functions[name]

    def exists_function(self, name):
        return name in self.__functions

    def run_function(self, name, *args, **kwargs):
        result = self.__functions[name](*args, **kwargs)
        return result

    """------------------------------------------------------------------------------------------------
    """
    def register_hypothesis_function(self, fn):
        self.register_function('__hypothesis', fn=fn)

    def get_hypothesis_function(self):
        return self.get_function('__hypothesis')

    def exists_hypothesis_function(self):
        return self.exists_function('__hypothesis')

    def run_hypothesis_function(self, *args, **kwargs):
        return self.run_function('__hypothesis', *args, **kwargs)

    # ----------------------------------------------------------------

    def register_cost_function(self, fn):
        self.register_function('__cost', fn=fn)

    def get_cost_function(self):
        return self.get_function('__cost')

    def exists_cost_function(self):
        return self.exists_function('__cost')

    def run_cost_function(self, *args, **kwargs):
        return self.run_function('__cost', *args, **kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def register_apply_cost_optimizer_function(self, optimizer=None):
        if(optimizer is None):
            raise exceptions.ArgumentError()
        def __apply_cost_optimizer(*args, **kwargs):
            grads_and_vars = tf.contrib.eager.implicit_gradients(self.get_cost_function())(*args, **kwargs)
            optimizer.apply_gradients(grads_and_vars)
        self.register_function('__apply_cost_optimizer', fn=__apply_cost_optimizer)

    def get_apply_cost_optimizer_function(self):
        return self.get_function('__apply_cost_optimizer')

    def exists_apply_cost_optimizer_function(self):
        return self.exists_function('__apply_cost_optimizer')

    def run_apply_cost_optimizer_function(self, *args, **kwargs):
        return self.run_function('__apply_cost_optimizer', *args, **kwargs)

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
                raise exceptions.ArgumentError()
            else:
                raise exceptions.NotSupportedError()

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
    def train(self, hparams=None, training_data=None, batch_size=None, iterations=None, epochs=None, **kwargs):
        # ----------------------------------------------------------------
        if(not refl.is_typeof(training_data, dc.Dataset)):
            training_data = dc.Dataset(training_data)
        if(batch_size is None):
            batch_size = len(training_data)
        if(iterations is None):
            iterations = 1024**4
        if (epochs is None):
            epochs = 1024**4
        # ----------------------------------------------------------------

        # ----------------------------------------------------------------
        stopwatch = dgn.stopwatch().start()

        cancellation_token = ImperativeModel.CancellationToken()

        append_to_training_log_condition = lambda context: True
        # ----------------------------------------------------------------

        # ----------------------------------------------------------------
        context = ImperativeModel.TrainingContext()
        context.time_elapsed = stopwatch.elapsed
        context.iterations = iterations
        context.epochs = epochs
        context.hparams = hparams
        context.training_data = training_data
        context.batch_size = batch_size
        for key in kwargs: setattr(context, key, kwargs[key])
        context.training_log = self.__training_log
        context.cancellation_token = cancellation_token
        context.append_to_training_log_condition = append_to_training_log_condition
        self._on_training_begin(context)
        append_to_training_log_condition = context.append_to_training_log_condition
        batch_size = context.batch_size
        hparams = context.hparams
        iterations = context.iterations
        epochs = context.epochs
        # ----------------------------------------------------------------

        iteration = 0
        epoch = 0
        while((iteration < iterations) and (epoch < epochs) and  (not cancellation_token.is_cancellation_requested())):
            # ----------------------------------------------------------------
            training_data = training_data.shuffle()
            training_data_iterator = training_data.iterator()
            # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            context = ImperativeModel.TrainingContext()
            context.time_elapsed = stopwatch.elapsed
            context.iteration = iteration
            context.iterations = iterations
            context.epoch = epoch
            context.epochs = epochs
            context.hparams = hparams
            context.training_data = training_data
            context.batch_size = batch_size
            for key in kwargs: setattr(context, key, kwargs[key])
            context.training_log = self.__training_log
            context.cancellation_token = cancellation_token
            self._on_training_epoch_begin(epoch, context)
            batch_size = context.batch_size
            hparams = context.hparams
            epochs = context.epochs
            epoch = context.epoch
            iterations = context.iterations
            iteration = context.iteration
            # ----------------------------------------------------------------

            while ((iteration < iterations) and (not cancellation_token.is_cancellation_requested())):
                # ----------------------------------------------------------------
                try:
                    iteration_training_data = training_data_iterator.next(batch_size)
                except StopIteration:
                    break

                iteration += 1
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                context = ImperativeModel.TrainingContext()
                context.time_elapsed = stopwatch.elapsed
                context.iteration = iteration
                context.iterations = iterations
                context.epoch = epoch
                context.epochs = epochs
                context.hparams = hparams
                context.training_data = training_data
                context.batch_size = batch_size
                context.iteration_training_data = iteration_training_data
                for key in kwargs: setattr(context, key, kwargs[key])
                context.training_log = self.__training_log
                context.cancellation_token = cancellation_token
                self._on_training_iteration_begin(iteration, context)
                batch_size = context.batch_size
                hparams = context.hparams
                epochs = context.epochs
                epoch = context.epoch
                iterations = context.iterations
                iteration = context.iteration
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                if (self.exists_apply_cost_optimizer_function()):
                    if(hparams is None):
                        self.run_apply_cost_optimizer_function(iteration_training_data[0], iteration_training_data[1])
                    else:
                        self.run_apply_cost_optimizer_function(iteration_training_data[0], iteration_training_data[1], hparams)
                else:
                    context = ImperativeModel.TrainingContext()
                    context.time_elapsed = stopwatch.elapsed
                    context.iteration = iteration
                    context.iterations = iterations
                    context.epoch = epoch
                    context.epochs = epochs
                    context.hparams = hparams
                    context.training_data = training_data
                    context.batch_size = batch_size
                    context.iteration_training_data = iteration_training_data
                    for key in kwargs: setattr(context, key, kwargs[key])
                    context.training_log = self.__training_log
                    context.cancellation_token = cancellation_token
                    self._on_training_apply_cost_optimizer(context)
                    batch_size = context.batch_size
                    hparams = context.hparams
                    epochs = context.epochs
                    epoch = context.epoch
                    iterations = context.iterations
                    iteration = context.iteration
                # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                context = ImperativeModel.TrainingContext()
                context.time_elapsed = stopwatch.elapsed
                context.iteration = iteration
                context.epoch = epoch
                append_to_training_log_condition_result = append_to_training_log_condition(context=context)
                # ----------------------------------------------------------------
                if(append_to_training_log_condition_result):
                    self.__training_log.append_item(time_elapsed=stopwatch.elapsed, iteration=iteration, epoch=epoch+training_data_iterator.position/training_data_iterator.count())
                    # ----------------------------------------------------------------
                    context = ImperativeModel.TrainingContext()
                    context.time_elapsed = stopwatch.elapsed
                    context.iteration = iteration
                    context.iterations = iterations
                    context.epoch = epoch
                    context.epochs = epochs
                    context.hparams = hparams
                    context.training_data = training_data
                    context.batch_size = batch_size
                    context.iteration_training_data = iteration_training_data
                    for key in kwargs: setattr(context, key, kwargs[key])
                    context.training_log = self.__training_log
                    context.cancellation_token = cancellation_token
                    self._on_append_to_training_log(self.__training_log, context)
                    batch_size = context.batch_size
                    hparams = context.hparams
                    epochs = context.epochs
                    epoch = context.epoch
                    iterations = context.iterations
                    iteration = context.iteration
                    # ----------------------------------------------------------------

                # ----------------------------------------------------------------
                context = ImperativeModel.TrainingContext()
                context.time_elapsed = stopwatch.elapsed
                context.iteration = iteration
                context.iterations = iterations
                context.epoch = epoch
                context.epochs = epochs
                context.hparams = hparams
                context.training_data = training_data
                context.batch_size = batch_size
                context.iteration_training_data = iteration_training_data
                for key in kwargs: setattr(context, key, kwargs[key])
                context.training_log = self.__training_log
                context.cancellation_token = cancellation_token
                self._on_training_iteration_end(iteration, context)
                batch_size = context.batch_size
                hparams = context.hparams
                epochs = context.epochs
                epoch = context.epoch
                iterations = context.iterations
                iteration = context.iteration
                # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            context = ImperativeModel.TrainingContext()
            context.time_elapsed = stopwatch.elapsed
            context.iteration = iteration
            context.iterations = iterations
            context.epoch = epoch
            context.epochs = epochs
            context.hparams = hparams
            context.training_data = training_data
            context.batch_size = batch_size
            for key in kwargs: setattr(context, key, kwargs[key])
            context.training_log = self.__training_log
            context.cancellation_token = cancellation_token
            self._on_training_epoch_end(epoch, context)
            batch_size = context.batch_size
            hparams = context.hparams
            epochs = context.epochs
            epoch = context.epoch
            iterations = context.iterations
            iteration = context.iteration
            # ----------------------------------------------------------------

            # ----------------------------------------------------------------
            epoch += 1
            # ----------------------------------------------------------------

        # ----------------------------------------------------------------
        context = ImperativeModel.TrainingContext()
        context.time_elapsed = stopwatch.elapsed
        context.iteration = iteration
        context.iterations = iterations
        context.epoch = epoch
        context.epochs = epochs
        context.hparams = hparams
        context.training_data = training_data
        context.batch_size = batch_size
        for key in kwargs: setattr(context, key, kwargs[key])
        context.training_log = self.__training_log
        self._on_training_end(context)
        # ----------------------------------------------------------------

        stopwatch.stop()

        result = ImperativeModel.TrainingResult()
        result.time_elapsed = stopwatch.elapsed
        result.iteration = iteration
        result.iterations = iterations
        result.epoch = epoch
        result.epochs = epochs
        result.hparams = hparams
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
