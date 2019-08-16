import builtins as builtins

def can_be_typeof(arg, classinfo):
    try:
        _ = (classinfo)(arg)
        return True
    except builtins.TypeError:
        return False

