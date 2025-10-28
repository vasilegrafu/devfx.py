from dataclasses import dataclass
from typing import List

@dataclass
class PaginationCriteria:
    page_size: int = None
    page_number: int = None

    
