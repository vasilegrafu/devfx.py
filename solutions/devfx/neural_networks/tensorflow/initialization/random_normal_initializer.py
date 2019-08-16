import devfx.computation_graphs.tensorflow as cg

def random_normal_initializer(mean=0.0, stddev=1.0, dtype=cg.float32, seed=None):
    return cg.random_normal_initializer(mean=mean, stddev=stddev, dtype=dtype, seed=seed)