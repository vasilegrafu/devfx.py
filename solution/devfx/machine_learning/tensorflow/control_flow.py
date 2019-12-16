import tensorflow as tf

"""------------------------------------------------------------------------------------------------
"""
def condition(predicate, true_fn=None, false_fn=None, name=None):
    return tf.cond(predicate, true_fn=true_fn, false_fn=false_fn, name=name)

def case(predicate_fn_pairs, default=None, name=None):
    return tf.case(predicate_fn_pairs, default=default, name=name)

def while_loop(condition, body, loop_variables, name=None):
    return tf.while_loop(condition, body, loop_variables, name=name)

"""------------------------------------------------------------------------------------------------
"""
def group(*args,**kwargs):
    return tf.group(*args,**kwargs)

def tuple(tensors, control_inputs=None, name=None):
    return tf.tuple(tensors, control_inputs=control_inputs, name=name)
