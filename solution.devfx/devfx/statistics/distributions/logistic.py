import scipy as sp
import scipy.stats
import devfx.math as math
from .dcontinuous import dcontinuous

"""------------------------------------------------------------------------------------------------
"""  
class logistic(dcontinuous):
    def __init__(self, mu=0.0, s=1.0):
        self.mu = mu
        self.s = s
        self.__distribution = sp.stats.logistic(loc=self.mu, scale=s)

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
    def s(self):
        return self.__s

    @s.setter
    def s(self, s):
        self.__s = s
        
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

