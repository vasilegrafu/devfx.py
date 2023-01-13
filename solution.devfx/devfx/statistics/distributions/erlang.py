import devfx.math as math
from .dcontinuous import dcontinuous
from .gamma import gamma

class erlang(dcontinuous):
    def __init__(self, n, rate):
        self.__distribution = gamma(n, rate)

        a = math.zero
        b = +math.inf
        super().__init__(a=a, b=b)

    """------------------------------------------------------------------------------------------------
    """     
    @property
    def rate(self):
        return self.__distribution.rate

    @rate.setter
    def rate(self, rate):
        self.__distribution.rate = rate
        
    @property
    def n(self):
        return self.__distribution.n

    @n.setter
    def n(self, n):
        self.__distribution.r = n
                      
    """------------------------------------------------------------------------------------------------
    """     
    def _cpdf(self, x):
        return self.__distribution.cdf(x)
        
    def _icpdf(self, p):
        return self.__distribution.icdf(p)
    
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
        return self.__distribution.skew()
        
    def _kurtosis(self):
        return self.__distribution.kurtosis()
        
