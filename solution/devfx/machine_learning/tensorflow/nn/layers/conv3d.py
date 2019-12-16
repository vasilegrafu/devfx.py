from .convNd import convNd

def conv3d(name,
           input,
           filters,
           kernel_size,
           strides=(1, 1, 1),
           padding='valid',
           kernel_initializer=None,
           bias_initializer=None,
           normalizer=None,
           activation_fn=None):
    output = convNd(N=3,
                    name=name,
                    input=input,
                    filters=filters,
                    kernel_size=kernel_size,
                    strides=strides,
                    padding=padding,
                    kernel_initializer=kernel_initializer,
                    bias_initializer=bias_initializer,
                    normalizer=normalizer,
                    activation_fn=activation_fn)
    return output


