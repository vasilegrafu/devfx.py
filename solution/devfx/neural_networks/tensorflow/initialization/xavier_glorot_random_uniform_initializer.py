import devfx.computation_graphs.tensorflow as cg

def xavier_glorot_random_uniform_initializer(dtype=cg.float32, seed=None):
    return cg.xavier_glorot_random_uniform_initializer(dtype=dtype, seed=seed)
