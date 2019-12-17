import builtins as builtins
import devfx.exceptions as exceps

def setattr(object, name, value):
    builtins.setattr(object, name, value)

def getattr(object, name):
    return builtins.getattr(object, name)

def hasattr(object, name):
    return builtins.hasattr(object, name)

def delattr(object, name):
    return builtins.delattr(object, name)

