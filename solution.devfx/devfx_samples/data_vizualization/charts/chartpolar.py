import numpy as np
import devfx.math as math
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""     
def test():
    x = math.range(0, 4.0, 0.01)
    theta = 2.0*math.pi*x
    theta_label='theta(x)=2*pi*x'
                
    chart = dv.ChartPolar(fig_size=(8, 4), rmax=2)
    [chart_line1] = chart.plot(theta, x, label=theta_label)
    chart.set_legend(loc=(1.00, 0.0))

    dv.Figures.show()


"""------------------------------------------------------------------------------------------------
"""                   
if __name__ == '__main__':
    test()
    
    
