import numpy as np
from .pvalue import pvalue as pvalue_module

class htest(object):
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


            def two_tailed(self, mu0, sigma0=None, scoef=5):
                alpha = scoef/100.0
                (n, mean, S, cv, pvalue) = pvalue_module.mean.normal(self.data).two_tailed(mu0, sigma0)
                if (pvalue <= alpha):
                    rejectH0 = True
                else:
                    rejectH0 = False
                return (n, mean, S, cv, pvalue, alpha, rejectH0)

            def lower_tailed(self, mu0, sigma0=None, scoef=5):
                alpha = scoef/100.0
                (n, mean, S, cv, pvalue) = pvalue_module.mean.normal(self.data).lower_tailed(mu0, sigma0)
                if (pvalue <= alpha):
                    rejectH0 = True
                else:
                    rejectH0 = False
                return (n, mean, S, cv, pvalue, alpha, rejectH0)

            def upper_tailed(self, mu0, sigma0=None, scoef=5):
                alpha = scoef/100.0
                (n, mean, S, cv, pvalue) = pvalue_module.mean.normal(self.data).upper_tailed(mu0, sigma0)
                if (pvalue <= alpha):
                    rejectH0 = True
                else:
                    rejectH0 = False
                return (n, mean, S, cv, pvalue, alpha, rejectH0)

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

