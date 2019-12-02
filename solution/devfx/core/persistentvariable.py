import devfx.exceptions as exceps

class persistentvariable(object):
    __storage__ = {}

    @staticmethod
    def __new__(cls, name, constructor_fn=None):
        if(name is None):
            raise exceps.ArgumentError()
        if(len(name.strip()) == 0):
            raise exceps.ArgumentError()
        
        if(constructor_fn is not None):
            if(name not in persistentvariable.__storage__):
                persistentvariable.__storage__[name] = constructor_fn()
            variable = persistentvariable.__storage__[name]
            return variable
        else:
            variable = persistentvariable.__storage__[name]
            return variable


