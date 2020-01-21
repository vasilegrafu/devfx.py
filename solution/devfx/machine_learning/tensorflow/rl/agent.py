import devfx.exceptions as exps
from .environment import Environment

class Agent(object):
    def __init__(self, environment, state=None):
        self.__set_environment(environment=environment)
        self.set_state(state=state)

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_environment(self, environment):
        self.__environment = environment
        self.__environment.add_agent(self)

    def get_environment(self):
        return self.__environment

    """------------------------------------------------------------------------------------------------
    """
    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self, action):
        environment = self.get_environment()
        state = self.get_state()
        if(environment.is_terminal_state(state=state)):
            return
        next_state = environment.get_next_state(state=state, action=action)
        self.set_state(state=next_state)

    def do_random_action(self):
        environment = self.get_environment()
        state = self.get_state()
        if(environment.is_terminal_state(state=state)):
            return
        action = environment.get_random_action(state=state)
        next_state = environment.get_next_state(state=state, action=action)
        self.set_state(state=next_state)
        
