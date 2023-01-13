import numpy as np
import scipy as sp
import scipy.stats
import devfx.math as math
from .ddiscrete import ddiscrete

""" bernoulli.pmf(k) = 1-p  if k = 0
    bernoulli.pmf(k) = p    if k = 1
"""
class bernoulli(ddiscrete):
    def __init__(self, p):
        self.p = p
        self.__distribution = sp.stats.bernoulli(p=self.p)

        a = math.zero
        b = math.one
        super().__init__(a=a, b=b)

    """------------------------------------------------------------------------------------------------
    """ 
    @property 
    def p(self):
        return self.__p
    
    @p.setter   
    def p(self, p):
        self.__p = p
                         
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
        
