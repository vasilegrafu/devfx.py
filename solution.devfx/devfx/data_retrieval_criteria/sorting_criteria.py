from dataclasses import dataclass
from typing import List

class SortingDirection:
    asc = 'asc'
    desc = 'desc'

@dataclass
class SortingCriterion(object):
    field: str = None
    direction: str = None

