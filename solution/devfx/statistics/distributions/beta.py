import numpy as np
import scipy as sp
import scipy.stats
import devfx.exceptions as exps
from .dcontinuous import dcontinuous


class beta(dcontinuous):
    def __init__(self, a=0.0, b=1.0, alpha=0.0, beta=1.0):
        if(alpha <= 0.0):
            raise exps.ArgumentOutOfRangeError()
        if(beta <= 0.0):
            raise exps.ArgumentOutOfRangeError()

        self.__distribution = sp.stats.beta(a=alpha, b=beta, loc=a, scale=(b-a))

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