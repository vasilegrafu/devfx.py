import numpy as np
import devfx.math as math
import devfx.machine_learning_deprecated as ml
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f(s0, b):
        x = ml.constant(math.range(-32.0, +16.0, 0.01), dtype=ml.float32)
        y = ml.nn.loglu(x, s0, b)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(s0=1.0, b=np.e), color='yellow')
    chart.plot(*f(s0=2.0, b=3.0), color='blue')
    chart.plot(*f(s0=1.0/2.0, b=8.0*np.e), color='red')
    chart.figure.show()

if __name__ == '__main__':
    test()


