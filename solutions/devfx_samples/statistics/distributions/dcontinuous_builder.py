import devfx.mathematics as math
import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
""" 
def test():   
    def exponential(rate):
        return stats.distributions.dcontinuous_builder(
            cdf=lambda x: 1.0-math.e**(-rate*x),
            pdf=lambda x: rate*math.e**(-rate*x),
            a=0,
            b=+math.inf)
              
    rate_max = 4
    rate_range = math.range(1, rate_max+1)

    chart = dv.Chart2d()

    for rate in rate_range:
        exponential(rate).pdf_on_chart(chart).plot()

    chart.figure.show()


"""------------------------------------------------------------------------------------------------
""" 
if __name__ == '__main__':
    test()