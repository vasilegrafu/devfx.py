import tkinter as tk
import tkinter.ttk as ttk
import devfx.core as core

from .widget import Widget

class Button(Widget):
    def __init__(self, parent, **kwargs):
        super().__init__(cls=ttk.Button, parent=parent, **kwargs)

        self.__init_event_handlers()

    def __init_event_handlers(self):
        self.on_command = core.EventHandler()
        self.on_mouse_click.add(self.on_command)
            self.on_key_press.add(self.on_command) 







