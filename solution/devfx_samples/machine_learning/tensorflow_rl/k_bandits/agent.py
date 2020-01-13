from .environment import Environment

class Agent(object):
    def __init__(self, environment):
        self.__environment = environment
        self.__environment.add_agend(self)
        self.__state = None
        self.__action_policy = None

    """------------------------------------------------------------------------------------------------
    """ 
    def get_environment(self):
        return self.__environment

    def get_state(self):
        return self.__state

    def get_action_policy(self):
        return self.__action_policy

    """------------------------------------------------------------------------------------------------
    """ 
    def perform_next_action(self):
        next_action = self.get_action_policy().get_next_action()
        state = self.get_state()
        (next_state, reward) = self.get_environment().get_next_state_and_reward(state, next_action)
        self.__state = next_state
        self.get_action_policy().set(next_state, reward)
