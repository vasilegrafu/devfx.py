import numpy as np
import devfx.math as math
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
def test1():
    x = math.range(0.0, 8.0, 0.01)

    figure = dv.Figure(size=(8, 8))

    chart = dv.Chart2d(figure=figure, position=((2, 2), (0, 0), (1, 1)), ylim=(0, 4))
    f1 = x**(0.5)
    f1_label='f(x)=x**(0.5)'
    chart.plot(x, f1, label=f1_label)
    chart.set_legend(loc='lower right')

    chart = dv.Chart2d(figure=figure, position=((2, 2), (0, 1), (1, 1)), ylim=(0, 4))
    f2_label='f(x)=x**(2.00)'
    f2 = x**(2.00)
    chart.plot(x, f2, label=f2_label)
    chart.set_legend(loc='lower right')

    chart = dv.Chart2d(figure=figure, position=((2, 2), (1, 0), (1, 2)), ylim=(0, 4))
    chart.plot(x, f1, label=f1_label)
    chart.plot(x, f2, label=f2_label)
    chart.set_legend(loc='lower right')

    figure.show()

"""------------------------------------------------------------------------------------------------
"""
def test2():
    x = math.range(0.0, 8.0, 0.01)

    figure = dv.Figure(size=(8, 8), grid=(2, 2))

    chart = dv.Chart2d(figure=figure, position=figure[0, 0], ylim=(0, 4))
    f1 = x**(0.5)
    f1_label='f(x)=x**(0.5)'
    chart.plot(x, f1, label=f1_label)
    chart.set_legend(loc='lower right')

    chart = dv.Chart2d(figure=figure, position=figure[0, 1], ylim=(0, 4))
    f2_label='f(x)=x**(2.00)'
    f2 = x**(2.00)
    chart.plot(x, f2, label=f2_label)
    chart.set_legend(loc='lower right')

    chart = dv.Chart2d(figure=figure, position=figure[1, :], ylim=(0, 4))
    chart.plot(x, f1, label=f1_label)
    chart.plot(x, f2, label=f2_label)
    chart.set_legend(loc='lower right')

    figure.show()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test2()

