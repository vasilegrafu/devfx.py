import numpy as np
import devfx.mathematics as math
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv

cg.enable_imperative_execution_mode()

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f(s0, n):
        x = cg.constant(math.range(-32.0, +16.0, 0.01), dtype=cg.float32)
        y = nn.activation.powlu(x, s0, n)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(1.0, 2.0), color='blue')
    chart.plot(*f(2.0, 3.0), color='red')
    chart.plot(*f(1.0/2.0, 4.0), color='yellow')
    chart.figure.show()

if __name__ == '__main__':
    test()

