#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    counts = [0] * 6
    
    for bird_id in arr:
        counts[bird_id] += 1
    
    max_count = 0
    result_bird_id = 0
    
    for i in range(1, 6):
        if counts[i] > max_count:
            max_count = counts[i]
            result_bird_id = i
    
    return result_bird_id
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
