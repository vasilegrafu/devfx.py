class Args(object):
    def __init__(self, **kwargs):
        for karg in kwargs.keys():
            setattr(self, karg, kwargs[karg])
