import numpy as np
import scipy as sp
import scipy.stats
import devfx.math as math
from .ddiscrete import ddiscrete

""" It’s the probability that the first occurrence of success requires k number of independent trials, each with success probability p.
    If the probability of success on each trial is p, then the probability that the kth trial (out of k trials) is the first success.
"""
""" X = the number of experiments up to and including the first success:
    P(X=k)=pmf(k)=((1.0-p)**(k-1))*p, (k = 1, 2, 3, ...).
"""
class geometrick1(ddiscrete):
    def __init__(self, p):
        """ p = probability to get a success result
        """
        self.p = p
        self.__distribution = sp.stats.geom(p=self.p, loc=0)

        a = math.one
        b = +math.inf
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


""" X = the number of failures (only failures) until the first success:
    P(X=k)=pmf(k)=((1.0-p)**k)*p, (k = 0, 1, 2, 3, ...).
"""
class geometrick0(ddiscrete):
    def __init__(self, p):
        """ p = probability to get a success result
        """
        self.p = p
        self.__distribution = sp.stats.geom(p=self.p, loc=-1)

        a = math.zero
        b = +math.inf
        ddiscrete.__init__(self, a=a, b=b)

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

