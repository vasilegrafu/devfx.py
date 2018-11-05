import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
"""    
def test_cdf():
    figure = dv.Figure(size=(8, 8), grid=(4,1))

    mu = 0.0
    sigma = 0.5
    chart = dv.Chart2d(figure, position=figure[0,0], ylim=(0.0, 1.0))
    stats.normal(mu, sigma).cdf_on_chart(chart).plot()

    mu = 0.5
    sigma = 0.5
    chart = dv.Chart2d(figure, position=figure[1,0], ylim=(0.0, 1.0))
    stats.normal(mu, sigma).cdf_on_chart(chart).plot()

    mu = 1.0
    sigma = 1.0
    chart = dv.Chart2d(figure, position=figure[2,0], ylim=(0.0, 1.0))
    stats.normal(mu, sigma).cdf_on_chart(chart).plot()

    mu = 2.0
    sigma = 2.0
    chart = dv.Chart2d(figure, position=figure[3,0], ylim=(0.0, 1.0))
    stats.normal(mu, sigma).cdf_on_chart(chart).plot()

    figure.show()

"""------------------------------------------------------------------------------------------------
"""     
def test_pdf():
    figure = dv.Figure(size=(8, 8), grid=(4, 1))

    mu = 0.0
    sigma = 0.5
    chart = dv.Chart2d(figure, position=figure[0,0], ylim=(0.0, 1.0))
    stats.normal(mu, sigma).pdf_on_chart(chart).plot()

    mu = 0.5
    sigma = 0.5
    chart = dv.Chart2d(figure, position=figure[1,0], ylim=(0.0, 1.0))
    stats.normal(mu, sigma).pdf_on_chart(chart).plot()

    mu = 1.0
    sigma = 1.0
    chart = dv.Chart2d(figure, position=figure[2,0], ylim=(0.0, 1.0))
    stats.normal(mu, sigma).pdf_on_chart(chart).plot()

    mu = 2.0
    sigma = 2.0
    chart = dv.Chart2d(figure, position=figure[3,0], ylim=(0.0, 1.0))
    stats.normal(mu, sigma).pdf_on_chart(chart).plot()

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
    