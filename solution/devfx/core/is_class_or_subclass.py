import builtins as builtins

def is_class_or_subclass(arg, classinfo):
    return builtins.issubclass(arg, classinfo)

