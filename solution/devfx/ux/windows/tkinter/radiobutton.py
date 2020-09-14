import tkinter as tk
import tkinter.ttk as ttk
import devfx.core as core

from .ttkwidget import TtkWidget

class Radiobutton(TtkWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(cls=ttk.Radiobutton, parent=parent, **kwargs)






