import devfx.ux.windows as windows

from .secondary_window import SecondaryWindow

class MainWindow(windows.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = windows.Label(parent=self, text='Press the button :)')
        self.label.grid(row=0, column=0)

        self.button = windows.Button(parent=self, text=':)')
        self.button.grid(row=0, column=1)
        self.button.on_mouse_click += self.__button__on_mouse_click

    def __button__on_mouse_click(self, source, event_args):
        window = SecondaryWindow(parent=self, title="Window")
        window.create()
