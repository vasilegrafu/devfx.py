import numpy as np
import devfx.mathematics as math
from .. import distributions
from .. import series

""" Predictions intervals
"""
class pi(object):
    """================================================================================================
    """
    class mean(object):
        """------------------------------------------------------------------------------------------------
        """
        class normal(object):
            def __init__(self, data):
                self.data = np.asarray(data)

            @property
            def data(self):
                return self.__data

            @data.setter
            def data(self, data):
                self.__data = data


            def two_sided(self, ccoef=95, sigma=None):
                n = self.data.size
                mean = series.mean(self.data)
                alpha = 1.0-ccoef/100.0
                if(sigma is not None):
                    d = distributions.normal().icdf(1.0-alpha/2.0)
                    thetaL = mean-d*sigma*math.sqrt(1.0+1.0/n)
                    thetaU = mean+d*sigma*math.sqrt(1.0+1.0/n)
                else:
                    d = distributions.student(n-1).icdf(1.0-alpha/2.0)
                    S = series.stddev(self.data)
                    thetaL = mean-d*S*math.sqrt(1.0+1.0/n)
                    thetaU = mean+d*S*math.sqrt(1.0+1.0/n)
                return (thetaL, thetaU)

            def lower_one_sided(self, ccoef=95, sigma=None):
                n = self.data.size
                mean = series.mean(self.data)
                alpha = 1.0 - ccoef/100.0
                if(sigma is not None):
                    d = distributions.normal().icdf(1.0-alpha)
                    thetaL = mean-d*sigma*math.sqrt(1.0+1.0/n)
                    thetaU = +math.inf
                else:
                    d = distributions.student(n-1).icdf(1.0-alpha)
                    S = series.stddev(self.data)
                    thetaL = mean-d*S*math.sqrt(1.0+1.0/n)
                    thetaU = +math.inf
                return (thetaL, thetaU)

            def upper_one_sided(self, ccoef=95, sigma=None):
                n = self.data.size
                mean = series.mean(self.data)
                alpha = 1.0-ccoef/100.0
                if(sigma is not None):
                    d = distributions.normal().icdf(1.0-alpha)
                    thetaL = -math.inf
                    thetaU = mean+d*sigma*math.sqrt(1.0+1.0/n)
                else:
                    d = distributions.student(n-1).icdf(1.0-alpha)
                    S = series.stddev(self.data)
                    thetaL = -math.inf
                    thetaU = mean+d*S*math.sqrt(1.0+1.0/n)
                return (thetaL, thetaU)

        """--------------------------------------------------------------------------------------------
        """
        class unknown(normal):
            def __init__(self, data):
                super().__init__(data)


    """================================================================================================
    """
    class mean_difference(object):
        pass


    """================================================================================================
    """
    class variance(object):
        pass


    """================================================================================================
    """
    class variance_ratio(object):
        pass

