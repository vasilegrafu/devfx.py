import numpy as np
import devfx.math as math
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    x = math.range(0.0, 8.0, 0.01)
    y1 = x**(0.5)
    y1_label='f(x)=x**(0.5)'
    y2_label='f(x)=x**(2.00)'
    y2 = x**(2.00)

    chart = dv.Chart2d(fig_size=(8, 4), ylim=(0, 4))
    [chart_line1] = chart.plot(x, y1, label=y1_label)
    [chart_line2] = chart.plot(x, y2, label=y2_label)
    chart.set_legend(loc='lower right')
    chart.figure.show()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test()

