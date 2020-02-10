import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
""" 
normalD1 = stats.distributions.normal(mu=0.0, sigma=1.0)
normalDErr = stats.distributions.normal(mu=0.0, sigma=1.0)

X = normalD1.ndr(size=4*1024)
E = normalDErr.ndr(size=4*1024)
Y = 3*X + E

chart = dv.Chart2d(figure=dv.Figure(size=(6, 6)))
chart.scatter(X, Y)
chart.figure.show()
