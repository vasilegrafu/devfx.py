from dataclasses import dataclass
from typing import List

class FilteringOperator:
    equals = 'equals'
    not_equals = 'not_equals'
    greater_than = 'greater_than'
    greater_than_or_equal = 'greater_than_or_equal'
    less_than = 'less_than'
    less_than_or_equal = 'less_than_or_equal'
    contains = 'contains'
    starts_with = 'starts_with'
    ends_with = 'ends_with'

@dataclass
class FilteringCriterion:
    field: str = None
    operator: str = None
    value: str = None


    
