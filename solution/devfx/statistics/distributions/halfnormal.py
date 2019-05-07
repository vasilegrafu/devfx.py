import numpy as np
import scipy as sp
import scipy.stats
import devfx.mathematics as math
from .dcontinuous import dcontinuous

"""------------------------------------------------------------------------------------------------
"""  
class halfnormal(dcontinuous):
    def __init__(self, mu=0.0, sigma2=1.0**2):
        self.mu = mu
        self.sigma2 = sigma2
        self.__distribution = sp.stats.halfnorm(loc=self.mu, scale=math.sqrt(self.sigma2))

        a = -math.inf
        b = +math.inf
        super().__init__(a=a, b=b)
       
    """------------------------------------------------------------------------------------------------
    """        
    @property
    def mu(self):
        return self.__mu

    @mu.setter
    def mu(self, mu):
        self.__mu = mu
        
    @property
    def sigma2(self):
        return self.__sigma2

    @sigma2.setter
    def sigma2(self, sigma2):
        self.__sigma2 = sigma2
        
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



