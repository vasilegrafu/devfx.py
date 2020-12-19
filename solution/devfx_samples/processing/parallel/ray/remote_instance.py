import time
import ray
import devfx.processing as processing

class MyClass(object):
    def __init__(self, a):
        self.a = a

    def fn(self, x):
        time.sleep(1)
        return (x, self.a)

RemoteMyClass = ray.remote(MyClass)

remote_myclass1 = RemoteMyClass.remote(10)
remote_myclass2 = RemoteMyClass.remote(20)
remote_myclass3 = RemoteMyClass.remote(30)
remote_myclass4 = RemoteMyClass.remote(40)

x = [remote_myclass1.fn.remote(20), remote_myclass2.fn.remote(20), remote_myclass3.fn.remote(20), remote_myclass4.fn.remote(20)]
result = ray.get(x)
print(result)

x = [remote_myclass1.fn.remote(20), remote_myclass2.fn.remote(20), remote_myclass3.fn.remote(20), remote_myclass4.fn.remote(20)]
result = ray.get(x)
print(result)

x = [remote_myclass1.fn.remote(20), remote_myclass2.fn.remote(20), remote_myclass3.fn.remote(20), remote_myclass4.fn.remote(20)]
result = ray.get(x)
print(result)

x = [remote_myclass1.fn.remote(20), remote_myclass2.fn.remote(20), remote_myclass3.fn.remote(20), remote_myclass4.fn.remote(20)]
result = ray.get(x)
print(result)

# RemoteMyClass = processing.parallel.RemoteClass(MyClass)

# remote_myclass = RemoteMyClass(a=10)

# results = remote_myclass.get_results([remote_myclass.fn.remote(x) for x in range(0, 4)])

# print(results)