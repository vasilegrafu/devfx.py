import devfx.core as core

class Widget(object):
    def __init__(self, cls, parent, **kwargs):
        self.__inner = cls(parent.inner, **kwargs)

        self.__init_event_handlers()

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def inner(self):
        return self.__inner
    
    @inner.setter   
    def inner(self, value):
        self.__inner = value

    """------------------------------------------------------------------------------------------------
    """ 
    def pack(self, **kwargs):
        self.__inner.pack(**kwargs)

    def grid(self, **kwargs):
        self.__inner.grid(**kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def on_event(self, name):
        if(not hasattr(self, '_Widget__event_handlers')):
            self.__event_handlers = {}
        if(name not in self.__event_handlers):
            self.__event_handlers[name] = core.EventHandler()
            self.inner.bind(name, lambda e: self.__event_handlers[name](self, e))
        return self.__event_handlers[name]

    def __init_event_handlers(self):
        # 
        self.on_mouse_click = core.EventHandler()
        self.on_event('<ButtonPress-1>').add(self.on_mouse_click)
        self.on_event('<ButtonPress-2>').add(self.on_mouse_click)
        self.on_event('<ButtonPress-3>').add(self.on_mouse_click)

        self.on_mouse_double_click = core.EventHandler()
        self.on_event('<Double-Button-1>').add(self.on_mouse_double_click)
        self.on_event('<Double-Button-2>').add(self.on_mouse_double_click)
        self.on_event('<Double-Button-3>').add(self.on_mouse_double_click)

        self.on_mouse_triple_click = core.EventHandler()
        self.on_event('<Triple-Button-1>').add(self.on_mouse_triple_click)
        self.on_event('<Triple-Button-2>').add(self.on_mouse_triple_click)
        self.on_event('<Triple-Button-3>').add(self.on_mouse_triple_click)

        self.on_mouse_down = self.on_mouse_click

        self.on_mouse_drag = core.EventHandler()
        self.on_event('<B1-Motion>').add(self.on_mouse_drag)
        self.on_event('<B2-Motion>').add(self.on_mouse_drag)
        self.on_event('<B3-Motion>').add(self.on_mouse_drag)

        self.on_mouse_move = core.EventHandler()
        self.on_event('<Motion>').add(self.on_mouse_move)
        self.on_event('<Motion>').add(self.on_mouse_move)
        self.on_event('<Motion>').add(self.on_mouse_move)

        self.mouse_up = core.EventHandler()
        self.on_event('<ButtonRelease-1>').add(self.mouse_up)
        self.on_event('<ButtonRelease-2>').add(self.mouse_up)
        self.on_event('<ButtonRelease-3>').add(self.mouse_up)

        self.on_mouse_enter = core.EventHandler()
        self.on_event('<Enter>').add(self.on_mouse_enter)

        self.on_mouse_leave = core.EventHandler()
        self.on_event('<Leave>').add(self.on_mouse_leave)

        #
        self.on_got_focus = core.EventHandler()
        self.on_event('<FocusIn>').add(self.on_got_focus)

        self.on_lost_focus = core.EventHandler()
        self.on_event('<FocusOut>').add(self.on_lost_focus)

        self.on_key_press = core.EventHandler()
        self.on_event('<KeyPress>').add(self.on_key_press)

        self.on_key_release = core.EventHandler()
        self.on_event('<KeyRelease>').add(self.on_key_release)

        #
        self.on_configure = core.EventHandler()
        self.on_event('<Configure>').add(self.on_configure)

        #
        self.on_destroy = core.EventHandler()
        self.on_event('<Destroy>').add(self.on_destroy)






