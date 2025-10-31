"""
FastAPI utilities for devfx web API framework.

Provides custom JSON response handling and global exception handlers
that integrate devfx's serialization and exception system with FastAPI.
"""

from typing import Any
from fastapi import FastAPI, Request
from fastapi.responses import Response
import devfx.exceptions as exp
from devfx.json import JsonSerializer
from ..http_status_code import HttpStatusCode
from ..base_response import BaseResponse


class JsonResponse(Response):
    """
    Custom JSON Response class that uses devfx's JsonSerializer.
    
    This response class handles special serialization requirements such as:
    - Decimal types
    - datetime/date/time objects
    - Custom dataclass serialization
    - Any other types handled by devfx's JsonSerializer
    
    Usage:
        @app.post('/endpoint', response_class=JsonResponse
        def endpoint() -> MyModel:
            return MyModel(...)
    """
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        """Serialize content using devfx's JsonSerializer."""
        return JsonSerializer.serialize(content).encode("utf-8")


def setup_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers for devfx custom exceptions.
    
    This function should be called once during application initialization,
    after creating the FastAPI app instance but before importing routes.
    
    Registered handlers:
    - ValidationError -> 400 Bad Request
    - AuthenticationError -> 401 Unauthorized
    - AutorizationError -> 403 Forbidden
    - NotFoundError -> 404 Not Found
    - Exception (catch-all) -> 500 Internal Server Error
    
    Args:
        app: The FastAPI application instance
        
    Example:
        from fastapi import FastAPI
        from devfx.ux.webapi.fastapi import setup_exception_handlers
        
        app = FastAPI()
        setup_exception_handlers(app)
    """
    
    @app.exception_handler(exp.ValidationError)
    async def validation_error_handler(request: Request, exc: exp.ValidationError) -> JsonResponse
        """Handle validation errors with 400 Bad Request status."""
        error_response = BaseResponse(error_messages=[exc.message])
        return JsonResponse(
            content=error_response,
            status_code=HttpStatusCode.BAD_REQUEST.value
        )
    
    @app.exception_handler(exp.AuthenticationError)
    async def authentication_error_handler(request: Request, exc: exp.AuthenticationError) -> JsonResponse
        """Handle authentication errors with 401 Unauthorized status."""
        error_response = BaseResponse(error_messages=[exc.message])
        return JsonResponse(
            content=error_response,
            status_code=HttpStatusCode.UNAUTHORIZED.value
        )
    
    @app.exception_handler(exp.AutorizationError)
    async def authorization_error_handler(request: Request, exc: exp.AutorizationError) -> JsonResponse:
        """Handle authorization errors with 403 Forbidden status."""
        error_response = BaseResponse(error_messages=[exc.message])
        return JsonResponse(
            content=error_response,
            status_code=HttpStatusCode.FORBIDDEN.value
        )
    
    @app.exception_handler(exp.NotFoundError)
    async def not_found_error_handler(request: Request, exc: exp.NotFoundError) -> JsonResponse:
        """Handle not found errors with 404 Not Found status."""
        error_response = BaseResponse(error_messages=[exc.message])
        return JsonResponse(
            content=error_response,
            status_code=HttpStatusCode.NOT_FOUND.value
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception) -> JsonResponse:
        """
        Catch-all handler for unexpected exceptions.
        Returns 500 Internal Server Error with error message.
        """
        error_response = BaseResponse(error_messages=[str(exc)])
        return JsonResponse(
            content=error_response,
            status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value
        )
