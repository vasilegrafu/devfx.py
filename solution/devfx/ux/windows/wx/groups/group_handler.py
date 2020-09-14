class GroupHandler(object):
    def __init__(self):
        pass

    # ----------------------------------------------------------------
    def DisableChildren(self):
        children = self.GetChildren()
        for child in children:
            try:
                child.GetWindow().Enable(False)
            except:
                pass

    def EnableChildren(self):
        children = self.GetChildren()
        for child in children:
            try:
                child.GetWindow().Enable(True)
            except:
                pass