import devfx.ux.windows as windows

class GridFrame(windows.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.size = (100, 100)

        
