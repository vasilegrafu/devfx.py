import numpy as np
import devfx.math as math
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f(s0, a):
        x = ml.constant(math.range(-32.0, +16.0, 0.01), dtype=ml.float32)
        y = ml.nn.relu(x, s0, a)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(s0=0.1, a=0.025), color='blue')
    chart.plot(*f(s0=0.2, a=0.05), color='red')
    chart.figure.show()

if __name__ == '__main__':
    test()


