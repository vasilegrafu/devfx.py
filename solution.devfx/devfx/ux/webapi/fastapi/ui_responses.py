"""
UI Response Wrappers
Combines business data with UI metadata in API responses
"""

from typing import Generic, TypeVar, Any
from pydantic import BaseModel, ConfigDict

T = TypeVar('T')


class UiResponse(BaseModel, Generic[T]):
    """
    Response wrapper for single item with UI hints.
    
    Attributes:
        data: The business data (payload)
        uiHints: The presentation metadata (UI configuration)
    
    Example:
        {
            "data": {"id": 1, "name": "Item"},
            "uiHints": {"id": {"label": "ID", "width": 80}}
        }
    """
    data: T
    uiHints: dict[str, Any]
    
    model_config = ConfigDict(arbitrary_types_allowed=True)


class UiListResponse(BaseModel, Generic[T]):
    """
    Response wrapper for list of items with UI hints.
    
    Attributes:
        data: List of business data items
        uiHints: The presentation metadata (UI configuration)
    
    Example:
        {
            "data": [{"id": 1}, {"id": 2}],
            "uiHints": {"id": {"label": "ID", "width": 80}}
        }
    """
    data: list[T]
    uiHints: dict[str, Any]
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
