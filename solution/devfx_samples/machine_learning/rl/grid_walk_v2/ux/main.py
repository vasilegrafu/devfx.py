import devfx.ux.windows.wx as ux

from devfx_samples.machine_learning.rl.grid_walk_v2.ux.main_window import MainWindow

"""------------------------------------------------------------------------------------------------
"""
class Application(ux.Application):
    def OnInit(self):
        super().OnInit()
        self.main_window = MainWindow(title="MainWindow",
                                      size=(1024, 768),
                                      align=(ux.CENTER, ux.CENTER))
        self.main_window.Show()
        return True

"""------------------------------------------------------------------------------------------------
"""
if __name__ == "__main__":
    application = Application()
    application.MainLoop()

