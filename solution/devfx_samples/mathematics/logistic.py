import devfx.math as math
import devfx.data_vizualization.matplotlib as dv

"""----------------------------------------------------------------
"""
x_range = math.range(-20.0, 20.0, +0.01)


"""----------------------------------------------------------------
"""
figure = dv.Figure(size=(8, 8), grid=(4, 1))

beta0 = 0.0
beta1 = 0.25
chart = dv.Chart2d(figure=figure, position=figure[0,0])
chart.plot(x_range, math.logistic(beta0 + beta1*x_range))

beta0 = 0.0
beta1 = 0.5
chart = dv.Chart2d(figure=figure, position=figure[1,0])
chart.plot(x_range, math.logistic(beta0 + beta1*x_range))

beta0 = 0.0
beta1 = 1.0
chart = dv.Chart2d(figure=figure, position=figure[2,0])
chart.plot(x_range, math.logistic(beta0 + beta1*x_range))

beta0 = 0.0
beta1 = 2.0
chart = dv.Chart2d(figure=figure, position=figure[3,0])
chart.plot(x_range, math.logistic(beta0 + beta1*x_range))

figure.show()


"""----------------------------------------------------------------
"""
figure = dv.Figure(size=(8, 8), grid=(4, 1))

beta0 = 0.0
beta1 = 1.0
chart = dv.Chart2d(figure=figure, position=figure[0,0])
chart.plot(x_range, math.logistic(beta0 + beta1*x_range))

beta0 = 1.0
beta1 = 1.0
chart = dv.Chart2d(figure=figure, position=figure[1,0])
chart.plot(x_range, math.logistic(beta0 + beta1*x_range))

beta0 = 2.0
beta1 = 1.0
chart = dv.Chart2d(figure=figure, position=figure[2,0])
chart.plot(x_range, math.logistic(beta0 + beta1*x_range))

beta0 = 4.0
beta1 = 1.0
chart = dv.Chart2d(figure=figure, position=figure[3,0])
chart.plot(x_range, math.logistic(beta0 + beta1*x_range))

figure.show()

