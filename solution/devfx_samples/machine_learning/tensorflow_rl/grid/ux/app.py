import wx
from .main_frame import MainFrame

class App(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, title="RL", size=(1024, 768))
        self.frame.Show()
        return True