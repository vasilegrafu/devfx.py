import devfx.mathematics as math
import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
"""
def test_cdf():
    rate_max = 4
    rate_range = math.range(1, rate_max + 1)

    figure = dv.Figure(size=(8, 12), grid=(4,1))

    n = 1.0
    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    for rate in rate_range:
        stats.distributions.erlang(n, rate).cdf_on_chart(chart).plot()

    n = 1.5
    chart = dv.Chart2d(figure=figure, position=figure[1,0])
    for rate in rate_range:
        stats.distributions.erlang(n, rate).cdf_on_chart(chart).plot()

    n = 2.0
    chart = dv.Chart2d(figure=figure, position=figure[2,0])
    for rate in rate_range:
        stats.distributions.erlang(n, rate).cdf_on_chart(chart).plot()

    n = 4.0
    chart = dv.Chart2d(figure=figure, position=figure[3,0])
    for rate in rate_range:
        stats.distributions.erlang(n, rate).cdf_on_chart(chart).plot()

    figure.show()


"""------------------------------------------------------------------------------------------------
"""
def test_pdf():
    rate_max = 4
    rate_range = math.range(1, rate_max + 1)

    figure = dv.Figure(size=(8, 12), grid=(4,1))

    n = 1.0
    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    for rate in rate_range:
        stats.distributions.erlang(n, rate).pdf_on_chart(chart).plot()

    n = 1.5
    chart = dv.Chart2d(figure=figure, position=figure[1,0])
    for rate in rate_range:
        stats.distributions.erlang(n, rate).pdf_on_chart(chart).plot()

    n = 2.0
    chart = dv.Chart2d(figure=figure, position=figure[2,0])
    for rate in rate_range:
        stats.distributions.erlang(n, rate).pdf_on_chart(chart).plot()

    n = 4.0
    chart = dv.Chart2d(figure=figure, position=figure[3,0])
    for rate in rate_range:
        stats.distributions.erlang(n, rate).pdf_on_chart(chart).plot()

    figure.show()


"""------------------------------------------------------------------------------------------------
"""
def test():
    test_cdf()
    test_pdf()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test()
