import tensorflow as tf
import numpy as np
import devfx.core as core
import devfx.os as os
import devfx.statistics as stats
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv

K_MEANs = [-4, -3, -2, -1, 0, 0, 1, 2, 3, 4]
K = len(K_MEANs)
K_NQs = [[0, 0] for _ in range(K)]

k_distributions = []
for k_mean in K_MEANs:
    k_distribution = stats.distributions.normal(mu=k_mean, sigma=1.0)
    k_distributions.append(k_distribution)

N = 100000
epsilon = 0.1
for n in range(1, (N+1)):
    if(n == 1):
        k = stats.series.choose_one(range(K))
    else:
        prob:
            yes: exploration
            no: exploatation
    k_rv = k_distributions[k].rv()
    K_NQs[k][0] += 1
    K_NQs[k][1] = K_NQs[k][1] + (1.0/K_NQs[k][0])*(k_rv - K_NQs[k][1])
    if(n%1000 == 0):
        print(K_NQs)



