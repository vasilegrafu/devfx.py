import devfx.exceptions as exceps
from .. import types
from .. import variables
from .. import initialization
from .. import math
from ..model import Model

"""------------------------------------------------------------------------------------------------
"""
class normalizer(object):
    def __init__(self):
        pass

    def normalize(self, name, input):
        return self._normalize(name=name, input=input)
    
    def _normalize(self, name, input):
        raise exceps.NotImplementedError()
    
"""------------------------------------------------------------------------------------------------
"""
class gauss_normalizer(normalizer):
    def __init__(self, alpha=0.05, epsilon=1e-8):
        self.__alpha = alpha
        self.__epsilon = epsilon

    @property
    def alpha(self):
        return self.__alpha

    @property
    def epsilon(self):
        return self.__epsilon

    def _normalize(self, name, input):
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
                mean_ema = self.__alpha*mean + (1.0 - self.__alpha)*mean_ema

            var = math.reduce_var(input, axis=0)
            if(not variables.exists_variable(name=f'{name}__var_ema')):
                var_ema = variables.create_or_get_variable(name=f'{name}__var_ema', 
                                                        shape=var.shape, 
                                                        dtype=var.dtype, 
                                                        initializer=lambda shape, dtype=None: var,
                                                        trainable=False)
            else:
                var_ema = variables.get_variable(name=f'{name}__var_ema')
                var_ema = self.__alpha*var + (1.0 - self.__alpha)*var_ema
        else:
            mean_ema = variables.get_variable(name=f'{name}__mean_ema')
            var_ema = variables.get_variable(name=f'{name}__var_ema')

        normalized_input = (input - mean_ema)/math.sqrt(var_ema + self.__epsilon)

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

"""------------------------------------------------------------------------------------------------
"""
class l2_normalizer(object):
    def __init__(self):
        pass

    def _normalize(self, name, input):
       raise exceps.NotImplementedError()
