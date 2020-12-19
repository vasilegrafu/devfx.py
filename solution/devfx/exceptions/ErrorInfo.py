import sys
import traceback

class ErrorInfo(object):
    @staticmethod
    def get():
        (exc_type, exc_value, exc_traceback) = sys.exc_info()
        return traceback.format_exception(exc_type, exc_value, exc_traceback)

    @staticmethod
    def print(file=sys.stdout):
        exc_info = ErrorInfo.get()
        print(exc_info, file=file)

