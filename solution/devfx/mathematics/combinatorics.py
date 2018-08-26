import numpy as np
import scipy as sp
import scipy.special

"""----------------------------------------------------------
"""
def nF(n):
    return sp.special.factorial(n)

"""----------------------------------------------------------
"""
def nP(n):
    return sp.special.perm(n, n)

def nPn(n):
    return sp.special.perm(n, n)

def nPr(n, r):
    return sp.special.perm(n, r)

"""----------------------------------------------------------
"""
def nCr(n, r):
    return sp.special.comb(n, r)

