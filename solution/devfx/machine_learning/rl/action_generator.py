import numpy as np
import random as rnd
import devfx.exceptions as ex
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

    def __get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__get_name()

    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    def __get_value(self):
        return self.__value

    @property
    def value(self):
        return self.__get_value()

    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        raise ex.NotImplementedError()

"""================================================================================================
"""
class DiscreteRange(Range):
    def __init__(self, name, value):
         super().__init__(name=name, value=value)

    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        random_value = rnd.choice(self.value)
        return random_value


"""================================================================================================
"""
class ContinousRange(Range):
    def __init__(self, name, value):
         super().__init__(name=name, value=value)

    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        random_value = rnd.uniform(self.value)
        return random_value
    

"""================================================================================================
"""
class ActionGenerator(object):
    def __init__(self, ranges):
        self.__set_ranges(ranges=ranges)

    """------------------------------------------------------------------------------------------------
    """
    def __set_ranges(self, ranges):
        self.__ranges = ranges

    def __get_ranges(self):
        return self.__ranges

    @property
    def ranges(self):
        return self.__get_ranges()

    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        return self._get_random()

    def _get_random(self):
        return Action(name='unknown', value=[range.get_random() for range in self.__get_ranges()])