import builtins as bt
import inspect as insp
import devfx.exceptions as exceps

def is_typeof(arg, classinfo):
    if(is_instance(arg, object)):
        return is_instance(arg, classinfo)
    if(is_instance(arg, type)):
        return is_class_or_subclass(arg, classinfo)
    raise exceps.NotSupportedError()

def is_class_or_subclass(arg, classinfo):
    return bt.issubclass(arg, classinfo)

def is_instance(arg, classinfo):
    return bt.isinstance(arg, classinfo)

def is_function(arg):
    return insp.isfunction(arg)

def is_iterable(arg):
    try:
        (_ for _ in arg)
        return True
    except bt.TypeError:
        return False










   

    

