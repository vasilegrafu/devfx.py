import devfx.computation_graphs.tensorflow as cg
from .. import initialization

def fully_connected(name,
                    input,
                    n,
                    initializer=None,
                    normalizer=None,
                    activation_fn=None):

    with cg.scope(name):
        # parameters
        if(initializer is None):
            initializer = initialization.xavier_glorot_random_truncated_normal_initializer()

        if(normalizer is None):
            normalizer = lambda x : x

        if (activation_fn is None):
            activation_fn = lambda x : x

        # algorithm
        input_shape = tuple([_ for _ in input.shape])
        input_M = input_shape[0]
        input_item_shape = input_shape[1:]

        w_shape = [n, *input_item_shape]
        b_shape = [n]

        w = cg.create_variable(name='w', shape=w_shape, initializer=initializer)
        b = cg.create_variable(name='b', shape=b_shape, initializer=initializer)

        # z: mj,ij->mi + b
        z = cg.tensordot(input, w, axes=(list(range(len(input_shape))[1:]), list(range(len(w_shape))[1:]))) + b

        z = normalizer(z)

        output = activation_fn(z)

        return output