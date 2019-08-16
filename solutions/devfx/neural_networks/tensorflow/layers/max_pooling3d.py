from .max_poolingNd import max_poolingNd

def max_pooling3d(name,
                  input,
                  pool_size=(2, 2, 2),
                  strides=(2, 2, 2),
                  padding='valid'):
    pool = max_poolingNd(N=3,
                         name=name,
                         input=input,
                         pool_size=pool_size,
                         strides=strides,
                         padding=padding)
    return pool