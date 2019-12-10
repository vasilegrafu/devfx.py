import tensorflow as tf
import devfx.exceptions as exceps
import devfx.reflection as refl

class ModelExecuter(object):
    def __init__(self, path=None):
        if(path is not None):
            self.import_from(path=path)

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    """------------------------------------------------------------------------------------------------
    """
    def import_from(self, path):
        pass

    """------------------------------------------------------------------------------------------------
    """
    def evaluate(self, x):
        pass

