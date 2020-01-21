import numpy as np
import scipy as sp
import devfx.exceptions as exps
import devfx.core as core
import devfx.math as math
from ..series import center
from .distribution import distribution
from .empirical import empirical

class ddiscrete(distribution):
    def __init__(self, a=math.zero, b=+math.inf):
        super().__init__(a, b)

    """------------------------------------------------------------------------------------------------
    """       
    def _cdf(self, x):
        return self.cpmf(x)
        
    def _icdf(self, p):
        return self.icpmf(p)
        
    
    def cpmf(self, x):
        return self._cpmf(x)
        
    def _cpmf(self, x):
        raise exps.NotImplementedError()
        
    def icpmf(self, p):
        return self._icpmf(p)
        
    def _icpmf(self, p):
        raise exps.NotImplementedError()
       
    """------------------------------------------------------------------------------------------------
    """
    def pmf(self, x):
        if(core.is_iterable(x)):
            if(np.where((x < self.a) | (x > self.b))[0].size > 0):
                raise exps.ArgumentOutOfRangeError()
            return self._pmf(x)
        else:
            if((x < self.a) or (x > self.b)):
                raise exps.ArgumentOutOfRangeError()
            return self._pmf(x)

    def _pmf(self, x):
        raise exps.NotImplementedError()
                         
    """------------------------------------------------------------------------------------------------
    """         
    def _mean(self):
        raise exps.NotImplementedError()
       
    def _var(self):
        raise exps.NotImplementedError()
       
    def _skew(self):
        raise exps.NotImplementedError()
        
    def _kurtosis(self):
        raise exps.NotImplementedError()


    """------------------------------------------------------------------------------------------------
    """
    def kstest(self, data):
        data = np.asarray(data)
        a = math.min(data)
        b = math.max(data)
        xrange = np.hstack((math.range(start=a, stop=b, step=1), b))
        coef = math.sqrt(center.mean((self.cdf(xrange)-empirical(data).cdf(xrange))**2))
        return coef

    """------------------------------------------------------------------------------------------------
    """
    class _ddiscrete_on_chart(distribution._distribution_on_chart):
        def __init__(self, distribution, distributionf, chart):
            super().__init__(distribution, distributionf, chart)

        def _get_xrange(self, kwargs):
            (ll, ul) = self._get_xinterval(kwargs)
            xrange = np.hstack((math.range(start=ll, stop=ul, step=1), ul))
            return xrange

    def cdf_on_chart(self, chart):
        return ddiscrete._ddiscrete_on_chart(self, self.cdf, chart)

    def pmf_on_chart(self, chart):
        return ddiscrete._ddiscrete_on_chart(self, self.pmf, chart)



