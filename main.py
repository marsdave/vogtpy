# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:03:37 2021

A number of Python functions that are useful for all kinds of coding situations. Will be extended over time. Should be put into a better format than it currently is in.

@author: David Vogt
"""

import numpy as np

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

