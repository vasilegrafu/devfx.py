import numpy as np
import scipy as sp
import scipy.stats
import devfx.mathematics as math
from .dcontinuous import dcontinuous

"""------------------------------------------------------------------------------------------------
"""  
class lognormal(dcontinuous):
    def __init__(self, mu=0.0, sigma2=1.0**2):
        self.mu = mu
        self.sigma2 = sigma2

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
        return sp.stats.lognorm.cdf(x, s=math.sqrrt(self.sigma2), loc=0.0, scale=math.expe(self.mu))
        
    def _icpdf(self, p):
        return sp.stats.lognorm.ppf(p, s=math.sqrrt(self.sigma2), loc=0.0, scale=math.expe(self.mu))
    
    """------------------------------------------------------------------------------------------------
    """ 
    def _pdf(self, x):
        return sp.stats.lognorm.pdf(x, s=math.sqrrt(self.sigma2), loc=0.0, scale=math.expe(self.mu))
        
    """------------------------------------------------------------------------------------------------
    """       
    def _rvs(self, size):
        return sp.stats.lognorm.rvs(size, s=math.sqrrt(self.sigma2), loc=0.0, scale=math.expe(self.mu))
   
    """------------------------------------------------------------------------------------------------
    """       
    def _mean(self):
        return sp.stats.lognorm.mean(s=math.sqrrt(self.sigma2), loc=0.0, scale=math.expe(self.mu))
        
    def _var(self):
        return sp.stats.lognorm.var(s=math.sqrrt(self.sigma2), loc=0.0, scale=math.expe(self.mu))
                       
    def _skew(self):
        return sp.stats.lognorm.stats(moments='s', s=math.sqrrt(self.sigma2), loc=0.0, scale=math.expe(self.mu))
        
    def _kurtosis(self):
        return sp.stats.lognorm.stats(moments='k', s=math.sqrrt(self.sigma2), loc=0.0, scale=math.expe(self.mu))
       