import numpy as np
import scipy as sp
import devfx.exceptions as exceptions
import devfx.reflection as refl
import devfx.mathematics as math
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
        raise exceptions.NotImplementedError()
        
    def icpdf(self, p):
        return self._icpdf(p)
        
    def _icpdf(self, p):
        raise exceptions.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def pdf(self, x):
        if(refl.is_iterable(x)):
            if(np.where((x < self.a) | (x > self.b))[0].size > 0):
                raise exceptions.ArgumentOutOfRangeError()
            return self._pdf(x)
        else:
            if ((x < self.a) or (x > self.b)):
                raise exceptions.ArgumentOutOfRangeError()
            return self._pdf(x)

    def _pdf(self, x):
        raise exceptions.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """    
    def _mean(self):
        raise exceptions.NotImplementedError()
       
    def _var(self):
        raise exceptions.NotImplementedError()
       
    def _skew(self):
        raise exceptions.NotImplementedError()
        
    def _kurtosis(self):
        raise exceptions.NotImplementedError()

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
