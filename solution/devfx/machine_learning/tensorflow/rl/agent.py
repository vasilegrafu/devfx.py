import devfx.exceptions as exps

class Agent(object):
    def __init__(self, name, environment, state, action_policy=None):
        self.set_name(name=name)
        self.set_environment(environment=environment)
        self.set_state(state=state)
        
        self.set_action_policy(action_policy=action_policy)

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
        if(environment is None):
            raise exps.ApplicationError()

        state = self.get_state()
        if(state is None):
            raise exps.ApplicationError()
        if(state.is_terminal()):
            raise exps.ApplicationError()

        action = environment.get_random_action(state=state)
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

        action_policy = self.get_action_policy()
        if(action_policy is None):
            raise exps.ApplicationError()
        
        action = action_policy.get_action(state=state)
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


        
