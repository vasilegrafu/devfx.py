import devfx.exceptions as exps

class persistent_variable(object):
    __storage = {}

    @staticmethod
    def __new__(cls, name, constructor_fn=None):
        if(name is None):
            raise exps.ArgumentError()
        if(len(name.strip()) == 0):
            raise exps.ArgumentError()
        
        if(constructor_fn is not None):
            if(name not in persistent_variable.__storage):
                persistent_variable.__storage[name] = constructor_fn()
            variable = persistent_variable.__storage[name]
            return variable
        else:
            variable = persistent_variable.__storage[name]
            return variable


