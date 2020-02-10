import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""       
def test_pvalue():
    # Initial we have a teortical distribution which we ssume it is correct
    mu0 = 8.0
    sigma0 = 2.0

    # For this example we generate some data, but this data is our new data which we want to test against theortical assumptions
    mu = 8.5
    sigma = sigma0
    data = stats.distributions.normal(mu, sigma).rvs(256)

    # The p-value associated with an observed test statistic is the
    # probability of getting a value for that test statistic as extreme as or more
    # extreme than what was actually observed (relative to H1) given that H0 is true.
    (n, mu, S, cv, pvalue) = stats.tests.pvalue.mean.normal(data).upper_tailed(mu0, sigma0)
    print((n, mu, S, cv, pvalue))

    figure = dv.Figure((8, 4))

    chart = dv.Chart2d(figure, position=(1, 1, 1))
    stats.distributions.normal(0, 1).pdf_on_chart(chart).plot(olNx=2, color='green')
    chart.yline(cv, color='green')

    figure.show()

    # figure = dv.figure((8, 4))
    #
    # chart = dv.chart2d(figure, position=(1, 1, 1))
    #
    # stats.distributions.normal(mu0, sigma0).pdf_on_chart(chart).plot(olNx=1, color='green')
    # chart.axvline(mu0, color='green')
    #
    # stats.distributions.normal(mu, sigma).pdf_on_chart(chart).plot(olNx=1, color='red')
    # chart.axvline(mu, color='red')
    #
    # dv.figures.show()


    
"""------------------------------------------------------------------------------------------------
"""       
def test():
    test_pvalue()

"""------------------------------------------------------------------------------------------------
"""  
if __name__ == '__main__':
    test()
    