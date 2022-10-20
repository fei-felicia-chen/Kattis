#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinimumBlows' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY height as parameter.
#

def getMinimumBlows(height):
    # Write your code here
    b_left = height.copy()
    left_blows = []
    while b_left:
        last = b_left.pop(0)
        blow = [last]
        while b_left:
            if (cur := b_left[0]) > last:
                blow.append(cur)
                b_left.pop(0)
                last = cur
            else:
                break
        left_blows.append(blow)
        
    b_right = height.copy()
    right_blows = []
    while b_right:
        last = b_right.pop()
        blow = [last]
        while b_right:
            if (cur := b_right[-1]) > last:
                blow.append(cur)
                b_right.pop()
                last = cur
            else:
                break
        right_blows.append(blow)
    
    #print(left_blows)
    #print(right_blows)
    num_blows = 0
    while height:
        #print(height)
        if left_blows:
            if right_blows:
                l = len(left_blows[0])
                r = len(right_blows[0])
                num_blows += 1
                if l > r:
                    tmp = left_blows[0]
                    left_blows.pop(0)
                    for _ in tmp:
                        height.pop(0)
                        if right_blows[-1] == []:
                            right_blows.pop()
                        right_blows[-1].pop(0)
                else:
                    tmp = right_blows[0]
                    right_blows.pop(0)
                    for _ in tmp:
                        height.pop()
                        if left_blows[0] == []:
                            left_blows.pop(0)
                        left_blows[0].pop(0)
            else:
                num_blows += len(left_blows)
                break
        else:
            num_blows += len(right_blows)
            break
    return num_blows
        
    
        
if __name__ == '__main__':
    print(getMinimumBlows([1, 2, 3, 4, 3, 2, 3, 2, 1]))
