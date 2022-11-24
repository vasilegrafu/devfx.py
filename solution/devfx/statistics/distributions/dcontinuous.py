import numpy as np
import scipy as sp
import devfx.exceptions as ex
import devfx.core as core
import devfx.math as math
from .distribution import distribution


class dcontinuous(distribution):
    def __init__(self, a=-math.inf, b=+math.inf):
        super().__init__(a, b)
        
    """------------------------------------------------------------------------------------------------
    """   
    def _cdf(self, x):
        return self.cpdf(x)
        
    def _icdf(self, p):
        return self.icpdf(p)
        
    
    def cpdf(self, x):
        return self._cpdf(x)
        
    def _cpdf(self, x):
        raise ex.NotImplementedError()
        
    def icpdf(self, p):
        return self._icpdf(p)
        
    def _icpdf(self, p):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def pdf(self, x):
        if(core.is_iterable(x)):
            if(np.where((x < self.a) | (x > self.b))[0].size > 0):
                raise ex.ArgumentOutOfRangeError()
            return self._pdf(x)
        else:
            if ((x < self.a) or (x > self.b)):
                raise ex.ArgumentOutOfRangeError()
            return self._pdf(x)

    def _pdf(self, x):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """    
    def _mean(self):
        raise ex.NotImplementedError()
       
    def _var(self):
        raise ex.NotImplementedError()
       
    def _skew(self):
        raise ex.NotImplementedError()
        
    def _kurtosis(self):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    class _dcontinuous_on_chart(distribution._distribution_on_chart):
        def __init__(self, distribution, distributionf, chart):
            super().__init__(distribution, distributionf, chart)

        def _get_xrange(self, kwargs):
            (ll, ul) = self._get_xinterval(kwargs)
            n = kwargs.pop('n', 1024)
            xrange = math.linspace(start=ll, stop=ul, count=n)
            return xrange

    def cdf_on_chart(self, chart):
        return dcontinuous._dcontinuous_on_chart(self, self.cdf, chart)

    def pdf_on_chart(self, chart):
        return dcontinuous._dcontinuous_on_chart(self, self.pdf, chart)
