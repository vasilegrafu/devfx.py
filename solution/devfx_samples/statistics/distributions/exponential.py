import devfx.math as math
import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
"""   
def test_cdf():   
    rate_max = 1
    rate_range = math.range(1, rate_max+1)

    chart = dv.Chart2d()

    for rate in rate_range:
        stats.distributions.exponential(rate).cdf_on_chart(chart).bar(n=16)

    chart.figure.show()

"""------------------------------------------------------------------------------------------------
""" 
def test_pdf():   
    rate_max = 1
    rate_range = math.range(1, rate_max+1)

    chart = dv.Chart2d()

    for rate in rate_range:
        stats.distributions.exponential(rate).pdf_on_chart(chart).bar(n=16)

    chart.figure.show()
   
"""------------------------------------------------------------------------------------------------
""" 
def test():    
    test_cdf()
    test_pdf()

"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()
    