import numpy as np
import devfx.mathematics as math
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
def test1():
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

def test2():
    x = math.range(-8.0, +8.0, 0.01)
    y = x*x*np.cos(x) + np.random.normal(0.0, 16.0, size=len(x))

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.scatter(x, y)
    chart.figure.show()

def test3():
    x = math.range(0.0, +100000.0, 10)
    y = np.exp(-x*5e-4)

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.scatter(x, y)
    chart.figure.show()


"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test3()

