import ray
import inspect
import devfx.exceptions as ex

"""------------------------------------------------------------------------------------------------
"""
if(not ray.is_initialized()):
    ray.init(include_dashboard=False)

"""------------------------------------------------------------------------------------------------
"""
class RemoteFunction(object):
    def __init__(self, fn):
        self.remote_function = ray.remote(fn)

    def options(self, *args, **kwargs):
        self.remote_function = self.remote_function.options(*args, **kwargs)
        return self

    def __call__(self, *args, **kwargs):
        return self.remote_function.remote(*args, **kwargs)
    def call(self, *args, **kwargs):
        return self.remote_function.remote(*args, **kwargs)

class RemoteClass(object):
    def __init__(self, cls):
        self.remote_class = ray.remote(cls)

    def options(self, *args, **kwargs):
        self.remote_class = self.remote_class.options(*args, **kwargs)
        return self

    def __call__(self, *args, **kwargs):
        return RemoteClass.__InstanceProxy(self.remote_class.remote(*args, **kwargs))
    def instance(self, *args, **kwargs):
        return RemoteClass.__InstanceProxy(self.remote_class.remote(*args, **kwargs))

    class __InstanceProxy(object):
        def __init__(self, remote_instance):
            self.remote_instance = remote_instance

        def __getattr__(self, name):
            return getattr(self.remote_instance, name).remote

    
def remote(entity, *args, **kwargs):
    if(inspect.isfunction(entity)):
        return RemoteFunction(fn=entity)
    if(inspect.isclass(entity)):
        return RemoteClass(cls=entity)
    raise ex.ArgumentError()

"""------------------------------------------------------------------------------------------------
"""
def get_result(future, *, timeout=None):
    return ray.get(future, timeout=timeout)

def get_results(futures, *, timeout=None):
    return ray.get(futures, timeout=timeout)


"""------------------------------------------------------------------------------------------------
"""
def put(value):
    return ray.put(value)

def wait(futures, *, num_returns=1, timeout=None):
    return ray.wait(futures, num_returns=num_returns, timeout=timeout)
