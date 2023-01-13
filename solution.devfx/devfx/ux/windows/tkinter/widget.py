import tkinter as tk
import tkinter.ttk as ttk
import devfx.core as core

class Widget(object):
    def __init__(self, cls, parent, **kwargs):
        self._parent = parent
        self._inner = cls(parent.inner, **kwargs)

        self._event_handlers = {}

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def parent(self):
        return self._parent
    
    @parent.setter   
    def parent(self, value):
        self._parent = value

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def inner(self):
        return self._inner
    
    @inner.setter   
    def inner(self, value):
        self._inner = value

    """------------------------------------------------------------------------------------------------
    """ 
    def place(self, **kwargs):
        self.inner.pack(**kwargs)

    def pack(self, **kwargs):
        self.inner.pack(**kwargs)

    def grid(self, **kwargs):
        self.inner.grid(**kwargs)

    def configure_grid_row(self, index, **kwargs):
        self.inner.rowconfigure(index=index, **kwargs)

    def configure_grid_column(self, index, **kwargs):
        self.inner.columnconfigure(index=index, **kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def configure(self, **kwargs):
        self.inner.configure(**kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def __setattr__(self, name, value):
        if(('_inner' in self.__dict__) and (name in self.__dict__['_inner'].keys())):
            self.__dict__['_inner'][name] = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if(('_inner' in self.__dict__) and (name in self.__dict__['_inner'].keys())):
            return self.__dict__['_inner'][name]
        else:
            return self.__dict__[name]

    
    @property
    def width(self):
        return self.inner.winfo_width()
    
    @width.setter   
    def width(self, value):
        self.inner['width'] = value

    
    @property
    def height(self):
        return self.inner.winfo_height()
    
    @height.setter   
    def height(self, value):
        self.inner['height'] = value

    """------------------------------------------------------------------------------------------------
    """
    def on_event(self, name):
        if(name not in self._event_handlers):
            self._event_handlers[name] = core.CallbackList()
            self.inner.bind(name, lambda e: self._event_handlers[name](self, e))
        return self._event_handlers[name]

    #
    @property
    def on_mouse_click(self):
        if('_on_mouse_click' not in self.__dict__):
            self._on_mouse_click = core.CallbackList()
            self.on_event('<ButtonPress-1>').add(self._on_mouse_click)
            self.on_event('<ButtonPress-2>').add(self._on_mouse_click)
            self.on_event('<ButtonPress-3>').add(self._on_mouse_click)
        return self._on_mouse_click

    @on_mouse_click.setter   
    def on_mouse_click(self, value):
        self._on_mouse_click = value

    #
    @property
    def on_mouse_double_click(self):
        if('_on_mouse_double_click' not in self.__dict__):
            self._on_mouse_double_click = core.CallbackList()
            self.on_event('<Double-Button-1>').add(self._on_mouse_double_click)
            self.on_event('<Double-Button-2>').add(self._on_mouse_double_click)
            self.on_event('<Double-Button-3>').add(self._on_mouse_double_click)
        return self._on_mouse_double_click

    @on_mouse_double_click.setter   
    def on_mouse_double_click(self, value):
        self._on_mouse_double_click = value
    
    #
    @property
    def on_mouse_triple_click(self):
        if('_on_mouse_triple_click' not in self.__dict__):
            self._on_mouse_triple_click = core.CallbackList()
            self.on_event('<Triple-Button-1>').add(self._on_mouse_triple_click)
            self.on_event('<Triple-Button-2>').add(self._on_mouse_triple_click)
            self.on_event('<Triple-Button-3>').add(self._on_mouse_triple_click)
        return self._on_mouse_triple_click

    @on_mouse_triple_click.setter   
    def on_mouse_triple_click(self, value):
        self._on_mouse_triple_click = value

    #
    @property
    def on_mouse_down(self):
        return self.on_mouse_click

    @on_mouse_down.setter   
    def on_mouse_down(self, value):
        self.on_mouse_click = value

    #
    @property
    def on_mouse_drag(self):
        if('_on_mouse_drag' not in self.__dict__):
            self._on_mouse_drag = core.CallbackList()
            self.on_event('<B1-Motion>').add(self._on_mouse_drag)
            self.on_event('<B2-Motion>').add(self._on_mouse_drag)
            self.on_event('<B3-Motion>').add(self._on_mouse_drag)
        return self._on_mouse_drag

    @on_mouse_drag.setter   
    def on_mouse_drag(self, value):
        self._on_mouse_drag = value

    #
    @property
    def on_mouse_move(self):
        if('_on_mouse_move' not in self.__dict__):
            self._on_mouse_move = core.CallbackList()
            self.on_event('<Motion>').add(self._on_mouse_move)
        return self._on_mouse_move

    @on_mouse_move.setter   
    def on_mouse_move(self, value):
        self._on_mouse_move = value

    #
    @property
    def mouse_up(self):
        if('_mouse_up' not in self.__dict__):
            self._mouse_up = core.CallbackList()
            self.on_event('<ButtonRelease-1>').add(self._mouse_up)
            self.on_event('<ButtonRelease-2>').add(self._mouse_up)
            self.on_event('<ButtonRelease-3>').add(self._mouse_up)
        return self._mouse_up

    @mouse_up.setter   
    def mouse_up(self, value):
        self._mouse_up = value

    #
    @property
    def on_mouse_move(self):
        if('_on_mouse_move' not in self.__dict__):
            self._on_mouse_move = core.CallbackList()
            self.on_event('<Motion>').add(self._on_mouse_move)
        return self._on_mouse_move

    @on_mouse_move.setter   
    def on_mouse_move(self, value):
        self._on_mouse_move = value

    #
    @property
    def on_mouse_enter(self):
        if('_on_mouse_enter' not in self.__dict__):
            self._on_mouse_enter = core.CallbackList()
            self.on_event('<Enter>').add(self._on_mouse_enter)
        return self._on_mouse_enter

    @on_mouse_enter.setter   
    def on_mouse_enter(self, value):
        self._on_mouse_enter = value

    #
    @property
    def on_mouse_leave(self):
        if('_on_mouse_leave' not in self.__dict__):
            self._on_mouse_leave = core.CallbackList()
            self.on_event('<Leave>').add(self._on_mouse_leave)
        return self._on_mouse_leave

    @on_mouse_leave.setter   
    def on_mouse_leave(self, value):
        self._on_mouse_leave = value

    #
    @property
    def on_got_focus(self):
        if('_on_got_focus' not in self.__dict__):
            self._on_got_focus = core.CallbackList()
            self.on_event('<FocusIn>').add(self._on_got_focus)
        return self._on_got_focus

    @on_got_focus.setter   
    def on_got_focus(self, value):
        self._on_got_focus = value

    #
    @property
    def on_lost_focus(self):
        if('_on_lost_focus' not in self.__dict__):
            self._on_lost_focus = core.CallbackList()
            self.on_event('<FocusOut>').add(self._on_lost_focus)
        return self._on_lost_focus

    @on_lost_focus.setter   
    def on_lost_focus(self, value):
        self._on_lost_focus = value

    #
    @property
    def on_key_press(self):
        if('_on_key_press' not in self.__dict__):
            self._on_key_press = core.CallbackList()
            self.on_event('<KeyPress>').add(self._on_key_press)
        return self._on_key_press

    @on_key_press.setter   
    def on_key_press(self, value):
        self._on_key_press = value

    #
    @property
    def on_key_release(self):
        if('_on_key_release' not in self.__dict__):
            self._on_key_release = core.CallbackList()
            self.on_event('<KeyRelease>').add(self._on_key_release)
        return self._on_key_release

    @on_key_release.setter   
    def on_key_release(self, value):
        self._on_key_release = value

    #
    @property
    def on_enter_key_press(self):
        if('_on_enter_key_press' not in self.__dict__):
            self._on_enter_key_press = core.CallbackList()
            self.on_event('<Return>').add(self._on_enter_key_press)
        return self._on_enter_key_press

    @on_enter_key_press.setter   
    def on_enter_key_press(self, value):
        self._on_enter_key_press = value


    #
    @property
    def on_configure(self):
        if('_on_configure' not in self.__dict__):
            self._on_configure = core.CallbackList()
            self.on_event('<Configure>').add(self._on_configure)
        return self._on_configure

    @on_configure.setter   
    def on_configure(self, value):
        self._on_configure = value

    #
    @property
    def on_destroy(self):
        if('_on_destroy' not in self.__dict__):
            self._on_destroy = core.CallbackList()
            self.on_event('<Destroy>').add(self._on_destroy)
        return self._on_destroy

    @on_destroy.setter   
    def on_destroy(self, value):
        self._on_destroy = value


    """------------------------------------------------------------------------------------------------
    """
    def update(self):
        self.inner.update()

    def update_idletasks(self):
        self.inner.update_idletasks()




