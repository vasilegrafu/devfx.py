import numpy as np
import devfx.math as math
import devfx.machine_learning as ml
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f():
        x = ml.constant(math.range(-32.0, +32.0, 0.01), dtype=ml.float32)
        y = ml.nn.softplus(x)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(), color='blue')
    chart.figure.show()

if __name__ == '__main__':
    test()


