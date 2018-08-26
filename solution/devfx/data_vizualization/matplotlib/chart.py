import devfx.exceptions as exceptions

class Chart(object):
    def __init__(self, figure=None, axes=None, title=None, grid=None):                              
        if(figure is None):
            raise exceptions.ArgumentNoneError()
        self.figure = figure
        
        if(axes is None):
            raise exceptions.ArgumentNoneError()
        self.axes = axes
        
        if(title is not None):
            self.set_title(title)
                                 
        if(grid is None):
            self.set_grid(True)
        else:
            self.set_grid(False)
            
            
    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def figure(self):
        return self.__figure
    
    @figure.setter   
    def figure(self, figure):
        self.__figure = figure
        

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def figure(self):
        return self.__figure
    
    @figure.setter   
    def figure(self, figure):
        self.__figure = figure
      
      
    @property
    def axes(self):
        return self.__axes
    
    @axes.setter   
    def axes(self, axes):
        self.__axes = axes
        
    """------------------------------------------------------------------------------------------------
    """ 
    def get_title(self):
        return self.axes.get_title()
        
    def title(self):
        return self.get_title()

    def set_title(self, *args, **kwargs):
        self.axes.set_title(*args, **kwargs)

    """------------------------------------------------------------------------------------------------
    """  
    def get_grid(self):
        return self.axes.get_grid()
        
    def grid(self):
        return self.get_grid()
    
    def set_grid(self, *args, **kwargs):     
        self.axes.grid(*args, **kwargs)
                  
    """------------------------------------------------------------------------------------------------
    """ 
    def get_legend(self):
        return self.axes.get_legend()
        
    def legend(self):
        return self.get_legend()

    def set_legend(self, *args, **kwargs):
        """
        *loc*
            'best'         : 0,
            'upper right'  : 1,
            'upper left'   : 2,
            'lower left'   : 3,
            'lower right'  : 4,
            'right'        : 5,
            'center left'  : 6,
            'center right' : 7,
            'lower center' : 8,
            'upper center' : 9,
            'center'       : 10
        """
        self.axes.legend(*args, **kwargs)

    """------------------------------------------------------------------------------------------------
    """  
    def text(self, *args, **kwargs):
        transform = kwargs.pop('transform', self.axes.transAxes)
        return self.axes.text(*args, transform=transform, **kwargs)

    def annotate(self, *args, **kwargs):
        return self.axes.annotate(*args, **kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def clear(self):
        self.figure.clear(chart=self)

    def clear_data(self):
        self.figure.clear_data(chart=self)
