from devfx_samples.machine_learning.rl.grid_walk.ux2.main_window import MainWindow

"""------------------------------------------------------------------------------------------------
"""
def main(): 
    main_window = MainWindow(title="MainWindow", 
                             size=(80, 0),
                             minsize=(60, 20),
                             align=('center', 'center'),
                             state='normal')
    main_window.create()

if __name__ == "__main__":
    main()
