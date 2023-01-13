import numpy as np

# a = np.arange(2*3*4)
# print(a)

# a = np.reshape(a, [2, 3, 4])
# print(a)

# print(a.sum(axis=2))

env = np.zeros(shape=[8, 8, 3])

env[ 0,:,0] = 1
env[-1,:,0] = 1
env[: ,0,0] = 1
env[:,-1,0] = 1

print(env[:,:,0])