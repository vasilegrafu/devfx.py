import numpy as np
import devfx.math as math
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f(L, s0):
        x = ml.constant(math.range(-8.0, +8.0, 0.01), dtype=ml.float32)
        y = ml.nn.tanh(x, L, s0)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 4))
    chart.plot(*f(L=1.0, s0=1.0/4.0), color='blue')
    chart.plot(*f(L=1.0, s0=1.0), color='red')
    chart.plot(*f(L=2.0, s0=1.0), color='yellow')
    chart.figure.show()

if __name__ == '__main__':
    test()


