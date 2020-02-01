import devfx.core as core

class SignalArgs(object):
    def __init__(self, **kwargs):
        for karg in kwargs.keys():
            core.setattr(self, name=karg, value=kwargs[karg])


