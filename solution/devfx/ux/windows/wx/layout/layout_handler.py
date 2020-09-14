class LayoutHandler(object):
    def __init__(self):
        pass

    # ----------------------------------------------------------------
    def AddToSizer(self, sizer, *args, **kwargs):
        sizer.Add(self, *args, **kwargs)
        return self

    def RemoveFromSizer(self, sizer, *args, **kwargs):
        sizer.Remove(self, *args, **kwargs)
        return self

