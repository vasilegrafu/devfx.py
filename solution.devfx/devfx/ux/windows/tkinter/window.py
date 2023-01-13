import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
import devfx.core as core

class Window(object):
    def __init__(self, parent=None, 
                       title='', 
                       size=(None, None), 
                       minsize=(None, None), 
                       align=('center', 'center'), 
                       state='normal', 
                       **kwargs):
        if(parent is None):
            self._inner = tk.Tk(**kwargs)
        else:
            self._inner = tk.Toplevel(master=parent.inner, **kwargs)

        self.title = title
        self.state = state
        self.size = size
        self.minsize = minsize
        self.align = align
  
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
    def create(self):
        self.inner.mainloop()

    def hide(self):
        self.inner.withdraw()

    def show(self):
        self.inner.deiconify()

    def destroy(self):
        self.inner.destroy()

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def title(self):
        return self.inner.title
    
    @title.setter   
    def title(self, value):
        self.inner.title(value)

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def state(self):
        return self.inner.state
    
    @state.setter   
    def state(self, value):
        self.inner.state(value)

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def size(self):
        self.inner.update_idletasks()

        windowwidth_pixels = self.inner.winfo_width()
        windowheight_pixels = self.inner.winfo_height()

        return (windowwidth_pixels, windowheight_pixels)
    
    @size.setter   
    def size(self, value):
        if(value == (None, None)):
            return

        windowwidth_pixels = value[0]
        windowheight_pixels = value[1]
        self.inner.geometry(f'{windowwidth_pixels}x{windowheight_pixels}')

        self.inner.update_idletasks()

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def minsize(self):
        self.inner.update_idletasks()

        minwindowwidth_pixels = self.inner.minsize()[0]
        minwindowheight_pixels = self.inner.minsize()[1]

        return (minwindowwidth_pixels, minwindowheight_pixels)
    
    @minsize.setter   
    def minsize(self, value):
        if(value == (None, None)):
            return

        minwindowwidth_pixels = value[0]
        minwindowheight_pixels = value[1]
        self.inner.minsize(minwindowwidth_pixels, minwindowheight_pixels)

        self.inner.update_idletasks()

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def align(self):
        return self._align
    
    @align.setter   
    def align(self, value):
        self._align = value

        horizontal_align = self._align[0]
        vertical_align = self._align[1]

        self.inner.update_idletasks()
        windowwidth_pixels = self.inner.winfo_width()
        windowheight_pixels = self.inner.winfo_height()

        screenwidth_pixels = self.inner.winfo_screenwidth()
        screenheight_pixels = self.inner.winfo_screenheight()

        if(horizontal_align == 'left'):
            xposition_pixels = 0
        if(horizontal_align == 'center'):
            xposition_pixels = int(screenwidth_pixels/2 - windowwidth_pixels/2)
        if(horizontal_align == 'right'):
            xposition_pixels = int(screenwidth_pixels - windowwidth_pixels)

        if(vertical_align == 'top'):
            yposition_pixels = 0
        if(vertical_align == 'center'):
            yposition_pixels = int(screenheight_pixels/2 - windowheight_pixels/2)
        if(vertical_align == 'bottom'):
            yposition_pixels = int(screenheight_pixels - windowheight_pixels)
        
        self.inner.geometry(f'+{xposition_pixels}+{yposition_pixels}')
        self.inner.update_idletasks()

    """------------------------------------------------------------------------------------------------
    """
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
    def update(self):
        self.inner.update()

    def update_idletasks(self):
        self.inner.update_idletasks()

    
