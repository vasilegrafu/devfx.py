import numpy as np
import scipy as sp
import scipy.stats
import devfx.mathematics as math
from .dcontinuous import dcontinuous

""" Let X be a gamma random variable with parameters (n, rate).
    To find f, the density function of X, note that {X <= x} occurs if the time of the nth event is in [0, x],
    that is, if the number of events occurring in [0, x] is at least n.
"""
""" Gamma is the time we will wait for the nth event to occur.
"""
class gamma(dcontinuous):
    def __init__(self, n, rate):
        self.n = n
        self.rate = rate
        self.__distribution = sp.stats.gamma(a=self.n, scale=1.0/self.rate)

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
        
    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n):
        self.__n = n
       
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

