import numpy as np
import scipy as sp
import scipy.stats
import devfx.mathematics as math
from .ddiscrete import ddiscrete

""" Negative binomial random variables are generalizations of geometric random variables.
    Suppose that a sequence of independent Bernoulli trials, each with probability of success p, 0 < p < 1, is performed.
    Let X be the number of experiments until the nth success occurs. Then X is a discrete random variable called a negative binomial.
"""
""" Number of experiments until the nth success occurs.
"""
class negbinomial(ddiscrete):
    def __init__(self, n, p):
        """ n = number of success results
            p = probability to get a success result
        """
        self.n = n
        self.p = p
        self.__distribution = sp.stats.nbinom(n=self.n, p=self.p)

        a = n
        b = +math.inf
        super().__init__(a=a, b=b)

    """------------------------------------------------------------------------------------------------
    """    
    @property
    def n(self):
        return self.__n
    
    @n.setter
    def n(self, n):
        self.__n = n

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
        
