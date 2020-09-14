import tkinter as tk
import tkinter.ttk as ttk
import devfx.core as core

from .tkwidget import TkWidget

class Canvas(TkWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(cls=tk.Canvas, parent=parent, **kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def create_text(self, x, y, text, **kwargs):
        return super().inner.create_text(x, y, text=text, **kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def create_line(self, x1, y1, x2, y2, **kwargs):
        return super().inner.create_line(x1, y1, x2, y2, **kwargs)

    def create_lines(self, coords, **kwargs):
        return super().inner.create_line(coords, **kwargs)

    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        return super().inner.create_rectangle(x1, y1, x2, y2, **kwargs)

    def create_circle(self, x, y, r, **kwargs):
        x1 = x - r
        y1 = y - r
        x2 = x + r
        y2 = y + r
        return super().inner.create_oval(x1, y1, x2, y2, **kwargs)

    def create_ellipse(self, x, y, rx, ry, **kwargs):
        x1 = x - rx
        y1 = y - ry
        x2 = x + rx
        y2 = y + ry
        return super().inner.create_oval(x1, y1, x2, y2, **kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def delete_item(self, id):
        return super().inner.delete(id)

    def delete_all_items(self):
        return super().inner.delete('all')



