from devfx_samples.ux.windows.app1.main_window import MainWindow


"""------------------------------------------------------------------------------------------------
"""
def main(): 
    main_window = MainWindow(title="MainWindow", 
                             align=('center', 'center'),
                             state='normal')
    main_window.create()

if __name__ == "__main__":
    main()
