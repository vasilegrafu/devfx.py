import numpy as np
import scipy as sp
import devfx.exceptions as exps
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
    def get_random_state(self):
        return self._get_random_state()

    def _get_random_state(self):
        raise exps.NotImplementedError()


    def get_random_non_terminal_state(self):
        return self._get_random_non_terminal_state()

    def _get_random_non_terminal_state(self):
        raise exps.NotImplementedError()


    def get_random_terminal_state(self):
        return self._get_random_terminal_state()

    def _get_random_terminal_state(self):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def get_random_action(self, state):
        return self._get_random_action(state=state)

    def _get_random_action(self, state):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_state_kind(self, state):
        return state.kind

    def is_non_terminal_state(self, state):
        return state.is_non_terminal()

    def is_terminal_state(self, state):
        return state.is_terminal()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_state_reward(self, state):
        return state.reward

    """------------------------------------------------------------------------------------------------
    """ 
    def get_next_state(self, state, action):
        next_state = self._get_next_state(state=state, action=action)
        return next_state
        
    def _get_next_state(self, state, action):
        raise exps.NotImplementedError()


        








