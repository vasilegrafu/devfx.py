import wx
import time as t
import random as rnd
from devfx_samples.machine_learning.tensorflow_rl.grid.logic.grid_environment import GridEnvironment
from devfx_samples.machine_learning.tensorflow_rl.grid.logic.grid_agent import GridAgent

class GridView(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush(wx.Colour(rnd.randint(0, 255), 255, 255)))
        dc.Clear()
        
