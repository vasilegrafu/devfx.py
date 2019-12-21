import numpy as np
import devfx.math as math
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f():
        x = ml.constant(math.range(-32.0, +16.0, 0.01), dtype=ml.float32)
        y = ml.nn.elu(x)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(), color='blue')
    chart.figure.show()

if __name__ == '__main__':
    test()


