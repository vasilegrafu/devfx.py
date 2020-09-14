import wx
import devfx.core as core
from . import constants as consts
from . import layout
from . import events

"""------------------------------------------------------------------------------------------------
"""
class Canvas(wx.Panel, 
             layout.LayoutHandler,
             events.GenericEventHandler, 
             events.MouseEventHandler, 
             events.KeyboardEventHandler, 
             events.ApplicationEventHandler):
    def __init__(self, parent, id=wx.ID_ANY, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)
        layout.LayoutHandler.__init__(self)
        events.GenericEventHandler.__init__(self)
        events.MouseEventHandler.__init__(self)
        events.KeyboardEventHandler.__init__(self)
        events.ApplicationEventHandler.__init__(self)

        self.OnPaint += self.__on_paint
        self.OnSizeChanged += self.__on_size_changed

        self.BackgroundColour = wx.Colour(255,255,255,255)
    
    # ----------------------------------------------------------------
    def __on_paint(self, sender, event_args):
        cgc = CanvasGraphicsContext(self, self.BackgroundColour)
        (self.OnDraw)(self, core.Args(CGC=cgc))

    def UpdateDrawing(self):
        self.Refresh(eraseBackground=False)
        self.Update()

    # ----------------------------------------------------------------
    def __on_size_changed(self, sender, event_args):
        self.UpdateDrawing()

    # ----------------------------------------------------------------
    @property
    def OnDraw(self):
        return self.OnCallback('CBK_DRAW')

    @OnDraw.setter
    def OnDraw(self, value):
        pass


"""------------------------------------------------------------------------------------------------
"""
class CanvasGraphicsContext(object):
    def __init__(self, canvas, background_color):
        self.__canvas = canvas

        (width, height) = canvas.GetClientSize()
        if width <= 0:
            width = 1
        if height <= 0:
            height = 1
        bitmap = wx.Bitmap.FromRGBA(width, height, 
                                    red=background_color.red, green=background_color.green, blue=background_color.blue, alpha=background_color.alpha)
        dc = wx.BufferedPaintDC(canvas, bitmap)
        gc = wx.GraphicsContext.Create(dc)
        self.__gc = gc

    # ----------------------------------------------------------------
    @property
    def GC(self):
        return self.__gc

    # ----------------------------------------------------------------
    def GetSize(self):
        return self.__gc.GetSize()

    # ----------------------------------------------------------------
    def DrawLine(self, x, y, w, h, pen, brush):
        self.__gc.SetPen(pen) 
        self.__gc.SetBrush(brush)
        path = self.__gc.CreatePath()
        path.MoveToPoint(x, y)
        path.AddLineToPoint(w, h)
        self.__gc.StrokePath(path)

    def DrawRectangle(self, x, y, w, h, pen, brush):
        self.__gc.SetPen(pen) 
        self.__gc.SetBrush(brush)
        path = self.__gc.CreatePath()
        path.AddRectangle(x, y, w, h)
        self.__gc.StrokePath(path)
        self.__gc.FillPath(path)

    def DrawRoundedRectangle(self, x, y, w, h, r, pen, brush):
        self.__gc.SetPen(pen) 
        self.__gc.SetBrush(brush)
        path = self.__gc.CreatePath()
        path.AddRoundedRectangle(x, y, w, h, r)
        self.__gc.StrokePath(path)
        self.__gc.FillPath(path)

    def DrawCircle(self, x, y, r, pen, brush):
        self.__gc.SetPen(pen) 
        self.__gc.SetBrush(brush)
        path = self.__gc.CreatePath()
        path.AddCircle(x, y, r)
        self.__gc.StrokePath(path)
        self.__gc.FillPath(path)

    def DrawArc(self, x1, y1, x2, y2, r, pen, brush):
        self.__gc.SetPen(pen) 
        self.__gc.SetBrush(brush)
        path = self.__gc.CreatePath()
        path.AddArcToPoint(x1, y1, x2, y2, r)
        self.__gc.StrokePath(path)

    def DrawEllipse(self, x, y, w, h, pen, brush):
        self.__gc.SetPen(pen) 
        self.__gc.SetBrush(brush)
        path = self.__gc.CreatePath()
        path.AddEllipse(x, y, w, h)
        self.__gc.StrokePath(path)
        self.__gc.FillPath(path)

    # ----------------------------------------------------------------
    def DrawText(self, text, 
                       x, y, offx=0, offy=0, angle=0, 
                       font=None, 
                       colour=None,
                       anchor=None):
        if(font is None):
            font = self.__canvas.GetFont()
        if(colour is None):
            colour = self.__canvas.ForegroundColour
        self.__gc.SetFont(font, colour)
        
        (width, height, descent, external_eading) = self.__gc.GetFullTextExtent(text)
        x = x - width/2
        y = y - height/2
        if core.is_iterable(anchor):
            if(consts.LEFT in anchor):
                x = x + offx + width/2
            if(consts.RIGHT in anchor):
                x = x - offx - width/2
            if(consts.TOP in anchor):
               y = y + offy + height/2
            if(consts.BOTTOM in anchor):
               y = y - offy - height/2
        else:
            if(consts.LEFT == anchor):
                x = x + offx + width/2
            if(consts.RIGHT == anchor):
                x = x - offx - width/2
            if(consts.TOP == anchor):
                y = y + offy + height/2
            if(consts.BOTTOM == anchor):
                y = y - offy - height/2

        self.__gc.DrawText(str=text, x=x, y=y, angle=angle)
    

