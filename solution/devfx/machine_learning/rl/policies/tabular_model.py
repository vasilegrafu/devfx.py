class TabularModel():
    def __init__(self):
        self.__setup_table()
  
    """------------------------------------------------------------------------------------------------
    """ 
    def __setup_table(self):
        self.__table = {}
   
    def __get_table(self):
        return self.__table

    """------------------------------------------------------------------------------------------------
    """
    def get_sav_iterator(self):
        for state in self.__get_table():
            for action in self.__get_table()[state]:
                value = self.__get_table()[state][action]    
                yield (state, action, value)

    """------------------------------------------------------------------------------------------------
    """
    def get_states_count(self):
        return len(self.__get_table())

    def get_states(self):
        return list(self.__get_table().keys())

    def has_states(self):
        return len(self.__get_table()) >= 1

    def has_state(self, state):
        return state in self.__get_table()


    def get_actions_count(self, state):
        return len(self.__get_table()[state])

    def get_actions(self, state):
        return list(self.__get_table()[state].keys())

    def has_actions(self, state):
        return len(self.__get_table()[state]) >= 1

    def has_action(self, state, action):
        return action in self.__get_table()[state]


    def set_value(self, state, action, value):
        if(state not in self.__get_table()):
            self.__get_table()[state] = {}
        self.__get_table()[state][action] = value

    def get_value(self, state, action):
        return self.__get_table()[state][action]

    def get_value_or_none(self, state, action):
        action_values = self.__get_table().get(state)
        if(action_values is None):
            return None
        value = action_values.get(action)
        if(value is None):
            return None
        return value

    def get_value_or_zero(self, state, action):
        action_values = self.__get_table().get(state)
        if(action_values is None):
            return 0
        value = action_values.get(action)
        if(value is None):
            return 0
        return value

    def has_value(self, state, action):
        if(state not in self.__get_table()):
            return False
        if(action not in self.__get_table()[state]):
            return False
        return True


    def get_max_value(self, state):
        return max(self.__get_table()[state].values())

    def get_min_value(self, state):
        return min(self.__get_table()[state].values())

    def get_avg_value(self, state):
        return sum(self.__get_table()[state].values())/len(self.__get_table()[state])


    def get_action_values(self, state):
        return self.__get_table()[state]

    def get_action_values_or_none(self, state):
        action_values = self.__get_table().get(state)
        if(action_values is None):
            return None
        return action_values



                


