import tkinter as tk
import tkinter.ttk as ttk
import devfx.core as core

from .ttkwidget import TtkWidget

class Checkbutton(TtkWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(cls=ttk.Checkbutton, parent=parent, **kwargs)


