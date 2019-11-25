import devfx.exceptions as exceps
import devfx.reflection as refl
from .training_log_item import TrainingLogItem
from .training_log_items import TrainingLogItems

"""------------------------------------------------------------------------------------------------
"""
class TrainingLog(object):
    def __init__(self):
        self.__items = []

    # ----------------------------------------------------------------
    def append(self, item):
        self.__items.append(item)

    def __delitem__(self, key):
        del self.__items[key]

    def clear(self):
        self.__items.clear()

    def __getitem__(self, key):
        item_or_items = self.__items[key]
        if(not refl.is_iterable(item_or_items)):
            return item_or_items
        else:
            return TrainingLogItems(item_or_items)

    def __len__(self):
        return len(self.__items)

