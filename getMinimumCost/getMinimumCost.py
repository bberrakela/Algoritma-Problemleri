#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    
    total_cost = 0
    
    purchased_flowers = [0] * k
    
    for i in range(len(c)):
        price = c[i]
        
        friend_index = i % k
        
        new_price = (purchased_flowers[friend_index] + 1) * price
        
        total_cost += new_price
        
        purchased_flowers[friend_index] += 1
        
    return total_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
