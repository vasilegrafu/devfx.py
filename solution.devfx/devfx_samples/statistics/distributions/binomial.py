import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
""" 
def test():
    n = 32
    p = 0.16
    binomial = stats.distributions.binomial(n, p)

    figure = dv.Figure(size=(8, 8), grid=(2, 1))

    chart = dv.Chart2d(figure=figure, position=figure.grid[0,0])
    stats.estimators.cdhistogram.from_distribution(binomial, ll=0, ul=n, bin_count=n).on_chart(chart).bar()

    chart = dv.Chart2d(figure=figure, position=figure.grid[1,0])
    stats.estimators.dhistogram.from_distribution(binomial, ll=0, ul=n, bin_count=n).on_chart(chart).bar()

    figure.show()

"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()

