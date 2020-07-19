import tkinter as tk
import tkinter.ttk as ttk
import devfx.core as core

from .widget import Widget

class Label(Widget):
    def __init__(self, parent, **kwargs):
        super().__init__(cls=ttk.Label, parent=parent, **kwargs)

        self.__init_event_handlers()

    def __init_event_handlers(self):
        pass   


