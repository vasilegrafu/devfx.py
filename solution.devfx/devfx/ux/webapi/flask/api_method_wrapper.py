from flask import request, make_response
from decimal import Decimal
from datetime import datetime, date, time
from uuid import UUID
from typing import get_type_hints
import devfx.exceptions as exp
from devfx.json import JsonSerializer
from devfx.json import JsonDeserializer
from ..http_status_code import HttpStatusCode
from ..base_response import BaseResponse

def api_method_wrapper():
    def _(fn):
        def __(**kwargs):
            output = __process_request(fn, **kwargs)   
            return output              
        if(not hasattr(fn, '_underlying_fn')):
            __._underlying_fn = fn
        else:
            __._underlying_fn = fn._underlying_fn
        __.__name__ = fn.__name__
        return __ 
    return _

def __process_request(fn, **kwargs):
    try:
        if(not hasattr(fn, '_underlying_fn')):
            fn = fn
        else:
            fn = fn._underlying_fn

        fn_args_info = get_type_hints(fn)
        fn_args_info.pop('return', None)

        if(len(fn_args_info) == 0):
            output = fn()
        else:
            next_kwargs = {}
            for arg_name in fn_args_info.keys():
                arg_type = fn_args_info[arg_name]
                if(arg_type in (str, int, float, Decimal, bool, datetime, date, time, UUID)):
                    if(arg_name in request.args):
                        next_kwargs[arg_name] = request.args.get(arg_name, default=arg_type(), type=arg_type)
                    elif(arg_name in kwargs):
                        next_kwargs[arg_name] = arg_type(kwargs[arg_name])
                    else:
                        raise exp.ValidationError('Argument not found: ' + arg_name)
                else:
                    next_kwargs[arg_name] = JsonDeserializer.deserialize(arg_type, request.data.decode('utf-8'))
            output = fn(**next_kwargs)
        output = JsonSerializer.serialize(output)
        output = make_response(output)
        output.status_code = str(HttpStatusCode.OK.value)
        return output
    except Exception as e:
        if isinstance(e, exp.ValidationError):
            output = BaseResponse(error_messages=[e.message])
            output = JsonSerializer.serialize(output)
            output = make_response(output)
            output.status_code = str(HttpStatusCode.BAD_REQUEST.value)
            return output
        elif isinstance(e, exp.AuthenticationError):
            output = BaseResponse(error_messages=[e.message])       
            output = JsonSerializer.serialize(output)
            output = make_response(output)
            output.status_code = str(HttpStatusCode.UNAUTHORIZED.value)
            return output
        elif isinstance(e, exp.AutorizationError):
            output = BaseResponse(error_messages=[e.message]) 
            output = JsonSerializer.serialize(output)
            output = make_response(output)
            output.status_code = str(HttpStatusCode.FORBIDDEN.value)
            return output
        elif isinstance(e, exp.NotFoundError):
            output = BaseResponse(error_messages=[e.message]) 
            output = JsonSerializer.serialize(output)
            output = make_response(output)
            output.status_code = str(HttpStatusCode.NOT_FOUND.value)
            return output
        else:
            output = BaseResponse(error_messages=[str(e)]) 
            output = JsonSerializer.serialize(output)
            output = make_response(output)
            output.status_code = str(HttpStatusCode.INTERNAL_SERVER_ERROR.value)
            return output