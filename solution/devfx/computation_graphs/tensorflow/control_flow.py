import tensorflow as tf

"""------------------------------------------------------------------------------------------------
"""

def control_dependencies(control_inputs):
    return tf.control_dependencies(control_inputs)

def condition(predicate, true_fn=None, false_fn=None, name=None):
    return tf.cond(predicate, true_fn=true_fn, false_fn=false_fn, name=name)

def case(predicate_fn_pairs, default, name=None):
    return tf.case(predicate_fn_pairs, default, exclusive=False, name=name)

def while_loop(condition, body, loop_variables, name=None):
    return tf.while_loop(condition, body, loop_variables, name=name)

"""------------------------------------------------------------------------------------------------
"""
def group(inputs):
    return tf.group(*inputs)

def tuple(tensors, control_inputs=None, name=None):
    return tf.tuple(tensors=tensors, control_inputs=control_inputs, name=name)
