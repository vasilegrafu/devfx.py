import numpy as np
import scipy as sp
import scipy.stats
import devfx.math as math
from .dcontinuous import dcontinuous

class student(dcontinuous):
    def __init__(self, n=1):
        self.n = n
        self.__distribution = sp.stats.t(df=n)

        a = -math.inf
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
       


