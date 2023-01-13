import numpy as np
import devfx.math as math
import devfx.machine_learning_deprecated as ml
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f(L, k):
        x = ml.constant(math.range(-16.0, +16.0, 0.01), dtype=ml.float32)
        y = ml.nn.softsign(x, L, k)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 4))
    chart.plot(*f(L=1.0, k=1.0), color='blue')
    chart.plot(*f(L=2.0, k=1.0), color='red')
    chart.plot(*f(L=1.0, k=1.0/2.0), color='yellow')
    chart.figure.show()

if __name__ == '__main__':
    test()
