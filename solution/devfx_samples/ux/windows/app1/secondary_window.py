import devfx.ux.windows as windows

class SecondaryWindow(windows.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = windows.Label(parent=self, text='Press the button :)')
        self.label.grid(row=0, column=0)

        self.button1 = windows.Button(parent=self, text=':(')
        self.button1.grid(row=0, column=1)
        self.button1.on_mouse_click += self.__button1__on_mouse_click

        self.button2 = windows.Button(parent=self, text=':)')
        self.button2.grid(row=1, column=1)
        self.button2.on_mouse_click += self.__button2__on_mouse_click

    def __button1__on_mouse_click(self, source, event_args):
        self.hide()

    def __button2__on_mouse_click(self, source, event_args):
        self.show()