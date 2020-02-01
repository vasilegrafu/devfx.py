from .. import objects

class SignalArgs(object):
    def __init__(self, **kwargs):
        for karg in kwargs.keys():
            objects.setattr(self, name=karg, value=kwargs[karg])


