#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1,n+1):
        bosluk_sayisi=n-i
        hash_sayisi=i
        bosluklar=" " * bosluk_sayisi
        hashlar="#" * hash_sayisi
        print (bosluklar+hashlar)
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
