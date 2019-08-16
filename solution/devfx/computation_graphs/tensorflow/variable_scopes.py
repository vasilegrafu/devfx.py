import tensorflow as tf

"""------------------------------------------------------------------------------------------------
"""
def scope(name_or_scope,
          values=None,
          variables_dtype=None, variables_initializer=None, variables_regularizer=None, variables_partitioner=None, variables_reuse=None):
    return tf.variable_scope(name_or_scope,
                             values=values,
                             dtype=variables_dtype, initializer=variables_initializer, regularizer=variables_regularizer,  partitioner=variables_partitioner, reuse=variables_reuse)

def get_scope():
    return tf.get_variable_scope()



