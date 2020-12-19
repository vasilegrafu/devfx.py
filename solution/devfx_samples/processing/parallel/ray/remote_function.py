import time
import devfx.processing.distributed as pd

def fn(x):
    time.sleep(1)
    return x

remote_fn = pd.remote(fn)
results = pd.get_results([remote_fn(x) for x in range(0, 4)])

print(results)