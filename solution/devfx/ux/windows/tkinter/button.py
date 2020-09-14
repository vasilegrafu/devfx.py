import tkinter as tk
import tkinter.ttk as ttk
import devfx.core as core

from .ttkwidget import TtkWidget

class Button(TtkWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(cls=ttk.Button, parent=parent, **kwargs)

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def on_command(self):
        if('_on_command' not in self.__dict__):
            self._on_command = core.CallbackList()
            super().inner['command'] = lambda: self._on_command(self)
        return self._on_command

    @on_command.setter   
    def on_command(self, value):
        self._on_command = value







