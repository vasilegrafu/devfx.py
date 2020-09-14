import devfx.exceptions as exps
import devfx.core as core
from .state_kind import StateKind

class Agent(object):
    def __init__(self, id, name, kind, environment, state=None, policy=None):
        self.__set_id(id=id)
        self.__set_name(name=name)
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
    def __set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

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


    def is_in_non_terminal_state(self):
        state = self.get_state()
        is_in_non_terminal_state = state.kind == StateKind.NON_TERMINAL
        return is_in_non_terminal_state

    def is_in_terminal_state(self):
        state = self.get_state()
        is_in_terminal_state = state.kind == StateKind.TERMINAL
        return is_in_terminal_state

    """------------------------------------------------------------------------------------------------
    """
    def set_policy(self, policy):
        self.__policy = policy

    def get_policy(self):
        return self.__policy


    def share_policy_with(self, agent):
        policy = self.get_policy()
        agent.set_policy(policy=policy)


    def transfer_policy_to(self, agent):
        policy = self.get_policy()
        self.set_policy(policy=None)
        agent.set_policy(policy=policy)

    def transfer_policy_from(self, agent):
        policy = agent.get_policy()
        agent.set_policy(policy=None)
        self.set_policy(policy=policy)


    def copy_policy_to(self, agent):
        policy = self.get_policy().copy()
        agent.set_policy(policy=policy)

    def copy_policy_from(self, agent):
        policy = agent.get_policy().copy()
        self.set_policy(policy=policy)

        
    """------------------------------------------------------------------------------------------------
    """
    def learn(self, state, action, next_state_and_reward):
        self.get_policy().learn(state=state, action=action, next_state_and_reward=next_state_and_reward)

    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self, action):
        environment = self.get_environment()
        state = self.get_state()

        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise exps.ApplicationError()

        next_state_and_reward = environment.get_next_state_and_reward(agent=self, state=state, action=action)
        if(next_state_and_reward is None):
            return (state, action, None)

        (next_state, next_reward) = next_state_and_reward
        self.set_state(state=next_state)

        self.learn(state=state, action=action, next_state_and_reward=next_state_and_reward)

        return (state, action, next_state_and_reward)

    def do_random_action(self):
        environment = self.get_environment()
        state = self.get_state()

        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise exps.ApplicationError()

        action = environment.get_random_action(agent=self, state=state)
        (state, action, next_state_and_reward) = self.do_action(action=action)
        return (state, action, next_state_and_reward)
 
    def do_optimal_action(self):
        state = self.get_state()

        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise exps.ApplicationError()

        action = self.get_policy().get_optimal_action(state=state)
        if(action is None):
            (state, action, next_state_and_reward) = (state, None, None)
        else:
            (state, action, next_state_and_reward) = self.do_action(action=action)
        return (state, action, next_state_and_reward)

    
    """------------------------------------------------------------------------------------------------
    """
    def do_iteration(self, *args, **kwargs):
        self._do_iteration(*args, **kwargs)

    def _do_iteration(self, *args, **kwargs):
        raise exps.NotImplementedError()

  


   