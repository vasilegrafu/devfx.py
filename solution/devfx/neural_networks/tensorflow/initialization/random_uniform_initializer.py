import devfx.computation_graphs.tensorflow as cg

def random_uniform_initializer(min=0.0, max=None, dtype=cg.float32, seed=None):
    return cg.random_uniform_initializer(min=min, max=max, dtype=dtype, seed=seed)