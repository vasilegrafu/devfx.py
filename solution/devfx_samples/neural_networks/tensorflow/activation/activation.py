import numpy as np
import devfx.mathematics as math
import devfx.computation_graphs.tensorflow as cg
import devfx.neural_networks.tensorflow as nn
import devfx.data_vizualization.seaborn as dv

cg.enable_imperative_execution_mode()

"""------------------------------------------------------------------------------------------------
"""
def test_sigmoid():
    def f(L, s0):
        x = cg.constant(math.range(-8.0, +8.0, 0.01), dtype=cg.float32)
        y = nn.activation.sigmoid(x, L, s0)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 4))
    chart.plot(*f(1.0, 1.0/4.0), color='blue')
    chart.plot(*f(1.0, 1.0), color='red')
    chart.plot(*f(2.0, 1.0), color='yellow')
    chart.figure.show()

# if __name__ == '__main__':
#     test_sigmoid()


def test_tanh():
    def f(L, s0):
        x = cg.constant(math.range(-8.0, +8.0, 0.01), dtype=cg.float32)
        y = nn.activation.tanh(x, L, s0)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 4))
    chart.plot(*f(1.0, 1.0/4.0), color='blue')
    chart.plot(*f(1.0, 1.0), color='red')
    chart.plot(*f(2.0, 1.0), color='yellow')
    chart.figure.show()

# if __name__ == '__main__':
#     test_tanh()


def test_softsign():
    def f(L, k):
        x = cg.constant(math.range(-16.0, +16.0, 0.01), dtype=cg.float32)
        y = nn.activation.softsign(x, L, k)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 4))
    chart.plot(*f(1.0, 1.0), color='blue')
    chart.plot(*f(2.0, 1.0), color='red')
    chart.plot(*f(1.0, 1.0/2.0), color='yellow')
    chart.figure.show()

# if __name__ == '__main__':
#     test_softsign()

"""------------------------------------------------------------------------------------------------
"""
def test_symlog():
    def f(s, b):
        x = cg.constant(math.range(-16.0, +16.0, 0.01), dtype=cg.float32)
        y = nn.activation.symlog(x, s, b)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(1.0, np.e), color='blue')
    chart.plot(*f(1.0/2.0, 2.0), color='red')
    chart.plot(*f(1.0/4.0, 2.0), color='yellow')
    chart.figure.show()

# if __name__ == '__main__':
#     test_symlog()


def test_sympow():
    def f(s, n):
        x = cg.constant(math.range(-64.0, +64.0, 0.01), dtype=cg.float32)
        y = nn.activation.sympow(x, s, n)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(1.0, 2.0), color='blue')
    chart.plot(*f(1.0, 4.0), color='red')
    chart.plot(*f(1.0/4.0, 3.0), color='yellow')
    chart.figure.show()

# if __name__ == '__main__':
#     test_sympow()

"""------------------------------------------------------------------------------------------------
"""
def test_softplus():
    def f():
        x = cg.constant(math.range(-32.0, +32.0, 0.01), dtype=cg.float32)
        y = nn.activation.softplus(x)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(), color='blue')
    chart.figure.show()

# if __name__ == '__main__':
#     test_softplus()


def test_relu():
    def f(a):
        x = cg.constant(math.range(-32.0, +16.0, 0.01), dtype=cg.float32)
        y = nn.activation.relu(x, a)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(0.01), color='blue')
    chart.plot(*f(0.05), color='red')
    chart.figure.show()

# if __name__ == '__main__':
#     test_relu()


def test_loglu():
    def f(s0, b):
        x = cg.constant(math.range(-32.0, +16.0, 0.01), dtype=cg.float32)
        y = nn.activation.loglu(x, s0, b)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(1.0, np.e), color='yellow')
    chart.plot(*f(2.0, 3.0), color='blue')
    chart.plot(*f(1.0/2.0, 8.0*np.e), color='red')
    chart.figure.show()

# if __name__ == '__main__':
#     test_loglu()


def test_powlu():
    def f(s0, n):
        x = cg.constant(math.range(-32.0, +16.0, 0.01), dtype=cg.float32)
        y = nn.activation.powlu(x, s0, n)
        return x.numpy(), y.numpy()

    chart = dv.Chart2d(fig_size=(6, 6))
    chart.plot(*f(1.0, 2.0), color='blue')
    chart.plot(*f(2.0, 3.0), color='red')
    chart.plot(*f(1.0/2.0, 4.0), color='yellow')
    chart.figure.show()

# if __name__ == '__main__':
#     test_powlu()

