import tkinter as tk
import tkinter.ttk as ttk
import devfx.core as core

from . import variables

from .ttkwidget import TtkWidget

class Spinbox(TtkWidget):
    def __init__(self, parent, min, max, inc, initial_value, **kwargs):
        self._value = variables.DoubleVar(value=initial_value)
        super().__init__(cls=tk.Spinbox, parent=parent, from_=min, to=max, increment=inc, textvariable=self._value, **kwargs)

    """------------------------------------------------------------------------------------------------
    """
    @property
    def value(self):
        return self._value.get()

    @value.setter   
    def value(self, value):
        return self._value.set(value)

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def on_command(self):
        if('_on_command' not in self.__dict__):
            self._on_command = core.CallbackList()
            super().inner['command'] = lambda: self._on_command(self, core.Args(value=self.value))
        return self._on_command

    @on_command.setter   
    def on_command(self, value):
        self._on_command = value