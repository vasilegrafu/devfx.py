import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
""" 
def test_empirical():
    normal = stats.distributions.normal(mu=0.0, sigma=1.0)
    empirical = stats.distributions.empirical(normal.ndr(size=1024*1024))

    figure = dv.Figure(size=(8, 8), grid=(2,1))

    chart = dv.Chart2d(figure=figure, position=figure.grid[0,0])
    dhistogram = stats.estimators.dhistogram.from_distribution(empirical)
    dhistogram.on_chart(chart).bar()
    dhistogram.on_chart(chart).plot('r')

    chart = dv.Chart2d(figure=figure, position=figure.grid[1,0])
    cdhistogram = stats.estimators.cdhistogram.from_distribution(empirical)
    cdhistogram.on_chart(chart).bar()
    cdhistogram.on_chart(chart).plot('r')

    figure.show()

"""------------------------------------------------------------------------------------------------
""" 
def test():  
    test_empirical()

"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()

    