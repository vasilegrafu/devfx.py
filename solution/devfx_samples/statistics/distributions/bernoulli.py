import devfx.statistics as stats

"""------------------------------------------------------------------------------------------------
""" 
def test():
    p = 0.25

    print(stats.bernoulli(p).pmf(1))
    print(stats.bernoulli(p).pmf(0))

    print(stats.bernoulli(p).cdf(1))
    print(stats.bernoulli(p).cdf(0))

"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()
    
