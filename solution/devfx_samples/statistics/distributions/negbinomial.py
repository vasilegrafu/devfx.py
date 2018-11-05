import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv
  
"""------------------------------------------------------------------------------------------------
""" 
def test_cdf():
    figure = dv.Figure(size=(8, 8), grid=(2,1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    n = 4
    p_range = [0.16, 0.32]
    for p in p_range:
        stats.negbinomial(n, p).cdf_on_chart(chart).plot()

    chart = dv.Chart2d(figure=figure, position=figure[1,0])
    n = 8
    p_range = [0.16, 0.32]
    for p in p_range:
        stats.negbinomial(n, p).cdf_on_chart(chart).plot()

    figure.show()
    
"""------------------------------------------------------------------------------------------------
""" 
def test_pmf():
    figure = dv.Figure(size=(8, 8), grid=(2,1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0], ylim=(0, 0.10))
    n = 1
    p_range = [0.16, 0.32]
    for p in p_range:
        stats.negbinomial(n, p).pmf_on_chart(chart).plot()

    chart = dv.Chart2d(figure=figure, position=figure[1,0], ylim=(0, 0.10))
    n = 8
    p_range = [0.16, 0.32]
    for p in p_range:
        stats.negbinomial(n, p).pmf_on_chart(chart).plot()

    figure.show()
  
"""------------------------------------------------------------------------------------------------
""" 
def test():
    test_cdf()
    test_pmf()

"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()
    
    

