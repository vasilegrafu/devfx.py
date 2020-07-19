import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

class Window(object):
    def __init__(self, parent=None, 
                       title='', 
                       size=(None, None), 
                       minsize=(None, None), 
                       align=('center', 'center'), 
                       state='normal', 
                       **kwargs):
        if(parent is None):
            self.__inner = tk.Tk(**kwargs)
        else:
            self.__inner = tk.Toplevel(master=parent.inner, **kwargs)

        self.title = title
        self.state = state
        self.size = size
        self.minsize = minsize
        self.align = align
  
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
    def create(self):
        self.__inner.mainloop()

    def hide(self):
        self.__inner.withdraw()

    def show(self):
        self.__inner.deiconify()

    def destroy(self):
        self.__inner.destroy()

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def title(self):
        return self.__inner.title
    
    @title.setter   
    def title(self, value):
        self.__inner.title(value)

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def state(self):
        return self.__inner.state
    
    @state.setter   
    def state(self, value):
        self.__inner.state(value)

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def size(self):
        self.__inner.update_idletasks()
        windowwidth_pixels = self.__inner.winfo_width()
        windowheight_pixels = self.__inner.winfo_height()

        charwidth_pixels = tkfont.nametofont('TkDefaultFont').measure('M')
        charheight_pixels = tkfont.nametofont('TkDefaultFont').metrics('linespace')

        windowwidth_chars = windowwidth_pixels/charwidth_pixels
        windowheight_chars = windowheight_pixels/charheight_pixels

        return (windowwidth_chars, windowheight_chars)
    
    @size.setter   
    def size(self, value):
        if(value == (None, None)):
            return

        windowwidth_chars = 0 if(value[0] is None) else value[0]
        windowheight_chars = 0 if(value[1] is None) else value[1]

        charwidth_pixels = tkfont.nametofont('TkDefaultFont').measure('M')
        charheight_pixels = tkfont.nametofont('TkDefaultFont').metrics('linespace')

        windowwidth_pixels = int(windowwidth_chars*charwidth_pixels)
        windowheight_pixels = int(windowheight_chars*charheight_pixels)

        self.__inner.geometry(f'{windowwidth_pixels}x{windowheight_pixels}')
        self.__inner.update_idletasks()

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def minsize(self):
        self.__inner.update_idletasks()
        minwindowwidth_pixels = self.__inner.minsize()[0]
        minwindowheight_pixels = self.__inner.minsize()[1]

        charwidth_pixels = tkfont.nametofont('TkDefaultFont').measure('M')
        charheight_pixels = tkfont.nametofont('TkDefaultFont').metrics('linespace')

        minwindowwidth_chars = minwindowwidth_pixels/charwidth_pixels
        minwindowheight_chars = minwindowheight_pixels/charheight_pixels

        return (minwindowwidth_chars, minwindowheight_chars)
    
    @minsize.setter   
    def minsize(self, value):
        if(value == (None, None)):
            return

        minwindowwidth_chars = 0 if(value[0] is None) else value[0]
        minwindowheight_chars = 0 if(value[1] is None) else value[1]

        charwidth_pixels = tkfont.nametofont('TkDefaultFont').measure('M')
        charheight_pixels = tkfont.nametofont('TkDefaultFont').metrics('linespace')

        minwindowwidth_pixels = int(minwindowwidth_chars*charwidth_pixels)
        minwindowheight_pixels = int(minwindowheight_chars*charheight_pixels)

        self.__inner.minsize(minwindowwidth_pixels, minwindowheight_pixels)
        self.__inner.update_idletasks()

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def align(self):
        return self.__align
    
    @align.setter   
    def align(self, value):
        self.__align = value

        horizontal_align = self.__align[0]
        vertical_align = self.__align[1]

        self.__inner.update_idletasks()
        windowwidth_pixels = self.__inner.winfo_width()
        windowheight_pixels = self.__inner.winfo_height()

        screenwidth_pixels = self.__inner.winfo_screenwidth()
        screenheight_pixels = self.__inner.winfo_screenheight()

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
        
        self.__inner.geometry(f'+{xposition_pixels}+{yposition_pixels}')
        self.__inner.update_idletasks()



