from dataclasses import dataclass
from typing import List

@dataclass
class BaseResponse(object):
    error_messages: List[str] = None