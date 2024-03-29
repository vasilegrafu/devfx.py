import devfx.math as math
import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
""" 
def test():
    # ----------------------------------------------------------------
    def poisson(rate):
        return stats.distributions.ddiscrete_builder(
            cdf=None,
            pmf=lambda x: math.expe(-rate)*rate**x/math.nF(x),
            a=0,
            b=+math.inf)

    #----------------------------------------------------------------
    def chart_cdf(figure, rate, position):
        chart = dv.Chart2d(figure=figure, position=position)
        poisson(rate).cdf_on_chart(chart).plot()

    figure = dv.Figure(size=(8, 8), grid=(4, 1))

    chart_cdf(figure, 2.0, position=figure.grid[0,0])
    chart_cdf(figure, 4.0, position=figure.grid[1,0])
    chart_cdf(figure, 8.0, position=figure.grid[2,0])
    chart_cdf(figure, 16.0, position=figure.grid[3,0])

    figure.show()

    # ----------------------------------------------------------------
    def chart_pmf(figure, rate, position):
        chart = dv.Chart2d(figure=figure, position=position)
        poisson(rate=rate).pmf_on_chart(chart).bar(ll=0, ul=40)
    
    figure = dv.Figure(size=(8, 8), grid=(4, 1))

    chart_pmf(figure, 2.0, position=figure.grid[0,0])
    chart_pmf(figure, 4.0, position=figure.grid[1,0])
    chart_pmf(figure, 8.0, position=figure.grid[2,0])
    chart_pmf(figure, 16.0, position=figure.grid[3,0])

    figure.show()

"""------------------------------------------------------------------------------------------------
""" 
if __name__ == '__main__':
    test()