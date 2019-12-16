import devfx.data_vizualization.matplotlib as dv
import devfx.math as math

"""----------------------------------------------------------------
"""
def f(p):
   return p/(1.0-p)

def logit(p):
   return math.loge(p/(1.0-p))


figure = dv.Figure(size=(8, 8), grid=(2, 1))

x_range = math.range(0.0, 1.0, +0.005)

chart = dv.Chart2d(figure=figure, position=figure[0,0])
chart.plot(x_range, f(x_range))

chart = dv.Chart2d(figure=figure, position=figure[1,0])
chart.plot(x_range, logit(x_range))

figure.show()

