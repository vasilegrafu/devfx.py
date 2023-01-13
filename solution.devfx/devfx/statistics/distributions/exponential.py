import numpy as np
import scipy as sp
import scipy.stats
import devfx.math as math
from .dcontinuous import dcontinuous

""" Exponential is the time we will wait for the first event to occur.
"""
class exponential(dcontinuous):
    def __init__(self, rate):
        self.rate = rate
        self.__distribution = sp.stats.expon(scale=1.0/self.rate)

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
        
