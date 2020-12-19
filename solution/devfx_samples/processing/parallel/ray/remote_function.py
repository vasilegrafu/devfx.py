import time
import devfx.processing.parallel as pp

def fn(x):
    time.sleep(1)
    return x

remote_fn = pp.RemoteFunction(fn)
results = pp.get_results([remote_fn(x) for x in range(0, 4)])

print(results)