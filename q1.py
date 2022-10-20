#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaximumMEX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMaximumMEX(arr):
    # Write your code here
    mexes = []
    for i, v in enumerate(arr):
        mexes.append(min(i, v))
    mex = 1
    while mex in mexes:
        mex += 1
    return mex

if __name__ == '__main__':
    print(getMaximumMEX([3, 2, 3]))
    print(getMaximumMEX([1, 2, 2]))
    print(getMaximumMEX([0, 0]))
    print(getMaximumMEX([2, 0, 0]))
