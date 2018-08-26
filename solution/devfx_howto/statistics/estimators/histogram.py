import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
""" 
normal = stats.normal(mu=0.0, sigma=1.0)

figure = dv.Figure(size=(8, 4))

chart = dv.Chart2d(figure=figure)
stats.dhistogram.from_distribution(normal).on_chart(chart).bar()

figure.show()

