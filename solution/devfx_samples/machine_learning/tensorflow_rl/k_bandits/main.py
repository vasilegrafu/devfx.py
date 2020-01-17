import tensorflow as tf
import numpy as np
import devfx.core as core
import devfx.os as os
import devfx.statistics as stats
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
def main():
    for p in np.arange(0.01, 0.5, 0.01):
        K_MEANs = [-4, -3, -2, -1, 0, 0, 1, 2, 3, 4]
        K = len(K_MEANs)
        K_NQs = [[0, 0] for _ in range(K)]
        K_DISTRIBUTIONS = [stats.distributions.normal(mu=k_mean, sigma=1.0) for k_mean in K_MEANs]

        N = 20000
        du = stats.distributions.uniform(a=0.0, b=1.0)
        for n in range(1, (N+1)):
            rv = du.rv()
            if(rv <= p):
                a = stats.series.choose_one(data=range(K))
            else:
                a = np.argmax(a=[k_nq[1] for k_nq in K_NQs], axis=0)
            k_rv = K_DISTRIBUTIONS[a].rv()
            K_NQs[a][0] += 1
            K_NQs[a][1] = K_NQs[a][1] + (1.0/K_NQs[a][0])*(k_rv - K_NQs[a][1])
        print(p, K_NQs[K-1][0])

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()


