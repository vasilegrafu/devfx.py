import numpy as np
import devfx.exceptions as exps
import devfx.core as core

class Agent(object):
    def __init__(self, name, environment, state, policy=None):
        self.set_name(name=name)
        self.set_environment(environment=environment)
        self.set_state(state=state)
        self.set_policy(policy=policy)

        self.training_info_update = core.SignalHandlers()
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
        return (state, action, next_state)
  
    def do_action(self):
        (state, action, next_state) = self.get_next_state()
        self.set_state(state=next_state)
        return (state, action, next_state)


    """------------------------------------------------------------------------------------------------
    """
    @property
    def training_info_update(self):
        return self.__training_info_update

    @training_info_update.setter
    def training_info_update(self, signal_handlers):
        self.__training_info_update = signal_handlers


    @property
    def training_progress(self):
        return self.__training_progress

    @training_progress.setter
    def training_progress(self, signal_handlers):
        self.__training_progress = signal_handlers


    class TrainingParameters(object):
        def __init__(self):
            self.episodes = None
            self.episode = None
            self.episode_step = None
            self.epsilon = None

        @property
        def episodes(self):
            return self.__episodes

        @episodes.setter
        def episodes(self, episodes):
            self.__episodes = episodes


        @property
        def episode(self):
            return self.__episode

        @episode.setter
        def episode(self, episode):
            self.__episode = episode


        @property
        def episode_step(self):
            return self.__episode_step

        @episode_step.setter
        def episode_step(self, episode_step):
            self.__episode_step = episode_step


        @property
        def epsilon(self):
            return self.__epsilon

        @epsilon.setter
        def epsilon(self, epsilon):
            self.__epsilon = epsilon


    def train(self, episodes, epsilon):
        environment = self.get_environment()
        policy = self.get_policy()

        training_parameters = Agent.TrainingParameters()
        training_parameters.episodes = episodes
        training_parameters.episode = 0
        training_parameters.episode_step = 0
        training_parameters.epsilon = epsilon

        while(training_parameters.episode < training_parameters.episodes):
            training_parameters.episode += 1
            training_parameters.episode_step = 0

            self.set_state(state=environment.get_random_non_terminal_state())

            self.training_status(source=self, signal_args=core.SignalArgs(training_parameters=training_parameters, state=self.get_state()))

            while(self.get_state().is_non_terminal()):
                action = policy.get_action(state=self.get_state())
                if(action is None):
                    (state, action, next_state) = self.do_random_action()
                else:
                    rv = np.random.uniform(size=1)
                    if(rv <= training_parameters.epsilon):
                        (state, action, next_state) = self.do_random_action()
                    else:
                        (state, action, next_state) = self.do_action()
                policy.update(state=state, action=action, next_state=next_state)

                training_parameters.episode_step += 1

                self.training_status(source=self, signal_args=core.SignalArgs(training_parameters=training_parameters, state=self.get_state()))

        
