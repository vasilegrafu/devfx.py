import numpy as np
import devfx.exceptions as exceps
import devfx.mathematics as math
from .. import distributions

"""------------------------------------------------------------------------------------------------
"""
class dhistogram(object):
    def __init__(self, a, b, freq):
        self.freq = np.array(freq)
        self.size = self.freq.size
        self.a = a
        self.b = b
        self.dx = (self.b-self.a)/self.freq.size
        self.xbin_edges = np.hstack(([(self.a+i*self.dx) for i in math.range(0, self.freq.size)], self.b))
        self.x = self.xbin_edges[:-1]+self.dx/2.0
        self.x_min = math.min(self.x)
        self.x_max = math.max(self.x)
        self.a_x_b = np.hstack((self.a, self.x, self.b))

    def normalize(self):
        self.freq=(1.0/self.dx)*((self.dx*self.freq)/math.sum(self.dx*self.freq))

    def __call__(self, x):
        if (x < self.a):
            raise exceps.ArgumentOutOfRangeError()
        elif (x > self.b):
            raise exceps.ArgumentOutOfRangeError()
        else:
            return self.freq[np.searchsorted(self.xbin_edges[:-1], x)]


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
            bins = int(math.min([math.ceil(math.sqrt(data.size)), 64]))
        elif ((bin_count is None) and (dx is not None)):
            bins = int(math.ceil((ul-ll)/dx))
        elif ((bin_count is not None) and (dx is None)):
            bins = int(bin_count)
        else:
            raise exceps.NotSupportedError()

        (freq, bin_edges) = np.histogram(data, range=(ll, ul), bins=bins, density=density)

        histogram = dhistogram(a=ll,
                               b=ul,
                               freq=freq)
        return histogram

    @classmethod
    def from_distribution(cls, d, size=distributions.distribution.ndsize, ll=None, ul=None, olNx=None, bin_count=None, dx=None):
        data = d.nd(size=size, ll=ll, ul=ul, olNx=olNx)
        return dhistogram.from_data(data, ll=ll, ul=ul, bin_count=bin_count, dx=dx)

    @classmethod
    def from_cdhistogram(cls, cdhistogram):
        histogram = dhistogram(a=cdhistogram.a,
                               b=cdhistogram.b,
                               freq=(1.0/cdhistogram.dx)*math.diff(np.hstack((0, cdhistogram.cfreq))))
        return histogram


    """------------------------------------------------------------------------------------------------
    """
    class _dhistogram_on_chart(object):
        def __init__(self, dhistogram, chart):
            self.__dhistogram = dhistogram
            self.__chart = chart

        def plot(self, *args, **kwargs):
            self.__chart.plot(self.__dhistogram.x, self.__dhistogram.freq, *args, **kwargs)

        def fill(self, *args, **kwargs):
            self.__chart.fill_between(self.__dhistogram.x, self.__dhistogram.freq, *args, **kwargs)

        def bar(self, *args, **kwargs):
            align = kwargs.pop('align', None)
            if (align is None):
                align = 'center'
            self.__chart.bar(x=self.__dhistogram.x, height=self.__dhistogram.freq, width=self.__dhistogram.dx, align=align, *args, **kwargs)

    def on_chart(self, chart):
        return dhistogram._dhistogram_on_chart(self, chart)




