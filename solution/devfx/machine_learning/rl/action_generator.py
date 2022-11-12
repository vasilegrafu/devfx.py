import numpy as np
import random as rnd
import devfx.exceptions as excps
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

    @property
    def name(self):
        return self.__name


    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value


    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        raise excps.NotImplementedError()

"""================================================================================================
"""
class DiscreteRange(Range):
    def __init__(self, name, value):
         super().__init__(name=name, value=value)

    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        value = rnd.choice(self.value)
        return value


"""================================================================================================
"""
class ContinousRange(Range):
    def __init__(self, name, value):
         super().__init__(name=name, value=value)

    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        value = rnd.uniform(self.value)
        return value
    

"""================================================================================================
"""
class ActionGenerator(object):
    def __init__(self, ranges):
        self.__set_ranges(ranges=ranges)

    """------------------------------------------------------------------------------------------------
    """
    def __set_ranges(self, ranges):
        self.__ranges = ranges

    @property
    def ranges(self):
        return self.__ranges


    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        return self._get_random()

    def _get_random(self):
        return Action(value=np.array([r.get_random() for r in self.ranges]))