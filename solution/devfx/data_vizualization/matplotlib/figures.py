import matplotlib as mpl
import matplotlib.pyplot

class Figures(object):
    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def ion(cls):
        mpl.pyplot.ion()

    @classmethod
    def ioff(cls):
        mpl.pyplot.ioff()

    @classmethod
    def istatus(cls):
        return mpl.pyplot.isinteractive()

    @classmethod
    def layout(cls, padding=1.0, rect=None, h_subplot_padding=None, w_subplot_padding=None):
        for i in mpl.pyplot.get_fignums():
            mpl.pyplot.figure(i).tight_layout(pad=padding, h_pad=h_subplot_padding, w_pad=w_subplot_padding, rect=rect)

    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def show(cls, figure=None, padding=1.0, rect=None, h_subplot_padding=None, w_subplot_padding=None, block=True):
        if(figure is not None):
            figure.tight_layout(pad=padding, h_pad=h_subplot_padding, w_pad=w_subplot_padding, rect=rect)

            if(block == True):
                mpl.pyplot.figure(figure.number)
                mpl.pyplot.show()
            else:
                mpl.pyplot.pause(0.001)
                mpl.pyplot.draw()
        else:
            for i in mpl.pyplot.get_fignums():
                mpl.pyplot.figure(i).tight_layout(pad=padding, h_pad=h_subplot_padding, w_pad=w_subplot_padding, rect=rect)

            if (block == True):
                mpl.pyplot.show()
            else:
                mpl.pyplot.pause(0.001)
                mpl.pyplot.draw()

    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def close(cls, figure=None):
        if (figure is not None):
            mpl.pyplot.close(figure)
        else:
            mpl.pyplot.close()



