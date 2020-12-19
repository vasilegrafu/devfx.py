import ray

"""------------------------------------------------------------------------------------------------
"""
if(not ray.is_initialized()):
    ray.init(include_dashboard=False)


"""------------------------------------------------------------------------------------------------
"""
class RemoteFunction(object):
    def __init__(self, fn, *args, **kwargs):
        self.remote_function = ray.remote(fn, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.remote_function.remote(*args, **kwargs)

"""------------------------------------------------------------------------------------------------
"""
class RemoteClass(object):
    def __init__(self, cls, *args, **kwargs):
        self.remote_class = ray.remote(cls, *args, **kwargs)
    
    def __call__(self, *args, **kwargs):
        return self.remote_class.remote(*args, **kwargs)

"""------------------------------------------------------------------------------------------------
"""
def get_result(future):
    return ray.get(future)

def get_results(futures):
    return ray.get([future for future in futures])




