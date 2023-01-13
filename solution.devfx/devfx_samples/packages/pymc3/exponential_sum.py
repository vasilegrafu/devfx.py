import pymc3 as pymc3
import devfx.statistics as stats
import devfx.data_vizualization as dv

with pymc3.Model() as pm:
    exponential_1 = pymc3.Exponential("exponential_1", 1)
    exponential_2 = pymc3.Exponential("exponential_2", 1)
    exponential_3 = pymc3.Exponential("exponential_3", 1)
    exponential_4 = pymc3.Exponential("exponential_4", 1)

    x = pymc3.Deterministic("x", exponential_1 + exponential_2 + exponential_3 + exponential_4)

    start = pymc3.find_MAP()
    step = pymc3.Metropolis()
    trace = pymc3.sample(draws=1024*16, step=step, start=start)

figure = dv.Figure(size=(8, 8))

chart = dv.Chart2d(figure=figure, position=(2, 1, 1), xmin=0)
stats.estimators.dhistogram.from_data(trace['x'], bin_count=24).on_chart(chart).bar()

# chart = dv.chart2d(figure=figure, position=(2, 1, 2))
# stats.estimators.cdhistogram.from_data(exponential_1.random(size=1024*64)).on_chart(chart).bar()

figure.show()