import numpy as np
import devfx.math as math
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f(s, n):
        x = ml.constant(math.range(-64.0, +64.0, 0.01), dtype=ml.float32)
        y = ml.nn.sympow(x, s, n)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(s=1.0, n=2.0), color='blue')
    chart.plot(*f(s=1.0, n=4.0), color='red')
    chart.plot(*f(s=1.0/4.0, n=3.0), color='yellow')
    chart.figure.show()

if __name__ == '__main__':
    test()


