import numpy as np
import scipy as sp
import devfx.exceptions as exps
import devfx.core as core
import devfx.math as math
from .distribution_algebra_operation_node import distribution_algebra_operation_node

"""------------------------------------------------------------------------------------------------
"""
class distribution(distribution_algebra_operation_node):
    def __init__(self, a=-math.inf, b=+math.inf):
        super().__init__(lambda size: self.rvs(size))

        self.a = a
        self.b = b
        
        self.cdf_a = self.cdf(a)
        self.cdf_b = self.cdf(b)
        
        self.__nd = None

        self.__ndr = None

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, a):
        self.__a = a
        
    @property
    def b(self):
        return self.__b
    
    @b.setter
    def b(self, b):
        self.__b = b
        
    """------------------------------------------------------------------------------------------------
    """
    @property
    def cdf_a(self):
        return self.__cdf_a
    
    @cdf_a.setter
    def cdf_a(self, cdf_a):
        self.__cdf_a = cdf_a
        
    @property
    def cdf_b(self):
        return self.__cdf_b
    
    @cdf_b.setter
    def cdf_b(self, cdf_b):
        self.__cdf_b = cdf_b
        
    """------------------------------------------------------------------------------------------------
    """ 
    def cdf(self, x):
        if(core.is_iterable(x)):
            if(np.where((x < self.a) | (x > self.b))[0].size > 0):
                raise exps.ArgumentOutOfRangeError()
            return self._cdf(x)
        else:
            if((x < self.a) or (x > self.b)):
                raise exps.ArgumentOutOfRangeError()
            return self._cdf(x)

    def _cdf(self, x):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def icdf(self, p):
        if(core.is_iterable(p)):
            if (np.where((p < self.cdf_a) | (p > self.cdf_b))[0].size > 0):
                raise exps.ArgumentOutOfRangeError()
            return self._icdf(p)
        else:
            if ((p < self.cdf_a) or (p > self.cdf_b)):
                raise exps.ArgumentOutOfRangeError()
            return self._icdf(p)

    def _icdf(self, p):
        raise exps.NotImplementedError()
                     
    """------------------------------------------------------------------------------------------------
    """   
    ndsize = 1024*1024

    def nd(self, size=ndsize, ll=None, ul=None, olNx=None):
        if((self.__nd is None) or (self.__nd.size != size)):
            if(olNx is None): olNx = 2
            if(np.isneginf(self.a) and np.isposinf(self.b)):
                ll = self.lolNx(Nx=olNx) if(ll is None) else ll
                ul = self.uolNx(Nx=olNx) if(ul is None) else ul
            elif(not np.isneginf(self.a) and np.isposinf(self.b)):
                ll = self.a if (ll is None) else ll
                ul = self.uolNx(Nx=olNx) if (ul is None) else ul
            elif(np.isneginf(self.a) and not np.isposinf(self.b)):
                ll = self.lolNx(Nx=olNx) if (ll is None) else ll
                ul = self.b if (ul is None) else ul
            else:
                ll = max(self.a, self.lolNx(Nx=olNx)) if (ll is None) else ll
                ul = min(self.uolNx(Nx=olNx), self.b) if (ul is None) else ul
            self.__nd = self._nd(size, ll, ul)
        return self.__nd
                 
    def _nd(self, size, ll, ul):
        rvs = self.rvs(size)
        rvs = np.asarray(rvs) if (size == 1) else rvs
        rvs = rvs[((ll <= rvs) & (rvs <= ul))]
        if(rvs.size < size):
            return np.hstack((rvs, self._nd(size-rvs.size, ll, ul)))
        else:
            return rvs[0] if (size == 1) else rvs

    """------------------------------------------------------------------------------------------------
    """
    ndrsize = 1024*1024

    def ndr(self, size=ndrsize, ll=None, ul=None, olNx=None):
        return self._ndr(size, ll, ul, olNx)
      
    def _ndr(self, size, ll, ul, olNx):
        if((self.__ndr is None) or (self.__ndr.size != size)):
            self.__ndr = np.random.permutation(self.nd(size, ll, ul, olNx))
        return self.__ndr

    """------------------------------------------------------------------------------------------------
    """
    def __call__(self, size=ndrsize, ll=None, ul=None, olNx=None):
        return self.ndr(size, ll, ul, olNx)

    """------------------------------------------------------------------------------------------------
    """   
    def rvs(self, size=1):
        return self._rvs(size)
      
    def _rvs(self, size):
        return self.icdf(self.cdf_a+(self.cdf_b-self.cdf_a)*np.random.rand(size))

    """------------------------------------------------------------------------------------------------
    """   
    def rv(self):
        return self._rv()
      
    def _rv(self):
        return self._rvs(1)[0]

    """------------------------------------------------------------------------------------------------
    """     
    def sf(self, x):
        return self._sf(x)
    
    def _sf(self, x):
        return 1.0 - self.cdf(x)
       
    def isf(self, p):
        return self._isf(p)
       
    def _isf(self, p):
        return self.icdf(1-p)
                             
    """------------------------------------------------------------------------------------------------
    """   
    def mean(self):
        return self._mean()
        
    def _mean(self):
        raise exps.NotImplementedError()

    def var(self):
        return self._var()
        
    def _var(self):
        raise exps.NotImplementedError()

    def stddev(self):
        return math.sqrt(self.var())
        
    def skew(self):
        return self._skew()
        
    def _skew(self):
        raise exps.NotImplementedError()
               
    def kurtosis(self):
        return self._kurtosis()
        
    def _kurtosis(self):
        raise exps.NotImplementedError()
 
            
    """------------------------------------------------------------------------------------------------
    """
    def percentile(self, p100):
        return self.icdf(p100/100)
        
    def Q1(self):
        return self.percentile(25)
            
    def Q2(self):
        return self.percentile(50)
        
    def Q3(self):
        return self.percentile(75)
        
    def IQR(self):
        return self.Q3()-self.Q1()
        
    def median(self):
        return self.percentile(50)


    """------------------------------------------------------------------------------------------------
    """
    def outliersNx_limits(self, Nx):
        p_25 = 25/100
        if (p_25 < self.cdf_a):
            Q1 = self.a
        else:
            Q1 = self._icdf(p_25)

        p_75 = 75/100
        if (p_75 > self.cdf_b):
            Q3 = self.b
        else:
            Q3 = self._icdf(p_75)

        IQR = Q3-Q1

        lol = Q1-Nx*1.5*IQR
        if(lol < self.a):
            lol = self.a

        uol = Q3+Nx*1.5*IQR
        if(uol > self.b):
            uol = self.b

        return (lol, uol)

    def is_outlierNx(self, x, Nx):
        x = np.asarray(x)
        (lol, uol) = self.outliersNx_limits(Nx)
        return ~((lol <= x) & (x <= uol))

    def lolNx(self, Nx):
        (lol, uol) = self.outliersNx_limits(Nx)
        return lol

    def uolNx(self, Nx):
        (lol, uol) = self.outliersNx_limits(Nx)
        return uol

    """------------------------------------------------------------------------------------------------
    """   
    def outliers_limits(self):
        return self.outliersNx_limits(Nx=1)

    def is_outlier(self, x):
        return self.is_outlierNx(x=x, Nx=1)

    def lol(self):
        (lol, uol) = self.outliers_limits()
        return lol

    def uol(self):
        (lol, uol) = self.outliers_limits()
        return uol

    """------------------------------------------------------------------------------------------------
    """
    def outliers2x_limits(self):
        return self.outliersNx_limits(Nx=2)

    def is_outlier2x(self, x):
        return self.is_outlierNx(x=x, Nx=2)

    def lol2x(self):
        (lol, uol) = self.outliers2x_limits()
        return lol

    def uol2x(self):
        (lol, uol) = self.outliers2x_limits()
        return uol

    """------------------------------------------------------------------------------------------------
    """
    def outliers4x_limits(self):
        return self.outliersNx_limits(Nx=4)

    def is_outlier4x(self, x):
        return self.is_outlierNx(x=x, Nx=4)

    def lol4x(self):
        (lol, uol) = self.outliers4x_limits()
        return lol

    def uol4x(self):
        (lol, uol) = self.outliers4x_limits()
        return uol

    """------------------------------------------------------------------------------------------------
    """
    def outliers8x_limits(self):
        return self.outliersNx_limits(Nx=8)

    def is_outlier8x(self, x):
        return self.is_outlierNx(x=x, Nx=8)

    def lol8x(self):
        (lol, uol) = self.outliers8x_limits()
        return lol

    def uol8x(self):
        (lol, uol) = self.outliers8x_limits()
        return uol


    """------------------------------------------------------------------------------------------------
    """
    class _distribution_on_chart(object):
        def __init__(self, distribution, distributionf, chart):
            self.__distribution = distribution
            self.__distributionf = distributionf
            self.__chart = chart

        def _get_xinterval(self, kwargs):
            ll = kwargs.pop('ll', None)
            ul = kwargs.pop('ul', None)
            olNx = kwargs.pop('olNx', 2)
            if(np.isneginf(self.__distribution.a) and np.isposinf(self.__distribution.b)):
                ll = self.__distribution.lolNx(Nx=olNx) if(ll is None) else ll
                ul = self.__distribution.uolNx(Nx=olNx) if(ul is None) else ul
            elif(not np.isneginf(self.__distribution.a) and np.isposinf(self.__distribution.b)):
                ll = self.__distribution.a if (ll is None) else ll
                ul = self.__distribution.uolNx(Nx=olNx) if (ul is None) else ul
            elif(np.isneginf(self.__distribution.a) and not np.isposinf(self.__distribution.b)):
                ll = self.__distribution.lolNx(Nx=olNx) if (ll is None) else ll
                ul = self.__distribution.b if (ul is None) else ul
            else:
                ll = self.__distribution.a if (ll is None) else ll
                ul = self.__distribution.b if (ul is None) else ul
            return (ll, ul)

        def _get_xrange(self, kwargs):
            raise exps.NotImplementedError()

        def plot(self, *args, **kwargs):
            xrange = self._get_xrange(kwargs)
            fxrange = self.__distributionf(xrange)
            self.__chart.plot(xrange, fxrange, *args, **kwargs)

        def fill(self, *args, **kwargs):
            xrange = self._get_xrange(kwargs)
            fxrange = self.__distributionf(xrange)
            self.__chart.fill_between(xrange, fxrange, *args, **kwargs)

        def bar(self, *args, **kwargs):
            xrange = self._get_xrange(kwargs)
            xrange_dx = np.diff(xrange)
            fxrange = self.__distributionf(xrange)
            align = kwargs.pop('align', None)
            if(align is None):
                align = 'center'
            self.__chart.bar(xrange[:-1]+xrange_dx/2.0, fxrange[:-1], xrange_dx, align=align, *args, **kwargs)

    def cdf_on_chart(self, chart):
        raise exps.NotImplementedError()
