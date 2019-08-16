import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
"""    
def test():
    mu = 1.0
    sigma2 = 0.5**2
    lognormal = stats.distributions.lognormal(mu, sigma2)

    figure = dv.Figure(size=(8, 8), grid=(2,1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    lognormal.cdf_on_chart(chart).plot()
    
    chart = dv.Chart2d(figure=figure, position=figure[1,0])
    lognormal.pdf_on_chart(chart).plot()

    figure.show()


"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()
    