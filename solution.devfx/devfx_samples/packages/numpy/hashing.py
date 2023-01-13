import numpy as np
import random as rnd
import hashlib as hlib
import devfx.diagnostics as dgn

a = np.random.rand(1024*1024)

sw = dgn.Stopwatch().start()

for i in range(0, 10):
    h = int(hlib.md5(a.view(np.uint8)).hexdigest(), 16)
    # print(h)

print(sw.elapsed)

