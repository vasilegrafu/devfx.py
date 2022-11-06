import devfx.exceptions as excps

class GlobalStorage(object):
    __storage__ = {}

    @staticmethod
    def get(key):
        return GlobalStorage.__storage__[key]
    
    @staticmethod
    def set(key, value):
        GlobalStorage.__storage__[key] = value

    @staticmethod
    def exists(key):
        return key in GlobalStorage.__storage__.keys()

    @staticmethod
    def remove(key):
        GlobalStorage.__storage__.pop(key)

    @staticmethod
    def intercept(key, source_fn=None, refresh_condition_fn=None):
        if(key not in GlobalStorage.__storage__.keys()):
            if(source_fn is not None):
                GlobalStorage.__storage__[key] = source_fn()
            else:
                raise excps.ApplicationError()
        else:
            if(refresh_condition_fn is not None):
                if(refresh_condition_fn(GlobalStorage.__storage__[key])):
                    GlobalStorage.__storage__[key] = source_fn()
                else:
                    pass
            else:
                pass
        return GlobalStorage.__storage__[key]

