import devfx.exceptions as exps
from .training_log_item import TrainingLogItem

"""------------------------------------------------------------------------------------------------
"""
class TrainingLog(object):
    def __init__(self):
        self.__items = []

        self.__attr_list_cache = {}

    # ----------------------------------------------------------------
    @property
    def items(self):
        return self.__items

    @property
    def last_item(self):
        return self.__items[-1]

    def append_item(self, time_elapsed, iteration, epoch):
        if(len(self.items) == 0):
            time_delta = 0
        elif(len(self.items) >= 1):
            time_delta = time_elapsed - self.last_item.time_elapsed
        else:
            raise exps.NotSupportedError()

        training_log_item = TrainingLogItem(nr=(len(self.__items) + 1),
                                            time_elapsed=time_elapsed,
                                            time_delta=time_delta,
                                            iteration=iteration,
                                            epoch=epoch)
        self.__items.append(training_log_item)

    def clear(self):
        self.__items.clear()

    # ----------------------------------------------------------------
    def __getattr__(self, name):
        if(name[-len('_list'):] == '_list'):
            if(len(self.__items) == 0):
                raise exps.NotSupportedError()
            else:
                name2 = name[:-len('_list')]
                if(not hasattr(self.last_item, name2)):
                    raise exps.ArgumentError()
                if(name not in self.__attr_list_cache):
                    self.__attr_list_cache[name] = [getattr(_, name2) for _ in self.__items]
                else:
                    if(len(self.__items) != len(self.__attr_list_cache[name])):
                        self.__attr_list_cache[name] = [getattr(_, name2) for _ in self.__items]
                return self.__attr_list_cache[name]

