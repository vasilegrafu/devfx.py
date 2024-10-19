import matplotlib as mpl
import mplfinance as mplf
import matplotlib.dates
import numpy as np
import pandas as pd
import datetime as dt
import devfx.core as core
import devfx.exceptions as exp
from .figure import Figure as Figure
from .chart import Chart
from .chart_factory import ChartFactory

class Chart2d(Chart):
    def __init__(self, 
                 figure=None, fig_size=None,
                 position=None,
                 title=None,
                 grid=None, 
                 xlim=None, xmin=None, xmax=None, ylim=None, ymin=None, ymax=None,
                 xlabel=None, ylabel=None):
        if(figure is None):
            if(fig_size is None):
                figure = Figure()
            else:
                figure = Figure(size=fig_size)
          
        if(position is None):
            axes = ChartFactory.new_chart2d(figure=figure)
        else:
            axes = ChartFactory.new_chart2d(figure=figure, position=position)

        super().__init__(figure, axes, title, grid)

        if ((xmin is not None) or (xmax is not None)):
            xlim = [xmin, xmax]
        self.set_xlim(xlim)

        if ((ymin is not None) or (ymax is not None)):
            ylim = [ymin, ymax]
        self.set_ylim(ylim)

        if(xlabel is not None):
            self.set_xlabel(xlabel)
            
        if(ylabel is not None):
            self.set_ylabel(ylabel)

    """------------------------------------------------------------------------------------------------
    """      
    def get_xlim(self):
        return self.__xlim

    def xlim(self):
        return self.get_xlim()

    def set_xlim(self, xlim):
        self.__xlim = xlim

    """------------------------------------------------------------------------------------------------
    """ 
    def get_ylim(self):
        return self.__ylim

    def ylim(self):
        return self.get_ylim()

    def set_ylim(self, ylim):
        self.__ylim = ylim
              
    """------------------------------------------------------------------------------------------------
    """ 
    def get_xlabel(self):
        return self.axes.get_xlabel()
            
    def xlabel(self):
        return self.get_xlabel()
        
    def set_xlabel(self, *args, **kwargs):
        self.axes.set_xlabel(*args, **kwargs)
            
    """------------------------------------------------------------------------------------------------
    """  
    def get_ylabel(self):
        return self.axes.get_ylabel()
                   
    def ylabel(self):
        return self.get_ylabel()
        
    def set_ylabel(self, *args, **kwargs):
        self.axes.set_ylabel(*args, **kwargs)

    """------------------------------------------------------------------------------------------------
    """

    def xline(self, y=0, xmin=0, xmax=1, **kwargs):
        return self.axes.axhline(y=y, xmin=xmin, xmax=xmax, **kwargs)

    def yline(self, x=0, ymin=0, ymax=1, **kwargs):
        return self.axes.axvline(x=x, ymin=ymin, ymax=ymax, **kwargs)
               
    """------------------------------------------------------------------------------------------------
    """
    def _do_prior_draw(self):
        pass

    def _do_post_draw(self):
        if(self.xlim() is not None):
            self.axes.set_xlim(self.get_xlim())
        if(self.ylim() is not None):
            self.axes.set_ylim(self.get_ylim())

        for _ in self.axes.get_xticklabels():
            _.set_rotation(0)
            _.set_fontsize('medium')
        for _ in self.axes.get_yticklabels():
            _.set_rotation(0)
            _.set_fontsize('medium')

    def plot(self, *args, **kwargs):
        self._do_prior_draw()
        if (core.is_iterable(args[0]) and (len(args) >= 2 and core.is_iterable(args[1]))):
            a = np.asarray([args[0], args[1]])
            a = a.T
            a = a[np.argsort(a[:, 0])]
            a = a.T
            result = self.axes.plot(a[0], a[1], *args[2:], **kwargs)
        elif (core.is_iterable(args[0])):
            result = self.axes.plot(args[0], *args[1:], **kwargs)
        else:
            raise exp.NotSupportedError()
        self._do_post_draw()
        return result

    def fill(self, *args, **kwargs):
        self._do_prior_draw()
        result = self.axes.fill(*args, **kwargs)
        self._do_post_draw()
        return result

    def fill_between(self, *args, **kwargs):
        self._do_prior_draw()
        result = self.axes.fill_between(*args, **kwargs)
        self._do_post_draw()
        return result

    def bar(self, *args, **kwargs):
        self._do_prior_draw()
        result = self.axes.bar(*args, **kwargs)
        self._do_post_draw()
        return result
    
    def barh(self, *args, **kwargs):
        self._do_prior_draw()
        result = self.axes.barh(*args, **kwargs)
        self._do_post_draw()
        return result
        
    def hist(self, *args, **kwargs):
        self._do_prior_draw()
        result = self.axes.hist(*args, **kwargs)
        self._do_post_draw()
        return result
            
    def hist2d(self, *args, **kwargs):
        self._do_prior_draw()
        result = self.axes.hist2d(*args, **kwargs)
        self._do_post_draw()
        return result

    def pie(self, *args, **kwargs):
        self._do_prior_draw()
        result = self.axes.pie(*args, **kwargs)
        self._do_post_draw()
        return result

    def scatter(self, *args, **kwargs):
        self._do_prior_draw()
        if(core.is_iterable(args[0]) and (len(args) >= 2 and core.is_iterable(args[1]))):
            result = self.axes.scatter(args[0], args[1], *args[2:], marker = kwargs.pop('marker', '.'), **kwargs)
        elif(core.is_iterable(args[0])):
            result = self.axes.scatter(range(1, len(args[0]) + 1), args[0], *args[1:], marker = kwargs.pop('marker', '.'), **kwargs)
        else:
            raise exp.NotSupportedError()
        self._do_post_draw()
        return result

    def contour(self, *args, **kwargs):
        self._do_prior_draw()
        result = self.axes.contour(*args, **kwargs)
        self._do_post_draw()
        return result

    def image(self, *args, **kwargs):
        self._do_prior_draw()
        result = self.axes.imshow(*args, **kwargs)
        self._do_post_draw()
        return result

    """------------------------------------------------------------------------------------------------
    """
    class __timeseries(object):
        def __init__(self, chart):
            self.__chart = chart

        """----------------------------------------------------------------
        """
        def __set_axes_labels(self, datetimes, datetime_format, eliminate_gaps):
            datetimes = np.asarray(datetimes, dtype='datetime64[us]')
            if (eliminate_gaps is False):
                self.__chart.axes.set_xticklabels([mpl.dates.num2date(xtick).strftime(datetime_format) for xtick in self.__chart.axes.get_xticks()])
            else:
                nxticks = 5
                if(nxticks >= len(datetimes)):
                    nxticks = len(datetimes)
                self.__chart.axes.set_xticks([int(round(i)) for i in np.linspace(0, len(datetimes)-1, nxticks)])
                self.__chart.axes.set_xticklabels([datetimes[xtick].astype(dt.datetime).strftime(datetime_format) for xtick in self.__chart.axes.get_xticks()])

        """----------------------------------------------------------------
        """
        def candlesticks(self, data, 
                               eliminate_gaps=True, 
                               datetime_format='%Y-%m-%d\n%H:%M:%S',
                               color_up='green',
                               color_down='red',
                               *args, **kwargs):  
            if(core.is_typeof(data, pd.DataFrame)):
                datetimes = data.index.values
            else:
                raise exp.ArgumentError()

            self.__chart._do_prior_draw()
           
            mplf.plot(data=data, 
                      show_nontrading=not eliminate_gaps, 
                      ax=self.__chart.axes, 
                      type='candle',
                      datetime_format=datetime_format,
                      style=mplf.make_mpf_style(marketcolors=mplf.make_marketcolors(up=color_up, down=color_down)),
                      *args, **kwargs)

            datetimes = np.asarray(data.index.values, dtype='datetime64[us]')
            self.__set_axes_labels(datetimes, datetime_format, eliminate_gaps)

            self.__chart._do_post_draw()

        """----------------------------------------------------------------
        """
        def ohlc(self, data, 
                       eliminate_gaps=True, 
                       datetime_format='%Y-%m-%d\n%H:%M:%S',
                       *args, **kwargs):     
            if(core.is_typeof(data, pd.DataFrame)):
                datetimes = data.index.values
            else:
                raise exp.ArgumentError()

            self.__chart._do_prior_draw()
           
            mplf.plot(data=data, 
                      show_nontrading=not eliminate_gaps, 
                      ax=self.__chart.axes, 
                      type='ohlc',
                      datetime_format=datetime_format,
                      *args, **kwargs)

            self.__set_axes_labels(datetimes, datetime_format, eliminate_gaps)

            self.__chart._do_post_draw()

        """----------------------------------------------------------------
        """
        def plot(self, data, 
                       eliminate_gaps=True, 
                       datetime_format='%Y-%m-%d\n%H:%M:%S',
                       *args, **kwargs): 
            if(core.is_typeof(data, pd.DataFrame)):
                (datetimes, values) = (data.index.values, data.iloc[:, 0].values)
            elif(core.is_typeof(data, pd.Series)):
                (datetimes, values) = (data.index.values, data.values)
            else:
                raise exp.ArgumentError()

            if(len(datetimes) is None):
                raise exp.ArgumentError()
            if(len(datetimes) <= 1):
                raise exp.ArgumentError()

            self.__chart._do_prior_draw()

            datetimes = np.asarray(datetimes, dtype='datetime64[us]')
            if (datetimes[0] > datetimes[1]):
                datetimes = datetimes[::-1]
                values = values[::-1]
            values = np.asarray(values)

            if(eliminate_gaps is False):
                self.__chart.plot(datetimes, values, *args, **kwargs)
            else:
                self.__chart.plot([i for i, _ in enumerate(values)], values, *args, **kwargs)

            self.__set_axes_labels(datetimes, datetime_format, eliminate_gaps)

            self.__chart._do_post_draw()

        """----------------------------------------------------------------
        """
        def bar(self, data, 
                      eliminate_gaps=True, 
                      datetime_format='%Y-%m-%d\n%H:%M:%S',
                      *args, **kwargs): 
            if(core.is_typeof(data, pd.DataFrame)):
                (datetimes, values) = (data.index.values, data.iloc[:, 0].values)
            elif(core.is_typeof(data, pd.Series)):
                (datetimes, values) = (data.index.values, data.values)
            else:
                raise exp.ArgumentError()

            if(len(datetimes) is None):
                raise exp.ArgumentError()
            if(len(datetimes) <= 1):
                raise exp.ArgumentError()

            self.__chart._do_prior_draw()

            datetimes = np.asarray(datetimes, dtype='datetime64[us]')
            if (datetimes[0] > datetimes[1]):
                datetimes = datetimes[::-1]
                values = values[::-1]
            values = np.asarray(values)

            if(eliminate_gaps is False):
                self.__chart.bar(datetimes, values, width=(1.0/1.25)*(min(np.diff(datetimes))/np.timedelta64(1, 'D')), *args, **kwargs)
            else:
                self.__chart.bar([i for i, _ in enumerate(values)], values, width=1.0/1.25, *args, **kwargs)

            self.__set_axes_labels(datetimes, datetime_format, eliminate_gaps)

            self.__chart._do_post_draw()

    @property
    def timeseries(self):
        return Chart2d.__timeseries(self)

