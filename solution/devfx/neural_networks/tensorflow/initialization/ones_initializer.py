import devfx.computation_graphs.tensorflow as cg

def ones_initializer(dtype=cg.float32):
    return cg.ones_initializer(dtype=dtype)