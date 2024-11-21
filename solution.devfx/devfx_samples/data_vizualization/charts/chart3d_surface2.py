import numpy as np
import devfx.math as math
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""      
def test():
    x = math.linspace(0.0, 1.5, 64)
    y = math.linspace(0.0, 1.0, 64)
    xx, yy = np.meshgrid(x, y)
    zz = xx * yy
                
    chart = dv.Chart3d()
    chart.surface(xx, yy, zz)
    chart.figure.show()


"""------------------------------------------------------------------------------------------------
"""             
if __name__ == '__main__':
    test()



