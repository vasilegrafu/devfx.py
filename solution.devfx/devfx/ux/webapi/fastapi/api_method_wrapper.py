from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from decimal import Decimal
from datetime import datetime, date, time
from uuid import UUID
from typing import get_type_hints, Any
import devfx.exceptions as exp
from devfx.json import JsonSerializer
from devfx.json import JsonDeserializer
from ..http_status_code import HttpStatusCode
from ..base_response import BaseResponse
import inspect

def api_method_wrapper():
    """
    FastAPI wrapper that handles JSON serialization/deserialization and exception handling.
    Automatically converts function parameters from request body and returns JSON responses.
    """
    def _(fn):
        async def __(*args, **kwargs):
            return await __process_request(fn, *args, **kwargs)
        
        # Preserve function metadata
        __.__name__ = fn.__name__
        __.__doc__ = fn.__doc__
        
        # Copy type hints for FastAPI to use
        __.__annotations__ = fn.__annotations__
        
        return __
    return _

async def __process_request(fn, *args, **kwargs):
    try:
        # Get function signature
        fn_args_info = get_type_hints(fn)
        fn_args_info.pop('return', None)
        
        # Check if Request is in the arguments
        request = None
        for arg in args:
            if isinstance(arg, Request):
                request = arg
                break
        
        # If no arguments needed, just call the function
        if len(fn_args_info) == 0:
            output = fn()
        else:
            next_kwargs = {}
            
            # Process each argument
            for arg_name, arg_type in fn_args_info.items():
                # Skip if it's Request type
                if arg_type == Request:
                    next_kwargs[arg_name] = request
                    continue
                    
                # Check if value is already in kwargs (from path/query parameters)
                if arg_name in kwargs:
                    # For primitive types, use the value directly
                    if arg_type in (str, int, float, Decimal, bool, datetime, date, time, UUID):
                        next_kwargs[arg_name] = kwargs[arg_name]
                    else:
                        # For complex types, it might already be deserialized by FastAPI
                        next_kwargs[arg_name] = kwargs[arg_name]
                # Otherwise, try to get from request body
                elif request is not None:
                    if arg_type in (str, int, float, Decimal, bool, datetime, date, time, UUID):
                        # Try to get from query parameters
                        query_params = dict(request.query_params)
                        if arg_name in query_params:
                            next_kwargs[arg_name] = arg_type(query_params[arg_name])
                        else:
                            raise exp.ValidationError(f'Argument not found: {arg_name}')
                    else:
                        # Get from request body for complex types
                        body = await request.body()
                        if body:
                            body_str = body.decode('utf-8')
                            next_kwargs[arg_name] = JsonDeserializer.deserialize(arg_type, body_str)
                        else:
                            raise exp.ValidationError(f'Request body required for argument: {arg_name}')
                else:
                    raise exp.ValidationError(f'Argument not found: {arg_name}')
            
            output = fn(**next_kwargs)
        
        # Serialize output
        output_json = JsonSerializer.serialize(output)
        return Response(content=output_json, media_type="application/json", status_code=HttpStatusCode.OK.value)
        
    except Exception as e:
        return __handle_exception(e)

def __handle_exception(e: Exception):
    """Handle exceptions and return appropriate HTTP responses"""
    if isinstance(e, exp.ValidationError):
        output = BaseResponse(error_messages=[e.message])
        output_json = JsonSerializer.serialize(output)
        return Response(content=output_json, media_type="application/json", status_code=HttpStatusCode.BAD_REQUEST.value)
    
    elif isinstance(e, exp.AuthenticationError):
        output = BaseResponse(error_messages=[e.message])
        output_json = JsonSerializer.serialize(output)
        return Response(content=output_json, media_type="application/json", status_code=HttpStatusCode.UNAUTHORIZED.value)
    
    elif isinstance(e, exp.AutorizationError):
        output = BaseResponse(error_messages=[e.message])
        output_json = JsonSerializer.serialize(output)
        return Response(content=output_json, media_type="application/json", status_code=HttpStatusCode.FORBIDDEN.value)
    
    elif isinstance(e, exp.NotFoundError):
        output = BaseResponse(error_messages=[e.message])
        output_json = JsonSerializer.serialize(output)
        return Response(content=output_json, media_type="application/json", status_code=HttpStatusCode.NOT_FOUND.value)
    
    else:
        output = BaseResponse(error_messages=[str(e)])
        output_json = JsonSerializer.serialize(output)
        return Response(content=output_json, media_type="application/json", status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value)
