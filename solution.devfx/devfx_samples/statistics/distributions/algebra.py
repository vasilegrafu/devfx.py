import devfx.diagnostics as dgn
import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
def test_algebra1():
    N1 = stats.distributions.normal(mu=2.0, sigma=1.0)
    N2 = stats.distributions.normal(mu=2.0, sigma=1.0)
    N3 = stats.distributions.normal(mu=2.0, sigma=1.0)
    N4 = stats.distributions.normal(mu=2.0, sigma=1.0)

    sw = dgn.Stopwatch().start()

    Y = N1 + N2 ** 2
    E = stats.distributions.empirical(Y.sample())

    print("time elapsed: ", sw.stop().elapsed)

    figure = dv.Figure(size=(8, 8), grid=(3, 1))

    chart = dv.Chart2d(figure=figure, position=figure.grid[0,0])
    stats.estimators.dhistogram.from_distribution(N1).on_chart(chart).bar()

    chart = dv.Chart2d(figure=figure, position=figure.grid[1,0])
    stats.estimators.dhistogram.from_distribution(N2).on_chart(chart).bar()

    chart = dv.Chart2d(figure=figure, position=figure.grid[2,0])
    stats.estimators.dhistogram.from_distribution(E).on_chart(chart).bar()
    stats.estimators.dhistogram.from_distribution(E).on_chart(chart).plot('r')

    figure.show()


"""------------------------------------------------------------------------------------------------
""" 
def test_algebra2():
    dL = stats.distributions.uniform(a=1.0, b=3.0)
    L0 = stats.distributions.uniform(a=9.0, b=11.0)
    dT = stats.distributions.normal(mu=1.0, sigma=1.0)

    sw = dgn.Stopwatch().start()

    K = dL/(L0*dT)

    KD = stats.distributions.empirical(K.sample())

    print("time elapsed: ", sw.stop().elapsed)

    figure = dv.Figure(size=(8, 8), grid=(2, 1))

    chart = dv.Chart2d(figure=figure, position=figure.grid[0,0])
    stats.estimators.dhistogram.from_distribution(KD, ll=-2, ul=2, bin_count=256).on_chart(chart).plot()

    chart = dv.Chart2d(figure=figure, position=figure.grid[1,0])
    stats.estimators.cdhistogram.from_distribution(KD, ll=-2, ul=2, bin_count=256).on_chart(chart).plot()

    figure.show()


"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test_algebra1()
    test_algebra2()
