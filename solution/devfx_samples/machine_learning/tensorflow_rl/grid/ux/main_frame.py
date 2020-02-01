import wx
from .grid_view import GridView

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Centre()

        self.grid_view = GridView(parent=self, style=wx.SIMPLE_BORDER)
        self.button = wx.Button(self, label="Train")
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnButton)

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
            self.grid_view.Refresh()