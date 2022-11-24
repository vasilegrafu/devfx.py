import builtins as bt
import devfx.exceptions as ex

"""------------------------------------------------------------------------------------------------
"""
def setattr(obj, name, value):
    bt.setattr(obj, name, value)

def getattr(obj, name):
    return bt.getattr(obj, name)

def hasattr(obj, name):
    return bt.hasattr(obj, name)

def delattr(obj, name):
    return bt.delattr(obj, name)

"""------------------------------------------------------------------------------------------------
"""
class getter(object):
    def __init__(self, fn):
        self.__fn = fn

    def __(self, obj, type=None):
        return self.__fn(obj)

class setter(object):
    def __init__(self, fn):
        self.__fn = fn

    def __set__(self, obj, value):
        return self.__fn(obj, value)


