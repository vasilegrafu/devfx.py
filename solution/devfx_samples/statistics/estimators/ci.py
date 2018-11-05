import devfx.statistics as stats

"""------------------------------------------------------------------------------------------------
"""       
def test_mean():
    mu = 2.0
    sigma = 2.0
    def compute():
        data = stats.normal(mu, sigma).rvs(64)
        (thetaL, thetaU) = stats.ci.mean.normal(data).two_sided(ccoef=95)
        return (thetaL, thetaU)
        
    N = 1024*1024
    n = 0
    i = 1
    while(i <= N):
        (thetaL, thetaU) = compute()
        if(thetaL <= mu <= thetaU):
            n+=1
        print(i, n/i)
        i+=1


"""------------------------------------------------------------------------------------------------
"""       
def test_mean_difference():
    mu1 = 2.0
    sigma1 = 2.0
    mu2 = 1.0
    sigma2 = 2.0
    def compute():
        data1 = stats.normal(mu1, sigma1).rvs(64)
        data2 = stats.normal(mu2, sigma2).rvs(64)
        (thetaL, thetaU) = stats.ci.mean_difference.normal(data1, data2).two_sided()
        return (thetaL, thetaU)
        
    N = 1024*1024
    n = 0
    i = 1
    while(i <= N):
        (thetaL, thetaU) = compute()
        if(thetaL <= (mu1-mu2) <= thetaU):
            n+=1
        print(i, n/i)
        i+=1


"""------------------------------------------------------------------------------------------------
"""    
def test_variance():
    mu = 2.0
    sigma = 2.0
    def compute():
        data = stats.normal(mu, sigma).rvs(64)
        (thetaL, thetaU) = stats.ci.variance.normal(data).upper_one_sided(ccoef=75)
        return (thetaL, thetaU)
        
    N = 1024*1024
    n = 0
    i = 1
    while(i <= N):
        (thetaL, thetaU) = compute()
        if(thetaL <= sigma**2 <= thetaU):
            n+=1
        print(i, n/i)
        i+=1


"""------------------------------------------------------------------------------------------------
"""       
def test():
    test_mean()
    # test_mean_difference()
    # test_variance()

"""------------------------------------------------------------------------------------------------
"""  
if __name__ == '__main__':
    test()
    