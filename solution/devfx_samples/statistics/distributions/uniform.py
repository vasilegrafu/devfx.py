import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
""" 
def test():
    a = 2
    b = 4

    figure = dv.Figure(size=(8, 8), grid=(2, 1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    stats.distributions.uniform(a=a, b=b).cdf_on_chart(chart).plot()

    chart = dv.Chart2d(figure=figure, position=figure[1,0])
    stats.distributions.uniform(a=a, b=b).pdf_on_chart(chart).plot()

    figure.show()


"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()
    