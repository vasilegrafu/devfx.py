import numpy as np
import devfx.math as math
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""      
def test():
    x = math.linspace(-1*math.pi, 1*math.pi, 32)
    y = math.linspace(-1*math.pi, 1*math.pi, 32)
    xx, yy = np.meshgrid(x, y)
    zz = math.sin(xx)*math.sin(yy)
                
    chart = dv.Chart3d()
    chart.wireframe(xx, yy, zz)
    chart.figure.show()


"""------------------------------------------------------------------------------------------------
"""             
if __name__ == '__main__':
    test()

