import devfx.exceptions as exps
from .environment import Environment
from .random_action_policy import RandomActionPolicy

class Agent(object):
    def __init__(self, environment, action_policy=None, state=None):
        self.set_environment(environment=environment)

        if(action_policy is None):
            action_policy = RandomActionPolicy(environment=environment)
        self.set_action_policy(action_policy=action_policy)
        
        if(state is None):
            state = environment.get_random_non_terminal_state()
        self.set_state(state=state)

    """------------------------------------------------------------------------------------------------
    """ 
    def set_environment(self, environment):
        self.__environment = environment
        self.__environment.add_agent(self)

    def get_environment(self):
        return self.__environment

    """------------------------------------------------------------------------------------------------
    """
    def set_action_policy(self, action_policy):
        self.__action_policy = action_policy

    def get_action_policy(self):
        return self.__action_policy

    """------------------------------------------------------------------------------------------------
    """
    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

    """------------------------------------------------------------------------------------------------
    """ 
    def get_random_next_state(self):
        environment = self.get_environment()
        state = self.get_state()
        if(state.is_terminal()):
            raise exps.ApplicationError()
        action = environment.get_random_action(state=state)
        next_state = environment.get_next_state(state=state, action=action)
        return next_state

    def get_next_state(self):
        environment = self.get_environment()
        state = self.get_state()
        if(state.is_terminal()):
            raise exps.ApplicationError()
        action = self.get_action_policy().get_action(state=state)
        next_state = environment.get_next_state(state=state, action=action)
        return next_state

    """------------------------------------------------------------------------------------------------
    """ 
    def do_random_action(self):
        next_state = self.get_random_next_state()
        self.set_state(state=next_state)

    def do_action(self):
        next_state = self.get_next_state()
        self.set_state(state=next_state)


        
