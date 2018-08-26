import devfx.diagnostics as dgn
import devfx.computation_graphs.tensorflow as cg
from ... import initialization

def __base_conv2d(name,
                  input, # NHWC
                  kernel_size, # HW
                  strides=(1, 1), # HW
                  kernel_initializer=None,
                  bias_initializer=None):
    with cg.scope(name):
        # parameters
        if (kernel_initializer is None):
            kernel_initializer = initialization.xavier_glorot_random_truncated_normal_initializer(dtype=input.dtype)

        if (bias_initializer is None):
            bias_initializer = initialization.zeros_initializer(dtype=input.dtype)

        # algorithm
        input_shape = tuple([_.value for _ in input.shape])
        input_N = input_shape[0]
        input_H = input_shape[1]
        input_W = input_shape[2]
        input_C = input_shape[3]
        input_item_shape = input_shape[1:]
        input_item_H = input_item_shape[0]
        input_item_W = input_item_shape[1]
        input_item_C = input_item_shape[2]

        kernel_shape = (kernel_size[0], kernel_size[1], input_C)
        kernel_H = kernel_shape[0]
        kernel_W = kernel_shape[1]
        kernel_C = kernel_shape[2]

        strides_H = strides[0]
        strides_W = strides[1]

        z_shape = (input_H - kernel_H, input_W - kernel_W)
        z_H = z_shape[0]
        z_W = z_shape[1]

        bias_shape = (input_H - kernel_H, input_W - kernel_W)
        bias_H = bias_shape[0]
        bias_W = bias_shape[1]

        kernel = cg.create_variable(name='kernel', shape=kernel_shape, dtype=input.dtype, initializer=kernel_initializer)
        bias = cg.create_variable(name='bias', shape=bias_shape, dtype=input.dtype, initializer=bias_initializer)

        stopwatch = dgn.stopwatch().start()

        z = []
        h = 0
        while(h < (input_item_H - kernel_H)):
            z_h = []
            w = 0
            while(w < (input_item_W - kernel_W)):
                input_hw = input[:, h:h + kernel_H, w:w + kernel_W, :]
                z_hw = cg.tensordot(input_hw, kernel, axes=([1, 2, 3], [0, 1, 2])) + bias[h, w]
                z_h.append(z_hw)
                w += strides_W
            z.append(z_h)
            h += strides_H

        output = z

        time_elapsed = stopwatch.elapsed
        print(time_elapsed)

        return output


def conv2d(name,
           input,
           filters,
           kernel_size,
           strides=(1, 1),
           kernel_initializer=None,
           bias_initializer=None,
           normalizer=None,
           activation_fn=None):
    with cg.scope(name):
        # parameters
        if(kernel_initializer is None):
            kernel_initializer = initialization.xavier_glorot_random_truncated_normal_initializer(dtype=input.dtype)

        if(bias_initializer is None):
            bias_initializer = initialization.zeros_initializer(dtype=input.dtype)

        if(normalizer is None):
            normalizer = lambda x : x

        if (activation_fn is None):
            activation_fn = lambda x : x

        # algorithm
        z = None
        filter_i = 0
        while(filter_i < filters):
            z_i = __base_conv2d(name = (name + str(filter_i)),
                                input=input,
                                kernel_size=kernel_size,
                                strides=strides,
                                kernel_initializer=kernel_initializer,
                                bias_initializer=bias_initializer)
            if (z is None):
                z = z_i
            else:
                z = cg.stack([z, z_i], axis=0)
            filter_i += 1

        z = normalizer(z)

        output = activation_fn(z)

        return output




