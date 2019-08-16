import numpy as np
import scipy as sp
import scipy.stats
import devfx.mathematics as math
from .dcontinuous import dcontinuous


class dcontinuous_builder(dcontinuous):
    def __init__(self, cdf=None, pdf=None, a=-math.inf, b=+math.inf):
        self.__distribution = sp.stats.rv_continuous(a=a, b=b)
                
        if(cdf is None):
            cdf = lambda x: math.S1d(pdf, a=self.a, b=x)
        self.__distribution._cdf = cdf
        
        if(pdf is None):
            pdf = lambda x: math.D1d(cdf, x)
        self.__distribution._pdf = pdf

        super().__init__(a=a, b=b)
        
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