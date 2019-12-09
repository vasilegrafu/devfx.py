import tensorflow as tf

"""------------------------------------------------------------------------------------------------
"""
def function(input_signature=None):
    return tf.function(input_signature=input_signature)

"""------------------------------------------------------------------------------------------------
"""

def control_dependencies(control_inputs):
    return tf.control_dependencies(control_inputs=control_inputs)

def condition(predicate, true_fn=None, false_fn=None, name=None):
    return tf.cond(predicate=predicate, true_fn=true_fn, false_fn=false_fn, name=name)

def case(predicate_fn_pairs, default, name=None):
    return tf.case(predicate_fn_pairs=predicate_fn_pairs, default=default, exclusive=False, name=name)

def while_loop(condition, body, loop_variables, name=None):
    return tf.while_loop(cond=condition, body=body, loop_vars=loop_variables, name=name)

"""------------------------------------------------------------------------------------------------
"""
def group(*args,**kwargs):
    return tf.group(*args,**kwargs)

def tuple(tensors, control_inputs=None, name=None):
    return tf.tuple(tensors=tensors, control_inputs=control_inputs, name=name)
