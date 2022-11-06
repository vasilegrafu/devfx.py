import inspect as insp
import functools as fnt
import devfx.exceptions as excps
import devfx.core as core

"""------------------------------------------------------------------------------------------------
"""
def is_series(data):
    if(core.is_iterable(data)):
        return True
    else:
        return False

"""------------------------------------------------------------------------------------------------
"""
def validate_is_series(data):
    if(not is_series(data)):
        raise excps.ArgumentError()

def validate_args_is_series(*arg_names):
    def _(fn):
        signature = insp.signature(fn)
        @fnt.wraps(fn)
        def __(*args, **kwargs):
            bound_arguments = signature.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            for arg_name in arg_names:
                data = bound_arguments.arguments[arg_name]
                validate_is_series(data)
            output = fn(*args, **kwargs)
            return output
        return __
    return _