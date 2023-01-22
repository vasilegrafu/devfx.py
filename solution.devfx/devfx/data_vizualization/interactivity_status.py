import matplotlib
import matplotlib.pyplot
    
"""------------------------------------------------------------------------------------------------
"""
def ion(cls):
    matplotlib.pyplot.ion()

def ioff(cls):
    matplotlib.pyplot.ioff()

def isinteractive(cls):
    return matplotlib.pyplot.isinteractive()