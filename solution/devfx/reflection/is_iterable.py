import builtins as builtins

def is_iterable(arg):
    try:
        (_ for _ in arg)
        return True
    except builtins.TypeError:
        return False
