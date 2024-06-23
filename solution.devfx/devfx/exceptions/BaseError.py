
class BaseError(Exception):
    def __init__(self, message=None, data={}, inner=None):
        Exception.__init__(self)

        self.__message = message
        self.__data = data
        self.__inner = inner

    @property
    def message(self):
        return self.__message

    @property
    def data(self):
        return self.__data

    @property
    def inner(self):
        return self.__inner

    def __str__(self):
        return self.message


