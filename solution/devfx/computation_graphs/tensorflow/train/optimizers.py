import tensorflow as tf
import devfx.reflection as refl
from .. import mathematics

"""------------------------------------------------------------------------------------------------
"""
GradientDescentOptimizer = tf.optimizers.SGD
AdadeltaOptimizer = tf.optimizers.Adadelta
AdagradOptimizer = tf.optimizers.Adagrad
AdamOptimizer = tf.optimizers.Adam

"""------------------------------------------------------------------------------------------------
"""
def construct_optimizer_applier(optimizer, fn, grad_clipping_values=None):
    if(not refl.is_typeof(fn, list)):
        grads_and_vars = optimizer.compute_gradients(fn)
        if (grad_clipping_values is not None):
            grads_and_vars = [(mathematics.clip_by_value(grad, grad_clipping_values[0], grad_clipping_values[1]), var) for grad, var in grads_and_vars]
        optimizer_applier = optimizer.apply_gradients(grads_and_vars=grads_and_vars)
        return optimizer_applier
    else:
        fns = fn
        def __average_grads_and_first_vars(tower_grads_and_vars):
            average_grads_and_first_vars = []
            for grads_and_vars in zip(*tower_grads_and_vars):
                average_grad = tf.reduce_mean([grad for grad, _ in grads_and_vars], axis=0)
                first_var = grads_and_vars[0][1]
                average_grads_and_first_vars.append((average_grad, first_var))
            return average_grads_and_first_vars
        tower_grads_and_vars = []
        for fn in fns:
            grads_and_vars = optimizer.compute_gradients(fn)
            if (grad_clipping_values is not None):
                grads_and_vars = [(mathematics.clip_by_value(grad, grad_clipping_values[0], grad_clipping_values[1]), var) for grad, var in grads_and_vars]
            tower_grads_and_vars.append(grads_and_vars)
        average_grads_and_first_vars = __average_grads_and_first_vars(tower_grads_and_vars)
        optimizer_applier = optimizer.apply_gradients(grads_and_vars=average_grads_and_first_vars)
        return optimizer_applier


def implicit_gradients(fn):
    return tf.contrib.eager.implicit_gradients(fn)