import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
"""    
def test():
    figure = dv.Figure((8, 12), grid=(4,1))
   
    chart = dv.Chart2d(figure=figure, position=figure[0,0], ylim=(0.0, 1.0))
    mu = 1.0
    s = 1.0
    stats.distributions.logistic(mu, s).cdf_on_chart(chart).plot()
    mu = 1.0
    s = 2.0
    stats.distributions.logistic(mu, s).cdf_on_chart(chart).plot()
    
    chart = dv.Chart2d(figure=figure, position=figure[1,0], ylim=(0.0, 1.0))
    mu = 1.0
    s = 1.0
    stats.distributions.logistic(mu, s).cdf_on_chart(chart).plot()
    mu = 2.0
    s = 1.0
    stats.distributions.logistic(mu, s).cdf_on_chart(chart).plot()

    chart = dv.Chart2d(figure=figure, position=figure[2,0], ylim=(0.0, 1.0))
    mu = 1.0
    s = 1.0
    stats.distributions.logistic(mu, s).cdf_on_chart(chart).plot()
    mu = 1.0
    s = 2.0
    stats.distributions.logistic(mu, s).cdf_on_chart(chart).plot()
    
    chart = dv.Chart2d(figure=figure, position=figure[3,0], ylim=(0.0, 1.0))
    mu = 1.0
    s = 1.0
    stats.distributions.logistic(mu, s).cdf_on_chart(chart).plot()
    mu = 2.0
    s = 1.0
    stats.distributions.logistic(mu, s).cdf_on_chart(chart).plot()

    figure.show()
        

"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()
    