import ray
import inspect
import devfx.exceptions as excs

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

    def __call__(self, *args, **kwargs):
        return self.remote_function.remote(*args, **kwargs)
    def call(self, *args, **kwargs):
        return self.remote_function.remote(*args, **kwargs)

class RemoteClass(object):
    def __init__(self, cls):
        self.remote_class = ray.remote(cls)

    def options(self, *args, **kwargs):
        self.remote_class = self.remote_class.options(*args, **kwargs)

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
    raise excs.ArgumentError()

"""------------------------------------------------------------------------------------------------
"""
def get_result(future):
    return ray.get(future)

def get_results(futures):
    return ray.get([future for future in futures])




