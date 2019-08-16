import devfx.computation_graphs.tensorflow as cg

def constant_initializer(value=0.0, dtype=cg.float32):
    return cg.constant_initializer(value=value, dtype=dtype)