import numpy as np
import scipy as sp
import scipy.stats
import devfx.exceptions as exceps
from .constants import e

""" constants  
"""
def isinf(x):
    return np.isinf(x)
    
def isneginf(x):
    return np.isneginf(x)
    
def isposinf(x):
    return np.isposinf(x)
    
def isnan(x):
    return np.isnan(x)

""" constant  
"""
def const(x, c):
    return c
    
    
""" linear  
"""
def lin(x, a, b):
    return a*x+b
 

""" quadratic  
"""
def qdr(x, a, b, c):
    return a*x*x+b*x+c

   
""" square 
"""
def sqr(x):
    return x**2


""" cubic
"""
def cb(x):
    return x**3


""" exponential
"""
def exp(a, x):
    return np.power(a, x)

def exp2(x):
    return np.power(2, x)
    
def exp10(x):
    return np.power(10, x)

def expe(x):
    return np.power(e, x)

""" power
"""
def pow(x, a):
    return np.power(x, a)
    
def pow2(x):
    return np.power(x, 2)
    
def pow10(x):
    return np.power(x, 10)

def powe(x):
    return np.power(x, e)

def sqrrt(x):
    return np.sqrt(x)
    
def cbrt(x):
    return np.power(x, 1.0/3.0)


""" logarithmic
"""
def log(x, b):
    return np.log(x)/np.log(b)
    
def log2(x):
    return np.log2(x)
    
def log10(x):
    return np.log10(x)

def loge(x):
    return np.log(x)


""" trigonometric
"""
def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)


""" ranges
"""       
def range(start, stop, step=None):
    if(step is None):
        return np.arange(start=start, stop=stop)
    else:
        return np.arange(start=start, stop=stop, step=step)

def linspace(start, stop, count=64, endpoint=True):
    return np.linspace(start=start, stop=stop, num=count, endpoint=endpoint)

def logspace(start, stop, count=64, endpoint=True, base=10):
    return np.logspace(start=start, stop=stop, num=count, endpoint=endpoint, base=base)
    

""" aggregates  
"""
def min(a, axis=None):
    a = np.asarray(a)
    return np.amin(a=a, axis=axis)
    
def max(a, axis=None):
    a = np.asarray(a)
    return np.amax(a=a, axis=axis)

def sum(a, axis=None):
    a = np.asarray(a)
    return np.sum(a=a, axis=axis)
    
def csum(a, axis=None):
    a = np.asarray(a)
    return np.cumsum(a=a, axis=axis)
    
def prod(a, axis=None):
    a = np.asarray(a)
    return np.prod(a=a, axis=axis)
    
def cprod(a, axis=None):
    a = np.asarray(a)
    return np.cumprod(a=a, axis=axis)
    
def diff(a, n=1, axis=None):
    a = np.asarray(a)
    if(axis is None):
        a = a.flatten()
        return np.diff(a=a, n=n, axis=-1)
    else:
        return np.diff(a=a, n=n, axis=axis)
    
    
""" miscellaneous  
"""   
def sgn(x):
    return iverson(x>0)-iverson(x<0)
          
def floor(x, decimals=None):
    if(decimals is None):
        return np.floor(x)
    else:
        d = 10**decimals
        return np.floor(x*d)/d

def ceil(x, decimals=None):
    if(decimals is None):
        return np.ceil(x)
    else:
        d = 10**decimals
        return np.ceil(x*d)/d

def round(x, decimals=None):
    if(decimals is None):
        return np.round(x)
    else:
        return np.round(x, decimals)

def abs(x):
    return np.absolute(x)
    
    
def is_even(x):
    return x%2==0
    
def is_odd(x):
    return x%2==1
      
def next_even(n):
    if(is_even(n)):
        return n+2
    elif(is_odd(n)):
        return n+1
    else:
        raise exceps.ArgumentError()

def next_odd(n):
    if(is_odd(n)):
        return n+2
    elif(is_even(n)):
        return n+1
    else:
        raise exceps.ArgumentError()
        
""" special  
"""
def iverson(predicate):
    return 1 if(predicate) else 0

def macaulay(x):
    return x if(x >= 0) else 0
    
def kronecker(i, j):
    return 1 if(i == j) else 0


def gamma(x):
    return sp.stats.gamma(x)

def beta(x):
    return sp.stats.beta(x)


def logistic(x):
    x = np.asarray(x)
    return expe(x)/(1.0 + expe(x))

def softmax(x):
    x = np.asarray(x)
    return expe(x)/sum(expe(x))


def odds(p):
    p = np.asarray(p)
    return p/(1.0-p)

def logit(p):
    p = np.asarray(p)
    return loge(p/(1.0-p))
  
