import numpy as np
import scipy as sp
import scipy.stats
import devfx.core as core
import devfx.math as math
from .ddiscrete import ddiscrete


class ddiscrete_builder(ddiscrete):
    def __init__(self, cdf=None, pmf=None, a=math.zero, b=+math.inf):
        self.__distribution = sp.stats.rv_discrete(a=a, b=b)
                
        if(cdf is None):
            cdf = lambda x: math.sum([pmf(x) for x in np.arange(self.a, x+1)])
        self.__distribution._cdf = cdf
        
        if(pmf is None):
            pmf = lambda x: cdf(x) if (x == self.a) else (cdf(x)-cdf(x-1))
        self.__distribution._pmf = pmf

        super().__init__(a=a, b=b)
        
    """------------------------------------------------------------------------------------------------
    """     
    def _cpmf(self, x):
        if (core.is_iterable(x)):
            return np.asarray([self.__distribution.cdf(x) for x in x])
        else:
            return self.__distribution.cdf(x)
        
    def _icpmf(self, p):
        return self.__distribution.ppf(p)
    
    """------------------------------------------------------------------------------------------------
    """ 
    def _pmf(self, x):
        if (core.is_iterable(x)):
            return np.asarray([self.__distribution.pmf(x) for x in x])
        else:
            return self.__distribution.pmf(x)
               
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
