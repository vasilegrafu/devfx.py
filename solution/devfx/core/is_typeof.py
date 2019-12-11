import devfx.exceptions as exceps
from .is_instance import is_instance
from .is_class_or_subclass import is_class_or_subclass

def is_typeof(arg, classinfo):
    if(is_instance(arg, object)):
        return is_instance(arg, classinfo)
    if(is_instance(arg, type)):
        return is_class_or_subclass(arg, classinfo)
    raise exceps.NotSupportedError()





   

    

