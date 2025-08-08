#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    results = []
    
    while len(arr) > 0:
        results.append(len(arr))
        
        min_length = min(arr)
        
        new_arr = []
        for stick in arr:
            new_length = stick - min_length
            if new_length > 0:
                new_arr.append(new_length)
                
        arr = new_arr
            
    return results
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
