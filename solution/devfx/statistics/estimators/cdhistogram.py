import numpy as np
import devfx.exceptions as exceps
import devfx.mathematics as math
from ..distributions import distribution

"""------------------------------------------------------------------------------------------------
"""
class cdhistogram(object):
    def __init__(self, a, b, cfreq):
        self.cfreq = np.array(cfreq)
        self.size = self.cfreq.size
        self.a = a
        self.b = b
        self.dx = (self.b-self.a)/self.cfreq.size
        self.xbin_edges = np.hstack(([(self.a+i*self.dx) for i in math.range(0, self.cfreq.size)], self.b))
        self.x = self.xbin_edges[:-1]+self.dx/2.0
        self.x_min = math.min(self.x)
        self.x_max = math.max(self.x)
        self.a_x_b = np.hstack((self.a, self.x, self.b))

    def normalize(self):
        self.cfreq = self.cfreq/self.cfreq[-1]

    def __call__(self, x):
        if (x < self.a):
            raise exceps.ArgumentOutOfRangeError()
        elif (x > self.b):
            raise exceps.ArgumentOutOfRangeError()
        else:
            return self.cfreq[np.searchsorted(self.xbin_edges[:-1], x)]


    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def from_data(cls, data, ll=None, ul=None, bin_count=None, dx=None, density=True):
        data = np.asarray(data)

        if (ll is None):
            ll = math.min(data)
        if (ul is None):
            ul = math.max(data)

        if ((bin_count is None) and (dx is None)):
            bins = int(math.min([math.ceil(math.sqrrt(data.size)), 64]))
        elif ((bin_count is None) and (dx is not None)):
            bins = int(math.ceil((ul-ll)/dx))
        elif ((bin_count is not None) and (dx is None)):
            bins = int(bin_count)
        else:
            raise exceps.NotSupportedError()

        (freq, bin_edges) = np.histogram(data, range=(ll, ul), bins=bins, density=density)

        histogram = cdhistogram(a=ll,
                                b=ul,
                                cfreq=math.csum(((ul-ll)/freq.size)*freq))
        return histogram

    @classmethod
    def from_distribution(cls, d, size=distribution.ndsize, ll=None, ul=None, olNx=None, bin_count=None, dx=None):
        data = d.nd(size=size, ll=ll, ul=ul, olNx=olNx)
        return cdhistogram.from_data(data, ll=ll, ul=ul, bin_count=bin_count, dx=dx)

    @classmethod
    def from_dhistogram(cls, dhistogram):
        histogram = cdhistogram(a=dhistogram.a,
                                b=dhistogram.b,
                                cfreq=math.csum(dhistogram.dx*dhistogram.freq))
        return histogram

    """------------------------------------------------------------------------------------------------
    """
    class _cdhistogram_on_chart(object):
        def __init__(self, cdhistogram, chart):
            self.__cdhistogram = cdhistogram
            self.__chart = chart

        def plot(self, *args, **kwargs):
            self.__chart.plot(self.__cdhistogram.x, self.__cdhistogram.cfreq, *args, **kwargs)

        def fill(self, *args, **kwargs):
            self.__chart.fill_between(self.__cdhistogram.x, self.__cdhistogram.cfreq, *args, **kwargs)

        def bar(self, *args, **kwargs):
            align = kwargs.pop('align', None)
            if (align is None):
                align = 'center'
            self.__chart.bar(left=self.__cdhistogram.x, height=self.__cdhistogram.cfreq, width=self.__cdhistogram.dx, align=align, *args, **kwargs)

    def on_chart(self, chart):
        return cdhistogram._cdhistogram_on_chart(self, chart)