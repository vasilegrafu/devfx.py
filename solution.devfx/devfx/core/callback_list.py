
class CallbackList(object):
    def __init__(self):
        self.__fns = []

    """------------------------------------------------------------------------------------------------
    """
    def add(self, fn):
        self.__fns.append(fn)
        return self

    def __iadd__(self, fn):
        return self.add(fn)


    def remove(self, fn):
        while fn in self.__fns:
            self.__fns.remove(fn)
        return self

    def __isub__(self, fn):
        return self.remove(fn)

    """------------------------------------------------------------------------------------------------
    """
    def __len__(self):
        return len(self.__fns)

    def __iter__(self):
        for fn in self.__fns:
            yield fn

    """------------------------------------------------------------------------------------------------
    """
    def __call__(self, *args, **kwargs):
        for fn in self.__fns:
            fn(*args, **kwargs)


