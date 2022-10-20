#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getOneBits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def getOneBits(n):
    # Write your code here
    bit_repr = []
    quotient = n
    while quotient > 0:
        remainder = quotient & 1
        quotient = quotient >> 1
        bit_repr.append(remainder)
    bit_repr.reverse()
    
    to_return = []
    to_return.append(bit_repr.count(1))
    for i, v in enumerate(bit_repr):
        if v == 1:
            to_return.append(i + 1)
    return to_return

if __name__ == '__main__':
    """ fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = getOneBits(n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close() """
    print(getOneBits(10)) # 1010

