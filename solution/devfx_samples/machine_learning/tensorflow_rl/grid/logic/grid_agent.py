import numpy as np
import devfx.core as core
import devfx.machine_learning.tensorflow as ml

"""========================================================================================================
"""
class GridAgent(ml.rl.Agent):
    def __init__(self, name, environment):
        state = environment.get_random_non_terminal_state()
        action_policy=ml.rl.QPolicy()
        super().__init__(name=name, environment=environment, state=state, action_policy=action_policy)

        self.training_info_update = core.SignalHandlers()
        self.training_progress = core.SignalHandlers()

    """------------------------------------------------------------------------------------------------
    """
    def train(self, episodes, discount_factor, learning_rate):
        environment = self.get_environment()
        action_policy = self.get_action_policy()

        episode = 0
        while(episode < episodes):
            episode += 1
            self.set_state(state=environment.get_random_non_terminal_state())

            self.training_info_update(source=self, event_args=core.SignalArgs(message=f'[episode: {episode}]'))
            self.training_info_update(source=self, event_args=core.SignalArgs(message=f'- initial state: {self.get_state()}'))

            i = 0
            while(self.get_state().is_non_terminal()):
                i += 1
                action = action_policy.get_action(state=self.get_state())
                if(action is None):
                    (state, action, next_state) = self.do_random_action()
                else:
                    rv = np.random.uniform(size=1)
                    if(rv <= 1.0):
                        (state, action, next_state) = self.do_random_action()
                    else:
                        (state, action, next_state) = self.do_action()
                action_policy.update(state=state, action=action, next_state=next_state, discount_factor=discount_factor, learning_rate=learning_rate)

                if(self.get_state().is_non_terminal()):
                    self.training_info_update(source=self, event_args=core.SignalArgs(message=f'- move {i} to non-terminal state: {self.get_state()}'))
                else:
                    self.training_info_update(source=self, event_args=core.SignalArgs(message=f'- move {i} to terminal state: {self.get_state()}'))

                self.training_progress(source=self, event_args=core.SignalArgs(state=self.get_state()))
