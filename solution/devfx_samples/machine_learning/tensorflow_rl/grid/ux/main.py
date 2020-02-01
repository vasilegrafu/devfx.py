import wx
from devfx_samples.machine_learning.tensorflow_rl.grid.logic.trainer import Trainer

class GridView(wx.Panel):
    def __init__(self, trainer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trainer = trainer

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush(wx.Colour(255, 255, 255)))
        dc.Clear()
        

class MainPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.trainer = Trainer()

        self.grid_view = GridView(trainer=self.trainer, parent=self, style=wx.SIMPLE_BORDER)
        self.button = wx.Button(self, label="Train")
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        self.__do_layout()

    def __do_layout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.grid_view, proportion=1, flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.button)
        vsizer.Add(hsizer, proportion=0, flag=wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM | wx.LEFT | wx.RIGHT, border=10)
        self.SetSizer(vsizer)

    def OnButton(self, event):
        button = event.EventObject
        if(button is self.button):
            self.trainer.train()
            self.grid_view.Refresh()

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Centre()

        self.panel = MainPanel(self)

class App(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, title="RL", size=(1024, 768))
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()