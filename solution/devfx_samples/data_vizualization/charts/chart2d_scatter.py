import numpy as np
import devfx.math as math
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    x = math.range(-8.0, +8.0, 0.01)
    y = x*x*np.cos(x) + np.random.normal(0.0, 16.0, size=len(x))

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.scatter(x, y)
    chart.figure.show()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test()

