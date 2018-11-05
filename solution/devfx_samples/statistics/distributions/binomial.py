import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
""" 
def test():
    n = 32
    p = 0.16
    binomial = stats.binomial(n, p)

    figure = dv.Figure(size=(8, 8), grid=(2, 1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    stats.cdhistogram.from_distribution(binomial, ll=0, ul=n, bin_count=n).on_chart(chart).bar()

    chart = dv.Chart2d(figure=figure, position=figure[1,0])
    stats.dhistogram.from_distribution(binomial, ll=0, ul=n, bin_count=n).on_chart(chart).bar()

    figure.show()

"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()

