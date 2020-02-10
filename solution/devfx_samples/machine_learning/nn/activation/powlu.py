import numpy as np
import devfx.math as math
import devfx.machine_learning as ml
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f(s0, n):
        x = ml.constant(math.range(-32.0, +16.0, 0.01), dtype=ml.float32)
        y = ml.nn.powlu(x, s0, n)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(s0=1.0, n=2.0), color='blue')
    chart.plot(*f(s0=2.0, n=3.0), color='red')
    chart.plot(*f(s0=1.0/2.0, n=4.0), color='yellow')
    chart.figure.show()

if __name__ == '__main__':
    test()

