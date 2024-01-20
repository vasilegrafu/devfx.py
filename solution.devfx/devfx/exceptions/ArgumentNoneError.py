from .BaseError import BaseError

class ArgumentNoneError(Exception):
    def __init__(self, message=None, data={}, inner=None):
        BaseError.__init__(self, message=message, data=data, inner=inner)