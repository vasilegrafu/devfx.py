import wx
from . import constants as consts

class Application(wx.App):
    def __init__(self):
        super().__init__()

    def OnInit(self):
        consts.BLACK.SetRGBA(wx.Colour(0,0,0).GetRGBA())
        consts.BLACK_PEN.SetColour(consts.BLACK)
        consts.BLACK_BRUSH.SetColour(consts.BLACK)

        consts.WHITE.SetRGBA(wx.Colour(255,255,255).GetRGBA())
        consts.WHITE_PEN.SetColour(consts.WHITE)
        consts.WHITE_BRUSH.SetColour(consts.WHITE)
        
        consts.RED.SetRGBA(wx.Colour(255,0,0).GetRGBA())
        consts.RED_PEN.SetColour(consts.RED)
        consts.RED_BRUSH.SetColour(consts.RED)
        
        consts.LIME.SetRGBA(wx.Colour(0,255,0).GetRGBA())
        consts.LIME_PEN.SetColour(consts.LIME)
        consts.LIME_BRUSH.SetColour(consts.LIME)
        
        consts.BLUE.SetRGBA(wx.Colour(0,0,255).GetRGBA())
        consts.BLUE_PEN.SetColour(consts.BLUE)
        consts.BLUE_BRUSH.SetColour(consts.BLUE)
        
        consts.YELLOW.SetRGBA(wx.Colour(255,255,0).GetRGBA())
        consts.YELLOW_PEN.SetColour(consts.YELLOW)
        consts.YELLOW_BRUSH.SetColour(consts.YELLOW)
        
        consts.CYAN.SetRGBA(wx.Colour(0,255,255).GetRGBA())
        consts.CYAN_PEN.SetColour(consts.CYAN)
        consts.CYAN_BRUSH.SetColour(consts.CYAN)
        
        consts.MAGENTA.SetRGBA(wx.Colour(255,0,255).GetRGBA())
        consts.MAGENTA_PEN.SetColour(consts.MAGENTA)
        consts.MAGENTA_BRUSH.SetColour(consts.MAGENTA)
        
        consts.SILVER.SetRGBA(wx.Colour(192,192,192).GetRGBA())
        consts.SILVER_PEN.SetColour(consts.SILVER)
        consts.SILVER_BRUSH.SetColour(consts.SILVER)
        
        consts.GRAY.SetRGBA(wx.Colour(128,128,128).GetRGBA())
        consts.GRAY_PEN.SetColour(consts.GRAY)
        consts.GRAY_BRUSH.SetColour(consts.GRAY)
        
        consts.MAROON.SetRGBA(wx.Colour(128,0,0).GetRGBA())
        consts.MAROON_PEN.SetColour(consts.MAROON)
        consts.MAROON_BRUSH.SetColour(consts.MAROON)
        
        consts.OLIVE.SetRGBA(wx.Colour(128,128,0).GetRGBA())
        consts.OLIVE_PEN.SetColour(consts.OLIVE)
        consts.OLIVE_BRUSH.SetColour(consts.OLIVE)

        consts.GREEN.SetRGBA(wx.Colour(0,128,0).GetRGBA())
        consts.GREEN_PEN.SetColour(consts.GREEN)
        consts.GREEN_BRUSH.SetColour(consts.GREEN)

        consts.PURPLE.SetRGBA(wx.Colour(128,0,128).GetRGBA())
        consts.PURPLE_PEN.SetColour(consts.PURPLE)
        consts.PURPLE_BRUSH.SetColour(consts.PURPLE)

        consts.TEAL.SetRGBA(wx.Colour(0,128,128).GetRGBA())
        consts.TEAL_PEN.SetColour(consts.TEAL)
        consts.TEAL_BRUSH.SetColour(consts.TEAL)

        consts.NAVY.SetRGBA(wx.Colour(0,0,128).GetRGBA())
        consts.NAVY_PEN.SetColour(consts.NAVY)
        consts.NAVY_BRUSH.SetColour(consts.NAVY)

