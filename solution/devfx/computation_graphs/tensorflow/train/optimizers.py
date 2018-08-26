import tensorflow as tf
from .. import mathematics

"""------------------------------------------------------------------------------------------------
"""
GradientDescentOptimizer = tf.train.GradientDescentOptimizer
MomentumOptimizer = tf.train.MomentumOptimizer
AdadeltaOptimizer = tf.train.AdadeltaOptimizer
AdagradOptimizer = tf.train.AdagradOptimizer
AdamOptimizer = tf.train.AdamOptimizer

"""------------------------------------------------------------------------------------------------
"""
def construct_optimizer_applier(optimizer, fn, grad_clipping_values=None):
    grads_and_vars = optimizer.compute_gradients(fn)
    if (grad_clipping_values is not None):
        grads_and_vars = [(mathematics.clip_by_value(grad, grad_clipping_values[0], grad_clipping_values[1]), var) for grad, var in grads_and_vars]
    optimizer_applier = optimizer.apply_gradients(grads_and_vars=grads_and_vars)
    return optimizer_applier

def construct_distributed_optimizer_applier(optimizer, fns, grad_clipping_values=None):
    def __average_grads(tower_grads_and_vars):
        average_grads = []
        for grad_and_vars in zip(*tower_grads_and_vars):
            grad = tf.reduce_mean(
                tf.concat(axis=0, values=[tf.expand_dims(g, 0) for g, _ in grad_and_vars]), 0)
            var = grad_and_vars[0][1]
            grad_and_var = (grad, var)
            average_grads.append(grad_and_var)
        return average_grads
    costs_grads_and_vars = []
    for fn in fns:
        grads_and_vars = optimizer.compute_gradients(fn)
        if (grad_clipping_values is not None):
            grads_and_vars = [(mathematics.clip_by_value(grad, grad_clipping_values[0], grad_clipping_values[1]), var) for grad, var in grads_and_vars]
        costs_grads_and_vars.append(grads_and_vars)
    average_grads_and_vars = __average_grads(costs_grads_and_vars)
    optimizer_applier = optimizer.apply_gradients(grads_and_vars=average_grads_and_vars)
    return optimizer_applier


def implicit_gradients(fn):
    return tf.contrib.eager.implicit_gradients(fn)