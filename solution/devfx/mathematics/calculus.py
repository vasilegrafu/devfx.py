import numpy as np
import scipy as sp
import scipy.misc
import scipy.integrate
import scipy.interpolate
from .constants import epsilon
from .functions import is_odd

"""----------------------------------------------------------
"""
def D1d(fn, x0, args=()):
    return Dnd(fn, x0, args=args, n=1)
    
def D2d(fn, x0, args=()):
    return Dnd(fn, x0, args=args, n=2)

def D3d(fn, x0, args=()):
    return Dnd(fn, x0, args=args, n=3)
    
def Dnd(fn, x0, args=(), n=1, dx=epsilon):
    return sp.misc.derivative(fn, x0, dx=dx, n=n, args=args, order=n if is_odd(n) else (n+1))

"""----------------------------------------------------------
"""
def S1d(fn, a, b, args=()):
    (y, *others) = sp.integrate.quad(fn, a, b, args=args)
    return y

def S2d(fn, a, b, gfn, hfn, args=()):
    fn = lambda y, x: fn(x, y)
    (y, *others) = sp.integrate.dblquad(fn, a, b, gfn, hfn, args=args)
    return y

def S3d(func, a, b, gfn, hfn, qfn, rfn, args=()):
    func = lambda z, y, x: func(x, y, z)
    qfn = lambda y, x: qfn(x, y)
    rfn = lambda y, x: rfn(x, y)
    (y, *others) = sp.integrate.tplquad(func, a, b, gfn, hfn, qfn, rfn, args=args)
    return y

"""----------------------------------------------------------
"""
def interp1d(x, y, kind=None):
    if (kind is None):
        return sp.interpolate.interp1d(x, y)
    else:
        return sp.interpolate.interp1d(x, y, kind=kind)

def interp2d(x, y, z, kind=None):
    if (kind is None):
        return sp.interpolate.interp2d(x, y, z)
    else:
        return sp.interpolate.interp2d(x, y, z, kind=kind)