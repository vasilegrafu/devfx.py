import numpy as np
import scipy as sp
import devfx.exceptions as exceps
import devfx.core as core

class Environment(object):
    def __init__(self):
        self.__set_agents(agents=[])

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_agents(self, agents):
        self.__agents = agents

    def get_agents(self):
        return self.__agents

    def add_agent(self, agent):
        self.get_agents().append(agent)

    def remove_agent(self, agent):
        self.get_agents().remove(agent)

    """------------------------------------------------------------------------------------------------
    """
    def is_valid_state(self, state):
        return self._is_valid_state(state=state) 

    def _is_valid_state(self, state):
        pass 

    def validate_state(self, state):
        if(not self.is_valid_state(state=state)):
            raise exceps.ApplicationError()


    def is_valid_action(self, action):
        return self._is_valid_action(action=action) 
  
    def _is_valid_action(self, action):
        pass

    def validate_action(self, action):
        if(not self.is_valid_action(action=action)):
            raise exceps.ApplicationError()


    def is_valid_state_action(self, state, action):
        if(not self.is_valid_state(state=state)):
            return False
        if(not self.is_valid_action(action=action)):
            return False
        actions = self.get_actions(state)
        if(action not in actions):
            return False
        return True

    def validate_state_action(self, state, action):
        if(not self.is_valid_state_action(state=state, action=action)):
            raise exceps.ApplicationError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_states(self):
        states = self._get_states()
        if(not core.is_iterable(states)):
            raise exceps.ArgumentError()
        return states

    def _get_states(self):
        raise exceps.NotImplementedError()  

    def get_random_state(self):
        states = self.get_states()
        state = states[np.random.choice(len(states), size=1)[0]]
        return state

    """------------------------------------------------------------------------------------------------
    """ 
    def is_non_terminal_state(self, state):
        self.validate_state(state=state)
        exists_actions = self.exists_actions(state)
        is_non_terminal_state = exists_actions
        return is_non_terminal_state

    def is_terminal_state(self, state):
        self.validate_state(state=state)
        is_terminal_state = not self.is_non_terminal_state(state)
        return is_terminal_state

    def get_non_terminal_states(self): 
        states = [state for state in self.get_states() if self.is_non_terminal_state(state)]
        return states

    def get_terminal_states(self): 
        states = [state for state in self.get_states() if self.is_terminal_state(state)]
        return states

    def get_random_non_terminal_state(self):
        states = self.get_non_terminal_states()
        state = states[np.random.choice(len(states), size=1)[0]]
        return state

    def get_random_terminal_state(self):
        states = self.get_terminal_states()
        state = states[np.random.choice(len(states), size=1)[0]]
        return state

    """------------------------------------------------------------------------------------------------
    """   
    def get_reward(self, state):
        self.validate_state(state=state)
        reward = self._get_reward(state=state)
        return reward
        
    def _get_reward(self, state):
        raise exceps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_actions(self, state):
        self.validate_state(state=state)
        actions = self._get_actions(state=state)
        if(not core.is_iterable(actions)):
            raise exceps.ArgumentError()
        return actions
        
    def _get_actions(self, state):
        raise exceps.NotImplementedError()

    def exists_actions(self, state):
        self.validate_state(state=state)
        actions = self.get_actions(state)
        if(actions is None):
            return False
        if(len(actions) == 0):
            return False
        return True

    def get_random_action(self, state):
        self.validate_state(state=state)
        actions = self.get_actions(state=state)
        action = actions[np.random.choice(len(actions), size=1)[0]]
        return action
       
    """------------------------------------------------------------------------------------------------
    """ 
    def get_next_state(self, state, action):
        self.validate_state_action(state, action)
        next_state = self._get_next_state(state=state, action=action)
        return next_state
        
    def _get_next_state(self, state, action):
        raise exceps.NotImplementedError()

    def get_next_state_and_reward(self, state, action):
        self.validate_state(state=state)
        self.validate_action(action=action)
        state = self.get_next_state(state=state, action=action)
        reward = self.get_reward(state=state)
        return (state, reward)


        








