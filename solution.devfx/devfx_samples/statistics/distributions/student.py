import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""    
def test_cdf():   
    figure = dv.Figure(size=(8, 4))

    chart = dv.Chart2d(figure)
    n = 1
    stats.distributions.student(n).cdf_on_chart(chart).plot()
    n = 2
    stats.distributions.student(n).cdf_on_chart(chart).plot()
    n = 3
    stats.distributions.student(n).cdf_on_chart(chart).plot()
    n = 4
    stats.distributions.student(n).cdf_on_chart(chart).plot()

    figure.show()

"""------------------------------------------------------------------------------------------------
"""     
def test_pdf():
    figure = dv.Figure(size=(8, 3))

    chart = dv.Chart2d(figure, ylim=(0.0, 0.4))
    n = 1
    stats.distributions.student(n).pdf_on_chart(chart).plot()
    n = 2
    stats.distributions.student(n).pdf_on_chart(chart).plot()
    n = 3
    stats.distributions.student(n).pdf_on_chart(chart).plot()
    n = 4
    stats.distributions.student(n).pdf_on_chart(chart).plot()

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
    