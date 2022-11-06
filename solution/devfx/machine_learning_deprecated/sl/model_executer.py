import tensorflow as tf
import devfx.exceptions as excps
import devfx.core as core

class ModelExecuter(object):
    """------------------------------------------------------------------------------------------------
    """
    def __init__(self, path):
        self.__model = tf.saved_model.load(path)

    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def import_from(cls, path):
        return ModelExecuter(path=path)

    """------------------------------------------------------------------------------------------------
    """
    def __getattr__(self, attr):
        if(self.__model is None):
            raise excps.ValueError()
        return core.getattr(self.__model, attr)



