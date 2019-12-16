import numpy as np
import scipy as sp
import scipy.stats
import scipy.interpolate
import sklearn as skl
import sklearn.neighbors
import statsmodels as sm
import statsmodels.nonparametric.kernel_density
import devfx.math as math
from .dcontinuous import dcontinuous

""" - normal_reference: normal reference rule of thumb (default)
    - cv_ml: cross validation maximum likelihood
    - cv_ls: cross validation least squares
"""
""" Valid kernels are:
    - 'gaussian'
    - 'tophat'
    - 'epanechnikov'
    - 'exponential'
    - 'linear'
    - 'cosine']
"""
class kde(dcontinuous):
    def __init__(self, data, n=1024, kernel='gaussian', bandwidth='cv_ls'):
        self.__data = np.asarray(data)
        a = math.min(self.__data)
        b = math.max(self.__data)

        kernel = kernel
        bandwidth = sm.nonparametric.kernel_density.KDEMultivariate(self.__data, var_type='c', bw=bandwidth).bw

        self.__distribution = skl.neighbors.KernelDensity(kernel=kernel, bandwidth=bandwidth)
        self.__distribution.fit(self.__data[:, np.newaxis])

        __x = np.linspace(a, b, n)
        __dx = (b-a)/n

        __pdf = np.exp(self.__distribution.score_samples(__x[:, np.newaxis]))
        self.__x_pdf = sp.interpolate.interp1d(__x, __pdf)

        __cdf = math.csum(__pdf*__dx)
        self.__x_cdf = sp.interpolate.interp1d(__x, __cdf)
        self.__cdf_x = sp.interpolate.interp1d(__cdf, __x)

        super().__init__(a=a, b=b)

    """------------------------------------------------------------------------------------------------
    """

    def _cdf(self, x):
        return self.__x_cdf(x)

    def _icdf(self, p):
        return self.__cdf_x(p)

    """------------------------------------------------------------------------------------------------
    """
    def _pdf(self, x):
        return self.__x_pdf(x)

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




