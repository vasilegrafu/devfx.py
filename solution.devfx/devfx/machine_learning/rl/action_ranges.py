import numpy as np
import random as rnd
import devfx.exceptions as excs
import devfx.core as core
from .action import Action

"""================================================================================================
"""
class Range(object):
    def __init__(self, name, value):
        self.__set_name(name=name)
        self.__set_value(value=value)

    """------------------------------------------------------------------------------------------------
    """
    def __set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        return self._get_random()

    def _get_random(self):
        raise ex.NotImplementedError()

"""================================================================================================
"""
class DiscreteRange(Range):
    def __init__(self, name, value):
         super().__init__(name=name, value=value)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random(self):
        random_value = rnd.choice(self.get_value())
        return random_value


"""================================================================================================
"""
class ContinousRange(Range):
    def __init__(self, name, value):
         super().__init__(name=name, value=value)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random(self):
        random_value = rnd.uniform(self.get_value())
        return random_value
    

"""================================================================================================
"""
class ActionRanges(object):
    def __init__(self, ranges):
        self.__set_ranges(ranges=ranges)

    """------------------------------------------------------------------------------------------------
    """
    def __set_ranges(self, ranges):
        self.__ranges = { range.get_name(): range for range in ranges }

    def get_ranges(self):
        return self.__ranges

    def get_range(self, name):
        return self.__ranges[name]