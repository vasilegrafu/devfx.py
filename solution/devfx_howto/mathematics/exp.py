import devfx.data_vizualization.matplotlib as dv
import devfx.mathematics as math

"""----------------------------------------------------------------
"""
def f(e, x):
   return e**x


figure = dv.Figure(size=(4, 4), grid=(1, 1))

x_range = math.range(0.0, 10.0, +0.05)


e = 1.0/1.5
chart = dv.Chart2d(figure=figure, position=figure[0,0])
chart.plot(x_range, f(e, x_range))

e = 1.0/1.75
chart = dv.Chart2d(figure=figure, position=figure[0,0])
chart.plot(x_range, f(e, x_range))

e = 1.0/2.0
chart = dv.Chart2d(figure=figure, position=figure[0,0])
chart.plot(x_range, f(e, x_range))

e = 1.0/3.0
chart = dv.Chart2d(figure=figure, position=figure[0,0])
chart.plot(x_range, f(e, x_range))

e = 1.0/4.0
chart = dv.Chart2d(figure=figure, position=figure[0,0])
chart.plot(x_range, f(e, x_range))

figure.show()

