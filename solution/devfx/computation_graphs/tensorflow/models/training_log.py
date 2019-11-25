import devfx.exceptions as exceps
import devfx.reflection as refl
from .training_log_item import TrainingLogItem

"""------------------------------------------------------------------------------------------------
"""
class TrainingLog(object):
    def __init__(self):
        self.__items = []


    def append(self, item):
        self.__items.append(item)


    def __delitem__(self, key):
        del self.__items[key]

    def clear(self):
        self.__items.clear()


    class __TrainingLogItemsProxy(object):
        def __init__(self, items):
            self.__items = items

        def __getattr__(self, name):
            return [getattr(_, name) for _ in self.__items]

    def __getitem__(self, key):
        item_or_items = self.__items[key]
        if(not refl.is_iterable(item_or_items)):
            return item_or_items
        else:
            return TrainingLog.__TrainingLogItemsProxy(item_or_items)


    def __len__(self):
        return len(self.__items)

