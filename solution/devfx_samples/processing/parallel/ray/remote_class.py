import time
import ray
import devfx.processing.distributed as pd

class Class(object):
    def __init__(self, a):
        self.a = a

    def fn(self, x):
        time.sleep(1)
        return (x, self.a)

remote_instance1 = pd.remote(Class).instance(10)
remote_instance2 = pd.remote(Class).instance(20)
remote_instance3 = pd.remote(Class).instance(30)
remote_instance4 = pd.remote(Class).instance(40)

x = [remote_instance1.fn(20), remote_instance2.fn(20), remote_instance3.fn(20), remote_instance4.fn(20)]
result = ray.get(x)
print(result)

x = [remote_instance1.fn(20), remote_instance2.fn(20), remote_instance3.fn(20), remote_instance4.fn(20)]
result = ray.get(x)
print(result)