import tkinter as tk
import tkinter.ttk as ttk
import uuid
import devfx.core as core

from .widget import Widget

class TtkWidget(Widget):
    def __init__(self, cls, parent, **kwargs):
        super().__init__(cls=cls, parent=parent, **kwargs)


    """------------------------------------------------------------------------------------------------
    """
    def configure(self, **kwargs):
        for (key, value) in kwargs.items():
            super().inner.configure(**{key: value})

    """------------------------------------------------------------------------------------------------
    """
    class Style(object):
        def __init__(self, style_name):
            self._style = ttk.Style()
            self._style_name = style_name

        def configure(self, **kwargs):
            self._style.configure(self._style_name, **kwargs)

        def map(self, **kwargs):
            self._style.map(self._style_name, **kwargs)

        def lookup(self, option, default=None):
            return self._style.lookup(self._style_name, option=option, state=None, default=default)

    @property
    def style(self):
        if(super().inner['style'] == ''):
            super().inner['style'] = f'{id(self)}.{super().inner.winfo_class()}'
        return TtkWidget.Style(style_name=super().inner['style'])

    @style.setter   
    def style(self, value):
        super().inner['style'] = value









