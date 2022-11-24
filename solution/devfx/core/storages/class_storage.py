import devfx.exceptions as ex

class ClassStorage(object):
    @staticmethod
    def __create_storage_if_not_exists(cls):
        if(not hasattr(cls, '__storage__')):
            setattr(cls, '__storage__', {}) 

    @staticmethod
    def get(cls, key):
        ClassStorage.__create_storage_if_not_exists(cls)
        return cls.__storage__[key]
    
    @staticmethod
    def set(cls, key, value):
        ClassStorage.__create_storage_if_not_exists(cls)
        cls.__storage__[key] = value

    @staticmethod
    def exists(cls, key):
        ClassStorage.__create_storage_if_not_exists(cls)
        return key in cls.__storage__.keys()

    @staticmethod
    def remove(cls, key):
        ClassStorage.__create_storage_if_not_exists(cls)
        cls.__storage__.pop(key)

    @staticmethod
    def intercept(cls, key, source_fn=None, refresh_condition_fn=None):
        ClassStorage.__create_storage_if_not_exists(cls)
        if(key not in cls.__storage__.keys()):
            if(source_fn is not None):
                cls.__storage__[key] = source_fn()
            else:
                raise ex.ApplicationError()
        else:
            if(refresh_condition_fn is not None):
                if(refresh_condition_fn(cls.__storage__[key])):
                    cls.__storage__[key] = source_fn()
                else:
                    pass
            else:
                pass
        return cls.__storage__[key]

