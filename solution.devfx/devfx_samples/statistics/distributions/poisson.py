import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
def test_cdf():
    figure = dv.Figure(size=(8, 8), grid=(4, 1))

    rate = 2.0
    chart = dv.Chart2d(figure, position=figure[0,0])
    stats.distributions.poisson(rate).cdf_on_chart(chart).plot(ll=0, ul=40)

    rate = 4.0
    chart = dv.Chart2d(figure, position=figure[1,0])
    stats.distributions.poisson(rate).cdf_on_chart(chart).plot(ll=0, ul=40)

    rate = 8.0
    chart = dv.Chart2d(figure, position=figure[2,0])
    stats.distributions.poisson(rate).cdf_on_chart(chart).plot(ll=0, ul=40)

    rate = 16.0
    chart = dv.Chart2d(figure, position=figure[3,0])
    stats.distributions.poisson(rate).cdf_on_chart(chart).plot(ll=0, ul=40)

    figure.show()


"""------------------------------------------------------------------------------------------------
"""
def test_pmf():
    figure = dv.Figure(size=(8, 8), grid=(4, 1))

    rate = 2.0
    chart = dv.Chart2d(figure, position=figure[0,0])
    stats.distributions.poisson(rate).pmf_on_chart(chart).bar(ll=0, ul=40)

    rate = 4.0
    chart = dv.Chart2d(figure, position=figure[1,0])
    stats.distributions.poisson(rate).pmf_on_chart(chart).bar(ll=0, ul=40)

    rate = 8.0
    chart = dv.Chart2d(figure, position=figure[2,0])
    stats.distributions.poisson(rate).pmf_on_chart(chart).bar(ll=0, ul=40)

    rate = 16.0
    chart = dv.Chart2d(figure, position=figure[3,0])
    stats.distributions.poisson(rate).pmf_on_chart(chart).bar(ll=0, ul=40)

    figure.show()


"""------------------------------------------------------------------------------------------------
"""


def test():
    test_cdf()
    test_pmf()


"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test()
