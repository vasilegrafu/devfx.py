from dataclasses import is_dataclass, fields
from typing import Any, Type, TypeVar, get_type_hints
from json import loads as load_json
from datetime import datetime, date, time

from typing import Any, Type, get_type_hints, get_origin, get_args
from dataclasses import is_dataclass, fields
from datetime import datetime, date, time

T = TypeVar('T')

class JsonDeserializer:
    @staticmethod
    def deserialize(cls: Type[T], json: str) -> T:
        json_deserializable = load_json(json)
        obj = JsonDeserializer.__convert_from_deserializable(cls, json_deserializable)
        return obj

    def __convert_from_deserializable(cls: Type[T], json_deserializable: Any) -> T:
        if json_deserializable is None:
            return None
        
        if get_origin(cls) is list:
            arg_type = get_args(cls)[0]
            return [JsonDeserializer.__convert_from_deserializable(arg_type, item) for item in json_deserializable]
        elif get_origin(cls) is tuple:
            arg_types = get_args(cls)
            return tuple(JsonDeserializer.__convert_from_deserializable(arg_type, item) for arg_type, item in zip(arg_types, json_deserializable))
        elif get_origin(cls) is dict:
            key_type, value_type = get_args(cls)
            return {JsonDeserializer.__convert_from_deserializable(key_type, key): JsonDeserializer.__convert_from_deserializable(value_type, value) for key, value in json_deserializable.items()}
        elif is_dataclass(cls):
            type_hints = get_type_hints(cls)
            field_values = {}
            for field in fields(cls):
                field_name = field.name
                field_type = type_hints[field_name]
                field_value = json_deserializable[field_name]
                field_values[field_name] = JsonDeserializer.__convert_from_deserializable(field_type, field_value)
            return cls(**field_values)
        elif cls == str:
            return json_deserializable
        elif cls in (int, float):
            return cls(json_deserializable)
        elif cls == bool:
            return cls(json_deserializable)
        elif cls == datetime:
            return datetime.fromisoformat(json_deserializable)
        elif cls == date:
            return date.fromisoformat(json_deserializable)
        elif cls == time:
            return datetime.strptime(json_deserializable, "%H:%M:%S").time()
        else:
            raise TypeError(f"Unsupported type for json deserialization: {cls}")