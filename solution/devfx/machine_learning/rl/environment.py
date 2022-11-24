import numpy as np
import random as rnd
import devfx.exceptions as ex
import devfx.core as core
from .agent import Agent
from .state_kind import StateKind

class Environment(object):
    def __init__(self):
        self.__agents_container = {}

    """------------------------------------------------------------------------------------------------
    """ 
    def create(self, *args, **kwargs):
        self._create(*args, **kwargs)

    def _create(self, *args, **kwargs):
        raise ex.NotImplementedError()

    
    def setup(self, *args, **kwargs):
        return self._setup(*args, **kwargs)

    def _setup(self, *args, **kwargs):
        raise ex.NotImplementedError()     


    def destroy(self, *args, **kwargs):
        self._destroy(*args, **kwargs)

    def _destroy(self, *args, **kwargs):
        for agent in self.get_agents():                
            self.remove_agent(agent)

    """------------------------------------------------------------------------------------------------
    """ 
    def add_agent(self, agent):
        if(agent.id in self.__agents_container):
            raise ex.ApplicationError()
        self.__agents_container[agent.id] = agent
        self.on_added_agent(agent)

    def on_added_agent(self, agent):
        self._on_added_agent(agent=agent)
        
    def _on_added_agent(self, agent):
        raise ex.NotImplementedError()


    def remove_agent(self, agent):
        if(agent.get_id() not in self.__agents_container):
            raise ex.ApplicationError()
        self.__agents_container.pop(agent.get_id())
        self.on_removed_agent(agent)

    def on_removed_agent(self, agent):
        self._on_removed_agent(agent=agent)
        
    def _on_removed_agent(self, agent):
        raise ex.NotImplementedError()


    def get_agents(self):
        agents = [agent for (_, agent) in self.__agents_container.items()]
        return agents


    def get_agents_like(self, kind):
        agents = [agent for (_, agent) in self.__agents_container.items() if(agent.kind == kind)]
        return agents

    def get_agents_not_like(self, kind):
        agents = [agent for (_, agent) in self.__agents_container.items() if(agent.kind != kind)]
        return agents


    def exists_agent(self, id):
        if(id not in self.__agents_container):
            return False
        return True


    def get_agent(self, id):
        if(id not in self.__agents_container):
            raise ex.ApplicationError()
        agent = self.__agents_container[id]
        return agent

    def get_other_agents(self, id):
        agents = [agent for (key, agent) in self.__agents_container.items() if(agent.get_id() != id)]
        return agents

    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self, agent, action):   
        state = agent.get_state()

        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise ex.ApplicationError()

        (reward, next_state) = self.get_reward_and_next_state(agent=agent, action=action)
        agent.set_state(state=next_state)

        agent.learn(state=state, action=action, reward=reward, next_state=next_state)

        return (state, action, (reward, next_state))

    def do_random_action(self, agent):
        action = self.get_random_action(agent=agent)
        if(action is None):
            state = agent.get_state()
            return (state, None, (None, None))
        (state, action, (reward, next_state)) = self.do_action(agent=agent, action=action)
        return (state, action, (reward, next_state))
 
    def do_optimal_action(self, agent):
        (action, value) = agent.policy.get_optimal_action(state=agent.get_state())
        if(action is None):
            state = agent.get_state()
            return (state, None, (None, None))
        (state, action, (reward, next_state)) = self.do_action(agent=agent, action=action)
        return (state, action, (reward, next_state))

    """------------------------------------------------------------------------------------------------
    """ 
    def do_iteration(self, agents=None):
        self._do_iteration(agents=agents)

    def _do_iteration(self, agents=None):
        if(any(agent.is_in_terminal_state() for agent in self.get_agents())):
            self.setup()
        else:
            if(agents is None):
                agents = self.get_agents()
            for agent in agents:
                if(agent.is_in_non_terminal_state()):
                    rv = np.random.uniform(size=1)
                    if(rv <= agent.get_iteration_randomness()):
                        self.do_random_action(agent=agent)
                    else:
                        self.do_optimal_action(agent=agent)
                elif(agent.is_in_terminal_state()):
                    pass
                else:
                    raise ex.NotSupportedError()


    def do_iterations(self, n, agents=None):
        self._do_iterations(n=n, agents=agents)

    def _do_iterations(self, n, agents=None):
        for i in range(0, n):
            self.do_iteration(agents=agents)

    """------------------------------------------------------------------------------------------------
    """ 
    def get_reward_and_next_state(self, agent, action):
        is_terminal_state = agent.get_state().kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise ex.ApplicationError()
        
        (reward, next_state) = self._get_reward_and_next_state(agent=agent, action=action)
        return (reward, next_state)
        
    def _get_reward_and_next_state(self, agent, action):
        raise ex.NotImplementedError()


    def get_next_state(self, agent, action):
        (reward, next_state) = self.get_reward_and_next_state(agent=agent, action=action)
        return next_state

    def get_reward(self, agent, action):
        (reward, next_state) = self.get_reward_and_next_state(agent=agent, action=action)
        return reward
        
    """------------------------------------------------------------------------------------------------
    """ 
    def get_random_action(self, agent):
        return self._get_random_action(agent=agent)

    def _get_random_action(self, agent):
        raise ex.NotImplementedError()


