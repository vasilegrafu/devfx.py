import builtins as builtins
import devfx.exceptions as exceps

def setattr(self, name, value):
    builtins.setattr(self, name, value)

def getattr(self, name):
    return builtins.getattr(self, name)

def hasattr(self, name):
    return builtins.hasattr(self, name)

def getorcreateattr(self, name, value=None, value_fn=None):
    if (not hasattr(self, name)):
        if(value is None and value_fn is None):
            setattr(self, name, None)
        elif(value is not None and value_fn is None):
            setattr(self, name, value)
        elif(value is None and value_fn is not None):
            setattr(self, name, value_fn())
        elif(value is not None and value_fn is not None):
            raise exceps.ArgumentError()
        else:
            raise exceps.NotSupportedError()
    return getattr(self, name)