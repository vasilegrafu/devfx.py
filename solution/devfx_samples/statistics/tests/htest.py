import devfx.math as math
import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv
    
"""------------------------------------------------------------------------------------------------
"""       
def test_htest():
    # Initial we have a teortical distribution which we ssume it is correct
    mu0 = 8.0
    sigma0 = 2.0

    # For this example we generate some data, but this data is our new data which we want to test against theortical assumptions
    mu = 8.5
    sigma = sigma0
    data = stats.distributions.normal(mu, sigma).rvs(256)

    (n, mean, S, cv, pvalue, alpha, rejectH0) = stats.tests.htest.mean.normal(data).upper_tailed(mu0, sigma0)
    print((n, mean, S, cv, pvalue, alpha, rejectH0))
    
"""------------------------------------------------------------------------------------------------
"""       
def test():
    test_htest()

"""------------------------------------------------------------------------------------------------
"""  
if __name__ == '__main__':
    test()


