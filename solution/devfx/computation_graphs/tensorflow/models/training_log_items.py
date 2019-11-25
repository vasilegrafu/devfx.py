import devfx.exceptions as exceps

"""------------------------------------------------------------------------------------------------
"""
class TrainingLogItems(object):
    def __init__(self, items):
        self.__items = items

    # ----------------------------------------------------------------
    def __getitem__(self, key):
        return self.__items[key]

    def __len__(self):
        return len(self.__items)

    # ----------------------------------------------------------------
    def __getattr__(self, name):
        return [getattr(_, name) for _ in self.__items]

