import numpy as np
import scipy as sp
import scipy.stats
import devfx.mathematics as math
from .ddiscrete import ddiscrete

class poisson(ddiscrete):
    def __init__(self, rate):
        self.rate = rate
        self.__distribution = sp.stats.poisson(mu=self.rate)

        a = math.zero
        b = +math.inf
        super().__init__(a=a, b=b)

    """------------------------------------------------------------------------------------------------
    """       
    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        self.__rate = rate
               
    """------------------------------------------------------------------------------------------------
    """       
    def _cpmf(self, x):
        return self.__distribution.cdf(x)
        
    def _icpmf(self, p):
        return self.__distribution.ppf(p)
    
    """------------------------------------------------------------------------------------------------
    """ 
    def _pmf(self, x):
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

