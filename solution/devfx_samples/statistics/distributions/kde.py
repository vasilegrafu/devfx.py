import numpy as np
import devfx.statistics as stats
import devfx.data_vizualization.matplotlib as dv

"""------------------------------------------------------------------------------------------------
"""
normal1 = stats.normal(mu=0.0, sigma=1.0)
normal2 = stats.normal(mu=5.0, sigma=1.0)
data = np.concatenate((normal1.ndr(size=128), normal2.ndr(size=512)))

figure = dv.Figure(size=(8, 4))

chart = dv.Chart2d(figure=figure, position=(1, 1, 1))
stats.dhistogram.from_data(data).on_chart(chart).bar()
stats.kde(data).pdf_on_chart(chart).plot('y')

print(stats.kde(data).cdf(0))

figure.show()

