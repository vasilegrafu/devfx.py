from .environment import Environment

class ActionPolicy(object):
    def __init__(self, agent):
        self.__set_agent(agent=agent)

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_agent(self, agent):
        self.__agent = agent

    def get_agent(self):
        return self.__agent

