import numpy as np
import devfx.math as math
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""      
def test():
    x = math.linspace(-2*math.pi, 2*math.pi, 100)
    y = math.linspace(-2*math.pi, 2*math.pi, 100)
    z = math.sin(x+y)
                
    chart = dv.Chart3d()
    chart.scatter(x, y, z)
    chart.figure.show()


"""------------------------------------------------------------------------------------------------
"""             
if __name__ == '__main__':
    test()

