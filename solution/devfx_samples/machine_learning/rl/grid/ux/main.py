import wx
from devfx_samples.machine_learning.rl.grid.ux.main_frame import MainFrame

"""------------------------------------------------------------------------------------------------
"""
class App(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)
        self.frame.Show()
        return True

"""------------------------------------------------------------------------------------------------
"""
if __name__ == "__main__":
    app = App()
    app.MainLoop()

