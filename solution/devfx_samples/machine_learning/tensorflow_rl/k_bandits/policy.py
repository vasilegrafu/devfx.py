from .environment import Environment

class Policy(object):
    def __init__(self, environment):
        self.__environment = environment

    """------------------------------------------------------------------------------------------------
    """ 
    def get_environment(self):
        return self.__environment

