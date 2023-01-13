import random as rnd
from .double_tabular_policy import DoubleTabularPolicy

class DoubleQLearningPolicy(DoubleTabularPolicy):
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

            model1 = super().get_model()[1]
            model2 = super().get_model()[2]

            random_number = rnd.random()
            if(random_number < 0.5):
                state_action_value = model1.get_value_or_zero(state, action)
                max_action = model2.get_max_action(state=state)
                next_state_max_value = model2.get_max_value_or_zero(next_state)
                error = reward.get_value() + self.get_discount_factor()*next_state_max_value - state_action_value
                state_action_value = state_action_value + self.get_learning_rate()*error
                model1.set_value(state, action, state_action_value)
            else:
                state_action_value = model2.get_value_or_zero(state, action)
                next_state_max_value = model1.get_max_value_or_zero(next_state)
                error = reward.get_value() + self.get_discount_factor()*next_state_max_value - state_action_value
                state_action_value = state_action_value + self.get_learning_rate()*error
                model2.set_value(state, action, state_action_value)




