import inspect as insp
import functools as fnt
import devfx.exceptions as exp
import devfx.core as core
from .. import series

"""------------------------------------------------------------------------------------------------
"""
def is_mseries(data):
    if(core.is_iterable(data)):
        if(len(data) == 0):
            return False

        for column_data in data:
            if(not series.is_series(column_data)):
                return False

        for column_data in data:
            if(len(data[0]) != len(column_data)):
                return False

        return True
    else:
        return False

"""------------------------------------------------------------------------------------------------
"""
def validate_is_mseries(data):
    if(not is_mseries(data)):
        raise exp.ArgumentError()

def validate_args_is_mseries(*arg_names):
    def _(fn):
        signature = insp.signature(fn)
        @fnt.wraps(fn)
        def __(*args, **kwargs):
            bound_arguments = signature.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            for arg_name in arg_names:
                data = bound_arguments.arguments[arg_name]
                validate_is_mseries(data)
            output = fn(*args, **kwargs)
            return output
        return __
    return _

    