import devfx.exceptions as excps

class ObjectStorage(object):
    @staticmethod
    def __create_storage_if_not_exists(obj):
        if(not hasattr(obj, '__storage__')):
            setattr(obj, '__storage__', {}) 

    @staticmethod
    def get(obj, key):
        ObjectStorage.__create_storage_if_not_exists(obj)
        return obj.__storage__[key]
    
    @staticmethod
    def set(obj, key, value):
        ObjectStorage.__create_storage_if_not_exists(obj)
        obj.__storage__[key] = value

    @staticmethod
    def exists(obj, key):
        ObjectStorage.__create_storage_if_not_exists(obj)
        return key in obj.__storage__.keys()

    @staticmethod
    def remove(obj, key):
        ObjectStorage.__create_storage_if_not_exists(obj)
        obj.__storage__.pop(key)

    @staticmethod
    def intercept(obj, key, source_fn=None, refresh_condition_fn=None):
        ObjectStorage.__create_storage_if_not_exists(obj)
        if(key not in obj.__storage__.keys()):
            if(source_fn is not None):
                obj.__storage__[key] = source_fn()
            else:
                raise excps.ApplicationError()
        else:
            if(refresh_condition_fn is not None):
                if(refresh_condition_fn(obj.__storage__[key])):
                    obj.__storage__[key] = source_fn()
                else:
                    pass
            else:
                pass
        return obj.__storage__[key]

