from dataclasses import is_dataclass
from typing import Any
from json import dumps as dump_json

from decimal import Decimal
from datetime import date, time, datetime
from uuid import UUID

class JsonSerializer:
    @staticmethod
    def serialize(obj: Any) -> str:
        json_serializable = JsonSerializer.__convert_to_serializable(obj)
        json = dump_json(json_serializable)
        return json

    @staticmethod
    def __convert_to_serializable(obj: Any) -> Any:
        if obj is None:
            return None
        
        if isinstance(obj, list):
            return [JsonSerializer.__convert_to_serializable(item) for item in obj]
        elif isinstance(obj, tuple):
            return [JsonSerializer.__convert_to_serializable(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: JsonSerializer.__convert_to_serializable(value) for key, value in obj.items()}
        elif is_dataclass(obj):
            return {field.name: JsonSerializer.__convert_to_serializable(getattr(obj, field.name)) for field in obj.__dataclass_fields__.values()}
        elif isinstance(obj, str):
            return obj
        elif isinstance(obj, (int, float, Decimal)):
            return obj
        elif isinstance(obj, bool):
            return obj
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, time):
            return obj.strftime("%H:%M:%S")
        elif isinstance(obj, UUID):
            return str(obj)
        else:
            raise TypeError(f"Unsupported type for json serialization: {type(obj)}")
        

