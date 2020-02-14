import numpy as np
import devfx.exceptions as exps
import devfx.core as core

class Agent(object):
    def __init__(self, name, environment, state, policy=None):
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
    def set_policy(self, policy):
        self.__policy = policy

    def get_policy(self):
        return self.__policy

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
        if(environment is None):
            raise exps.ApplicationError()

        state = self.get_state()
        if(state is None):
            raise exps.ApplicationError()
        if(state.is_terminal()):
            raise exps.ApplicationError()

        action = environment.get_random_action(state=state)
        if(action is None):
            return (state, None, None)
        else:
            next_state = environment.get_next_state(state=state, action=action)
            return (state, action, next_state)

    def get_next_state(self):
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
            next_state = environment.get_next_state(state=state, action=action)
            return (state, action, next_state)

    """------------------------------------------------------------------------------------------------
    """ 
    def do_random_action(self):
        (state, action, next_state) = self.get_random_next_state()
        self.set_state(state=next_state)
        self.get_policy().update(state=state, action=action, next_state=next_state)
        return (state, action, next_state)
  
    def do_action(self):
        (state, action, next_state) = self.get_next_state()
        self.set_state(state=next_state)
        self.get_policy().update(state=state, action=action, next_state=next_state)
        return (state, action, next_state)


    """------------------------------------------------------------------------------------------------
    """
    @property
    def training_status(self):
        return self.__training_status

    @training_status.setter
    def training_status(self, signal_handlers):
        self.__training_status = signal_handlers


    class TrainingParameters(object):
        def __init__(self):
            self.episode_count = None
            self.episode_number = None
            self.episode_action_number = None
            self.epsilon = None

        @property
        def episode_count(self):
            return self.__episode_count

        @episode_count.setter
        def episode_count(self, value):
            self.__episode_count = value


        @property
        def episode_number(self):
            return self.__episode_number

        @episode_number.setter
        def episode_number(self, value):
            self.__episode_number = value


        @property
        def episode_action_number(self):
            return self.__episode_action_number

        @episode_action_number.setter
        def episode_action_number(self, value):
            self.__episode_action_number = value


        @property
        def epsilon(self):
            return self.__epsilon

        @epsilon.setter
        def epsilon(self, value):
            self.__epsilon = value


    def train(self, episode_count, epsilon):
        environment = self.get_environment()

        training_parameters = Agent.TrainingParameters()
        training_parameters.episode_count = episode_count
        training_parameters.episode_number = 0
        training_parameters.episode_action_number = 0
        training_parameters.epsilon = epsilon

        while(training_parameters.episode_number < training_parameters.episode_count):
            training_parameters.episode_number += 1
            training_parameters.episode_action_number = 0

            self.set_state(state=environment.get_random_non_terminal_state())
            
            self.training_status(source=self, signal_args=core.SignalArgs(training_parameters=training_parameters))

            while(self.get_state().is_non_terminal()):
                rv = np.random.uniform(size=1)
                if(rv <= training_parameters.epsilon):
                    self.do_random_action()
                else:
                    self.do_action()

                training_parameters.episode_action_number += 1

                self.training_status(source=self, signal_args=core.SignalArgs(training_parameters=training_parameters))

        
