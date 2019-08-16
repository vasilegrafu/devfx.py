import numpy as np
import devfx.mathematics as math
from ..distributions import normal, student
from ..series import center, dispersion

class pvalue(object):
    """================================================================================================
    """
    class mean(object):
        """--------------------------------------------------------------------------------------------
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


            def two_tailed(self, mu0, sigma0=None):
                n = self.data.size
                mean = center.mean(self.data)
                S = dispersion.stddev(self.data)
                if (sigma0 is not None):
                    cv = math.abs((mean-mu0)/(sigma0/math.sqrt(n)))
                    pvalue = normal().cdf(-cv)+(1.0-normal().cdf(cv))
                else:
                    cv = math.abs((mean-mu0)/(S/math.sqrt(n)))
                    pvalue = student(n-1).cdf(-cv) + (1.0-student(n-1).cdf(cv))
                return (n, mean, S, cv, pvalue)

            def lower_tailed(self, mu0, sigma0=None):
                n = self.data.size
                mean = center.mean(self.data)
                S = dispersion.stddev(self.data)
                if (sigma0 is not None):
                    cv = (mean-mu0)/(sigma0/math.sqrt(n))
                    pvalue = normal().cdf(cv)
                else:
                    cv = (mean-mu0)/(S/math.sqrt(n))
                    pvalue = student(n-1).cdf(cv)
                return (n, mean, S, cv, pvalue)

            def upper_tailed(self, mu0, sigma0=None):
                n = self.data.size
                mean = center.mean(self.data)
                S = dispersion.stddev(self.data)
                if (sigma0 is not None):
                    cv = (mean-mu0)/(sigma0/math.sqrt(n))
                    pvalue = 1.0-normal().cdf(cv)
                else:
                    cv = (mean-mu0)/(S/math.sqrt(n))
                    pvalue = 1.0-student(n-1).cdf(cv)
                return (n, mean, S, cv, pvalue)

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

