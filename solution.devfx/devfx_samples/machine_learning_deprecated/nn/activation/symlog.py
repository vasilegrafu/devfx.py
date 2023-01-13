import numpy as np
import devfx.math as math
import devfx.machine_learning_deprecated as ml
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f(s, b):
        x = ml.constant(math.range(-16.0, +16.0, 0.01), dtype=ml.float32)
        y = ml.nn.symlog(x, s, b)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(s=1.0, b=np.e), color='blue')
    chart.plot(*f(s=1.0/2.0, b=2.0), color='red')
    chart.plot(*f(s=1.0/4.0, b=2.0), color='yellow')
    chart.figure.show()

if __name__ == '__main__':
    test()


