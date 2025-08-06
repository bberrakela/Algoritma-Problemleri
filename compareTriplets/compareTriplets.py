#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice_puan=0
    bob_puan=0
   
    for i in range(3):
        if a[i]>b[i]:
           alice_puan += 1
        elif b[i]>a[i]:
           bob_puan+=1
        
    return [ alice_puan, bob_puan ]
   
