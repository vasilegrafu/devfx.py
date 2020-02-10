import numpy as np
import devfx.math as math
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""      
def test():
    theta = math.linspace(-4 * math.pi, 4 * math.pi, 100)
    z = math.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * math.sin(theta)
    y = r * math.cos(theta)
                
    chart = dv.Chart3d()
    [chart_line1] = chart.plot(x, y, z, label='parametric curve')
    chart.set_legend()
    chart.figure.show()


"""------------------------------------------------------------------------------------------------
"""             
if __name__ == '__main__':
    test()

