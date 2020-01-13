
class Environment(object):
    def __init__(self):
        self.__model = None
        self.__agents = []

    """------------------------------------------------------------------------------------------------
    """ 
    def get_agents(self):
        return self.__agents

    def add_agent(self, agent):
        self.get_agents().append(agent)

    def remove_agent(self, agent):
        self.get_agents().remove(agent)

    """------------------------------------------------------------------------------------------------
    """ 
    def get_next_state_and_reward(self, state, action):
        next_state = None
        reward = None
        return (next_state, reward)