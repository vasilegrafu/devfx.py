import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
""" 
X = stats.distributions.normal(0.0, 1.0)
E = stats.distributions.normal(0.0, 1.0)

x = X(1024*4)
y = lambda x: 2*x + E(x.size)

print(stats.series.corr(x, y(x)))

figure = dv.Figure(size=(8, 8), grid=(2,1))

chart = dv.Chart2d(figure=figure, position=figure.grid[0,0])
chart.scatter(x, y(x))

chart = dv.Chart2d(figure=figure, position=figure.grid[1,0])
stats.estimators.dhistogram.from_data(y(x), bin_count=16).on_chart(chart).bar()

figure.show()

