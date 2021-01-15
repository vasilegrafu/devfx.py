import time
import devfx.processing.parallel.distributed as ppd

def fn(x):
    time.sleep(1)
    return x

remote_fn = ppd.remote(fn)
results = ppd.get_results([remote_fn(x) for x in range(0, 4)])

print(results)