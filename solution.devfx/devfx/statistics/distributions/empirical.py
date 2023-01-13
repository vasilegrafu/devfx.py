import numpy as np
import scipy as sp
import scipy.stats
import scipy.interpolate
import devfx.math as math
from .distribution import distribution

class empirical(distribution):
    def __init__(self, data, olNx=None):
        self.__data = np.asarray(data)
        self.__setup()

        if(olNx is not None):
            self.__data = np.asarray([x for x in self.__data if(not self.is_outlierNx(x, olNx))])
            self.__setup()

    def __setup(self):
        itemfreq = np.unique(self.__data, return_counts=True)
        item = itemfreq[0]
        freq = itemfreq[1]
        cfreq = math.csum(freq/math.sum(freq))

        __x = item
        __cdf = cfreq
        self.__x_cdf = sp.interpolate.interp1d(__x, __cdf)
        self.__cdf_x = sp.interpolate.interp1d(__cdf, __x)

        a = math.min(self.__data)
        b = math.max(self.__data)
        super().__init__(a=a, b=b)
    
    """------------------------------------------------------------------------------------------------
    """         
    def _cdf(self, x):
        return self.__x_cdf(x)
            
    def _icdf(self, p):
        return self.__cdf_x(p)

    """------------------------------------------------------------------------------------------------
    """  
    def _mean(self):
        return np.average(self.__data)

    def _var(self):
        return np.var(self.__data)

    def _skew(self):
        return sp.stats.skew(self.__data)
        
    def _kurtosis(self):
        return sp.stats.kurtosis(self.__data)

    """------------------------------------------------------------------------------------------------
    """
    class _empirical_on_chart(distribution._distribution_on_chart):
        def __init__(self, distribution, distributionf, chart):
            super().__init__(distribution, distributionf, chart)

        def _get_xrange(self, kwargs):
            (ll, ul) = self._get_xinterval(kwargs)
            n = kwargs.pop('n', 1024)
            xrange = math.linspace(start=ll, stop=ul, count=n)
            return xrange

    def cdf_on_chart(self, chart):
        return empirical._empirical_on_chart(self, self.cdf, chart)




