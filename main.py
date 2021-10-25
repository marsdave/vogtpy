# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:03:37 2021

A number of Python functions that are useful for all kinds of coding situations. Will be extended over time. Should be put into a better format than it currently is in.

@author: David Vogt
"""

import numpy as np
from scipy import sparse

def baseline_als(y, lam, p, niter=10):
  L = len(y)
  D = sparse.csc_matrix(np.diff(np.eye(L), 2))
  w = np.ones(L)
  for i in range(niter):
    W = sparse.spdiags(w, 0, L, L)
    Z = W + lam * D.dot(D.transpose())
    z = sparse.linalg.spsolve(Z, w*y)
    w = p * (y > z) + (1-p) * (y < z)
  return z

def round_to_significant(x, significant_digits=1):
    if hasattr(x, "__len__"):
        output = np.copy(x)
        for i in range(len(x)):
            number = x[i]
            decimals = -int(np.floor(np.log10(np.abs(number)))) + (significant_digits - 1)
            output[i] = round(number, decimals)
    else:
        number = x
        decimals = -int(np.floor(np.log10(np.abs(number)))) + (significant_digits - 1)
        output = round(number, decimals)
    
    return output

