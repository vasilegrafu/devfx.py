import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
""" 
def test():
    alpha = 0.7
    beta = 0.6
    a=0.0
    b=1.0

    figure = dv.Figure(size=(8, 8), grid=(2, 1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    stats.distributions.beta(a=a, b=b, alpha=alpha, beta=beta).cdf_on_chart(chart).plot()

    chart = dv.Chart2d(figure=figure, position=figure[1,0])
    stats.distributions.beta(a=a, b=b, alpha=alpha, beta=beta).pdf_on_chart(chart).plot()

    figure.show()


"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()
    