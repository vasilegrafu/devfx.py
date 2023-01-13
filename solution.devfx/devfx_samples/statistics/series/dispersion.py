import numpy as np
import devfx.statistics as stats

"""------------------------------------------------------------------------------------------------
"""       
def test():
    mu = 0.0
    sigma = 1.0
    normal = stats.distributions.normal(mu, sigma)

    data = []
    data.append(np.hstack((normal.rvs(1024), [50])))
    data.append(np.hstack((normal.rvs(1024), [50])))
    data = np.asarray(data)
    
    # outliers_limits
    (lol, uol) = stats.series.outliers_limits(data[0])
    print(lol, uol)
    print(stats.series.outliers_limits(data[0]))
    print(stats.series.is_outlier(data[0], [50]))

    (lol, uol) = stats.series.outliers2x_limits(data[1])
    print(lol, uol)
    print(stats.series.outliers2x_limits(data[1]))
    print(stats.series.is_outlier2x(data[0], [50]))

    
"""------------------------------------------------------------------------------------------------
"""  
if __name__ == '__main__':
    test()
    