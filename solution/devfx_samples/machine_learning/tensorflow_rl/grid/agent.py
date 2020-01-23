import devfx.machine_learning.tensorflow as ml

class GridAgent(ml.rl.Agent):
    def __init__(self, environment, action_policy=None, state=None):
        super().__init__(environment=environment, action_policy=action_policy, state=state)

