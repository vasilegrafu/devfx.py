import tkinter as tk
import tkinter.ttk as ttk
import devfx.core as core

from .widget import Widget

class TkWidget(Widget):
    def __init__(self, cls, parent, **kwargs):
        super().__init__(cls=cls, parent=parent, **kwargs)
    
    """------------------------------------------------------------------------------------------------
    """
    def configure(self, **kwargs):
        for key, value in kwargs.items():
            super().inner.configure(**{key: value})