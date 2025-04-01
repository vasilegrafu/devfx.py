from .tabular_policy import TabularPolicy

class QLearningPolicy(TabularPolicy):
    def __init__(self, discount_factor, learning_rate):
        super().__init__()

        self.set_discount_factor(discount_factor=discount_factor)
        self.set_learning_rate(learning_rate=learning_rate)

    """------------------------------------------------------------------------------------------------
    """ 
    def set_discount_factor(self, discount_factor):
        self.__discount_factor = discount_factor

    def get_discount_factor(self):
        return self.__discount_factor

    """------------------------------------------------------------------------------------------------
    """ 
    def set_learning_rate(self, learning_rate):
        self.__learning_rate = learning_rate

    def get_learning_rate(self):
        return self.__learning_rate

    """------------------------------------------------------------------------------------------------
    """
    def _learn(self, transitions):
        for transition in transitions:
            (state, action, (reward, next_state)) = transition

            value = super().get_value_or_zero(state, action)
            if(not super().has_state(state=next_state)):
                td = reward.get_value() - value   
            else:
                td = reward.get_value() + self.get_discount_factor()*super().get_value(state=next_state, action=super().get_optimal_action(state=next_state)) - value
            value = value + self.get_learning_rate()*td
            super().set_value(state, action, value)



