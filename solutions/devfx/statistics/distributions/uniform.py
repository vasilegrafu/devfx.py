import numpy as np
import scipy as sp
import scipy.stats
from .dcontinuous import dcontinuous

class uniform(dcontinuous):
    def __init__(self, a=0.0, b=1.0):
        self.__distribution = sp.stats.uniform(loc=a, scale=(b-a))

        super().__init__(a=a, b=b)
        
    """------------------------------------------------------------------------------------------------
    """       
    def _cpdf(self, x):
        return self.__distribution.cdf(x)
        
    def _icpdf(self, p):
        return self.__distribution.ppf(p)
    
    """------------------------------------------------------------------------------------------------
    """ 
    def _pdf(self, x):
        return self.__distribution.pdf(x)
         
    """------------------------------------------------------------------------------------------------
    """       
    def _rvs(self, size):
        return self.__distribution.rvs(size)
   
    """------------------------------------------------------------------------------------------------
    """      
    def _mean(self):
        return self.__distribution.mean()
        
    def _var(self):
        return self.__distribution.var()
                       
    def _skew(self):
        return self.__distribution.stats(moments='s')
        
    def _kurtosis(self):
        return self.__distribution.stats(moments='k')

