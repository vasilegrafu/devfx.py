from .. import types
from .. import variables
from .. import initializers
from .. import math
from ..model import Model

def normalize(name, input):
    if(Model.is_called_by_apply_cost_optimizer()):
        alpha = 0.05
        mean = math.reduce_mean(input, axis=0)
        if(not variables.exists_variable(name=f'{name}__normalize__mean_ema')):
            mean_ema = variables.create_variable(name=f'{name}__normalize__mean_ema', 
                                                 shape=mean.shape, 
                                                 dtype=mean.dtype, 
                                                 initializer=lambda shape, dtype=None: mean, 
                                                 trainable=False)
        else:
            mean_ema = variables.get_variable(name=f'{name}__normalize__mean_ema')
            mean_ema = alpha*mean + (1.0 - alpha)*mean_ema

        var = math.reduce_var(input, axis=0)
        if(not variables.exists_variable(name=f'{name}__normalize__var_ema')):
            var_ema = variables.create_or_get_variable(name=f'{name}__normalize__var_ema', 
                                                       shape=var.shape, 
                                                       dtype=var.dtype, 
                                                       initializer=lambda shape, dtype=None: var,
                                                       trainable=False)
        else:
            var_ema = variables.get_variable(name=f'{name}__normalize__var_ema')
            var_ema = alpha*var + (1.0 - alpha)*var_ema
    else:
        mean_ema = variables.get_variable(name=f'{name}__normalize__mean_ema')
        var_ema = variables.get_variable(name=f'{name}__normalize__var_ema')

    epsilon = 1e-16
    norm_input = (input - mean_ema)/math.sqrt(var_ema + epsilon)

    gamma = variables.create_or_get_variable(name=f'{name}__normalize__gamma', 
                                             shape=(), 
                                             dtype=norm_input.dtype, 
                                             initializer=initializers.ones_initializer())
    beta = variables.create_or_get_variable(name=f'{name}__normalize__beta', 
                                            shape=(), 
                                            dtype=norm_input.dtype, 
                                            initializer=initializers.zeros_initializer())
    shifted_norm_input = gamma*norm_input + beta

    output = shifted_norm_input

    return output

