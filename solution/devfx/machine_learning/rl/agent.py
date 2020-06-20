import devfx.exceptions as exps
import devfx.core as core
from .state_kind import StateKind

class Agent(object):
    def __init__(self, id, kind, environment, state, policy):
        self.__set_id(id=id)
        self.__set_kind(kind=kind)
        self.__set_environment(environment=environment)
        self.set_state(state=state)
        self.set_policy(policy=policy)

    """------------------------------------------------------------------------------------------------
    """
    def __set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    """------------------------------------------------------------------------------------------------
    """
    def __set_kind(self, kind):
        self.__kind = kind

    def get_kind(self):
        return self.__kind

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_environment(self, environment):
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
    def set_random_state(self):
        environment = self.get_environment()
        state = environment.get_random_state(agent_kind=self.get_kind())
        self.set_state(state=state)

    """------------------------------------------------------------------------------------------------
    """
    def set_policy(self, policy):
        self.__policy = policy

    def get_policy(self):
        return self.__policy

    """------------------------------------------------------------------------------------------------
    """
    def learn(self, state, action, next_state_and_reward):
        self.get_policy().learn(state=state, action=action, next_state_and_reward=next_state_and_reward)

    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self, action):
        if(action is None):
            raise exps.ArgumentNoneError()

        environment = self.get_environment()
        agent_kind = self.get_kind()
        state = self.get_state()

        is_in_terminal_state = state.kind == StateKind.TERMINAL
        if(is_in_terminal_state):
            raise exps.ApplicationError()

        next_state_and_reward = environment.get_next_state_and_reward(agent_kind=agent_kind, state=state, action=action)
        if(next_state_and_reward is None):
            return (state, action, None)

        (next_state, next_reward) = next_state_and_reward
        self.set_state(state=next_state)

        self.learn(state=state, action=action, next_state_and_reward=next_state_and_reward)

        return (state, action, next_state_and_reward)


    def do_random_action(self):
        environment = self.get_environment()
        agent_kind = self.get_kind()
        state = self.get_state()

        action = environment.get_random_action(agent_kind=agent_kind, state=state)
        (state, action, next_state_and_reward) = self.do_action(action=action)
        return (state, action, next_state_and_reward)
 
    def do_optimal_action(self):
        state = self.get_state()

        action = self.get_policy().get_optimal_action(state=state)
        (state, action, next_state_and_reward) = self.do_action(action=action)
        return (state, action, next_state_and_reward)

  


   