import numpy as np
import devfx.exceptions as exps
import devfx.core as core

class Agent(object):
    def __init__(self, name, environment, state=None, policy=None):
        self.set_name(name=name)
        self.set_environment(environment=environment)
        self.set_state(state=state)
        self.set_policy(policy=policy)

        self.training_status = core.SignalHandlers()

    """------------------------------------------------------------------------------------------------
    """
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    """------------------------------------------------------------------------------------------------
    """ 
    def set_environment(self, environment):
        self.__environment = environment
                
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
    def set_policy(self, policy):
        self.__policy = policy

    def get_policy(self):
        return self.__policy

    """------------------------------------------------------------------------------------------------
    """ 
    def get_random_next_state_and_reward(self):
        environment = self.get_environment()
        if(environment is None):
            raise exps.ApplicationError()

        state = self.get_state()
        if(state is None):
            raise exps.ApplicationError()
        if(state.is_terminal()):
            raise exps.ApplicationError()

        action = environment.get_random_action(agent=self)
        if(action is None):
            return (state, None, None)
        else:
            (next_state, reward) = environment.get_next_state_and_reward(agent=self, action=action)
            return (state, action, next_state, reward)

    def get_next_state_and_reward(self):
        environment = self.get_environment()
        if(environment is None):
            raise exps.ApplicationError()

        state = self.get_state()
        if(state is None):
            raise exps.ApplicationError()
        if(state.is_terminal()):
            raise exps.ApplicationError()

        policy = self.get_policy()
        if(policy is None):
            raise exps.ApplicationError()
        
        action = policy.get_action(state=state)
        if(action is None):
            return (state, None, None)
        else:
            (next_state, reward) = environment.get_next_state_and_reward(agent=self, action=action)
            return (state, action, next_state, reward)

    """------------------------------------------------------------------------------------------------
    """ 
    def do_random_action(self):
        (state, action, next_state, reward) = self.get_random_next_state_and_reward()

        self.set_state(state=next_state)

        policy = self.get_policy()
        if(policy is None):
            raise exps.ApplicationError()
        policy.update(state=state, action=action, next_state=next_state, reward=reward)

        return (state, action, next_state, reward)
  
    def do_action(self):
        (state, action, next_state, reward) = self.get_next_state_and_reward()

        self.set_state(state=next_state)

        policy = self.get_policy()
        if(policy is None):
            raise exps.ApplicationError()
        policy.update(state=state, action=action, next_state=next_state, reward=reward)

        return (state, action, next_state, reward)


   