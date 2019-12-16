import numpy as np
import devfx.mathematics as math
import devfx.machine_learning.tensorflow as ml
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv

cg.enable_imperative_execution_mode()

"""------------------------------------------------------------------------------------------------
"""
def test():
    def f(a):
        x = cg.constant(math.range(-32.0, +16.0, 0.01), dtype=cg.float32)
        y = nn.activation.relu(x, a)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(0.01), color='blue')
    chart.plot(*f(0.05), color='red')
    chart.figure.show()

if __name__ == '__main__':
    test()


