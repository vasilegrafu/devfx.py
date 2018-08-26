import devfx.statistics as stats

"""------------------------------------------------------------------------------------------------
"""       
def test():
    mu = 2.0
    sigma = 2.0
    def compute():
        data = stats.normal(mu, sigma).rvs(64)
        (thetaL, thetaU) = stats.pi.mean.normal(data).two_sided()
        return (thetaL, thetaU)
          
    N = 1024*1024
    n = 0
    i = 1
    while(i <= N):
        (thetaL, thetaU) = compute()
        data = stats.normal(mu, sigma).rvs(1)
        if(thetaL <= data <= thetaU):
            n+=1
        print(i, n/i)
        i+=1


"""------------------------------------------------------------------------------------------------
"""  
if __name__ == '__main__':
    test()
