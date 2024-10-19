import devfx.exceptions as exp
from .. import initialization
from .. import math
from ..sl import variables
from ..sl.model import Model
 
"""------------------------------------------------------------------------------------------------
"""
def gauss_normalizer(alpha=0.05, epsilon=1e-8):
    def __call(name, input):
        name = name + '__gauss_normalizer__normalize'
        
        if(Model.is_called_by_apply_cost_optimizer()):
            mean = math.reduce_mean(input, axis=0)
            if(not variables.exists_variable(name=f'{name}__mean_ema')):
                mean_ema = variables.create_variable(name=f'{name}__mean_ema', 
                                                    shape=mean.shape, 
                                                    dtype=mean.dtype, 
                                                    initializer=lambda shape, dtype=None: mean, 
                                                    trainable=False)
            else:
                mean_ema = variables.get_variable(name=f'{name}__mean_ema')
                mean_ema = alpha*mean + (1.0 - alpha)*mean_ema

            var = math.reduce_var(input, axis=0)
            if(not variables.exists_variable(name=f'{name}__var_ema')):
                var_ema = variables.create_or_get_variable(name=f'{name}__var_ema', 
                                                        shape=var.shape, 
                                                        dtype=var.dtype, 
                                                        initializer=lambda shape, dtype=None: var,
                                                        trainable=False)
            else:
                var_ema = variables.get_variable(name=f'{name}__var_ema')
                var_ema = alpha*var + (1.0 - alpha)*var_ema
        else:
            mean_ema = variables.get_variable(name=f'{name}__mean_ema')
            var_ema = variables.get_variable(name=f'{name}__var_ema')

        normalized_input = (input - mean_ema)/math.sqrt(var_ema + epsilon)

        gamma = variables.create_or_get_variable(name=f'{name}__gamma', 
                                                shape=(), 
                                                dtype=normalized_input.dtype, 
                                                initializer=initialization.ones_initializer())
        beta = variables.create_or_get_variable(name=f'{name}__beta', 
                                                shape=(), 
                                                dtype=normalized_input.dtype, 
                                                initializer=initialization.zeros_initializer())
        shifted_normalized_input = gamma*normalized_input + beta

        output = shifted_normalized_input

        return output
    return __call

"""------------------------------------------------------------------------------------------------
"""
def l2_normalizer():
    def __call(self, name, input):
       raise exp.NotImplementedError()
    return __call

