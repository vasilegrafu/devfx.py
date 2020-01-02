from .. import types
from .. import variables
from .. import initializers
from .. import math
from ..model import Model

def batch_norm(name, input):
    if(Model.is_called_by_apply_cost_optimizer()):
        mean = math.reduce_mean(input, axis=0)
        if(not variables.exists_variable(name=f'{name}__batch_norm__mean_ema')):
            mean_ema = variables.create_variable(name=f'{name}__batch_norm__mean_ema', 
                                                 shape=mean.shape, 
                                                 dtype=mean.dtype, 
                                                 initializer=lambda shape, dtype=None: mean, 
                                                 trainable=False)
        else:
            mean_ema = variables.get_variable(name=f'{name}__batch_norm__mean_ema')
            mean_ema = 0.9*mean_ema + 0.1*mean

        var = math.reduce_var(input, axis=0)
        if(not variables.exists_variable(name=f'{name}__batch_norm__var_ema')):
            var_ema = variables.create_or_get_variable(name=f'{name}__batch_norm__var_ema', 
                                                       shape=var.shape, 
                                                       dtype=var.dtype, 
                                                       initializer=lambda shape, dtype=None: var,
                                                       trainable=False)
        else:
            var_ema = variables.get_variable(name=f'{name}__batch_norm__var_ema')
            var_ema = 0.9*var_ema + 0.1*var
    else:
        mean_ema = variables.get_variable(name=f'{name}__batch_norm__mean_ema')
        var_ema = variables.get_variable(name=f'{name}__batch_norm__var_ema')

    epsilon = 1e-8
    norm_input = (input - mean_ema)/math.sqrt(var_ema + epsilon)

    gamma = variables.create_or_get_variable(name=f'{name}__batch_norm__gamma', 
                                             shape=(), 
                                             dtype=norm_input.dtype, 
                                             initializer=initializers.ones_initializer())
    beta = variables.create_or_get_variable(name=f'{name}__batch_norm__beta', 
                                            shape=(), 
                                            dtype=norm_input.dtype, 
                                            initializer=initializers.zeros_initializer())
    shifted_norm_input = gamma*norm_input + beta

    output = shifted_norm_input

    return output

