import numpy as np
import pymc3 as pymc3
import devfx.math as math
import devfx.statistics as stats
import devfx.data_vizualization as dv

""" We will generate some data based on real parameters
"""

# Initialize random number generator
np.random.seed(512)

# Size of dataset
size = 1024

# True parameter values
alpha = 2.0
beta = 1.0

# Predictor variable
X = math.linspace(0.0, 16.0, size)

# Noise
mu = 0.0
sigma = 1.0
epsilon = stats.distributions.normal(mu, sigma).rvs(size)

Y_model = alpha + beta*X
Y_real = Y_model + epsilon

# Display model
# chart = dv.chart2d(fig_size=(8, 4))
# chart.plot(X, Y_model)
# chart.plot(X, Y_real)
# dv.figures.show()


""" Bayesian inference
    We will try to infer alpha, beta on data generated (Y2)
"""
#

with pymc3.Model() as pm:
    # Priors for unknown model parameters
    alpha = pymc3.Uniform('alpha', lower=-8, upper=+8)
    beta = pymc3.Uniform('beta', lower=-8, upper=+8)
    sigma = pymc3.HalfNormal('sigma', sd=1)

    # Expected value of outcome
    mu = alpha + beta*X

    # Likelihood (sampling distribution) of observations
    Y_observed = pymc3.Normal('Y_observed', mu=mu, sd=sigma, observed=Y_real)

    # Sampling
    trace = pymc3.sample(draws=1024*32, n_init=1024*256)

# Posterior analysis
# pymc3.traceplot(trace)

print(stats.series.mean(trace['alpha']))
print(stats.series.mean(trace['beta']))
print(stats.series.mean(trace['sigma']))

figure = dv.Figure(size=(8, 8))

chart = dv.Chart2D(figure=figure, position=(3, 1, 1))
stats.estimators.dhistogram.from_data(trace['alpha']).on_chart(chart).bar()

chart = dv.Chart2D(figure=figure, position=(3, 1, 2))
stats.estimators.dhistogram.from_data(trace['beta']).on_chart(chart).bar()

chart = dv.Chart2D(figure=figure, position=(3, 1, 3))
stats.estimators.dhistogram.from_data(trace['sigma']).on_chart(chart).bar()

figure.show()
