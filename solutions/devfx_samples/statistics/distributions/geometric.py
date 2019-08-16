import devfx.mathematics as math
import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
"""
def test_GeometricK1Distribution():
    p_range = math.range(0.16, 0.64, 0.08)

    figure = dv.Figure(size=(8, 8), grid=(2,1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    for p in p_range:
        stats.distributions.geometrick1(p).cdf_on_chart(chart).plot()

    chart = dv.Chart2d(figure=figure, position=figure[1,0])
    for p in p_range:
        stats.distributions.geometrick1(p).pmf_on_chart(chart).plot()

    figure.show()


"""------------------------------------------------------------------------------------------------
"""
def test_GeometricK0Distribution():
    p_range = math.range(0.16, 0.64, 0.08)

    figure = dv.Figure(size=(8, 8), grid=(2,1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    for p in p_range:
        stats.distributions.geometrick0(p).cdf_on_chart(chart).plot()

    chart = dv.Chart2d(figure=figure, position=figure[1,0])
    for p in p_range:
        stats.distributions.geometrick0(p).pmf_on_chart(chart).plot()

    figure.show()


"""------------------------------------------------------------------------------------------------
"""
def test():
    test_GeometricK1Distribution()
    test_GeometricK0Distribution()


"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test()


