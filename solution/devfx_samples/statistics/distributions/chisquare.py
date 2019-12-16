import devfx.math as math
import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
"""    
def test():
    n_max = 8
    n_range = math.range(1, n_max+1)

    figure = dv.Figure(size=(8, 8), grid=(2, 1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0], ylim=(0.0, 0.5))
    for n in n_range:
        stats.distributions.chisquare(n).pdf_on_chart(chart).plot()

    chart = dv.Chart2d(figure=figure, position=figure[1,0], ylim=(0.0, 1.0))
    for n in n_range:
        stats.distributions.chisquare(n).cdf_on_chart(chart).plot()

    figure.show()
     

"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()
    