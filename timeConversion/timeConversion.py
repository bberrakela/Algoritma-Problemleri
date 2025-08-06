#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    am_pm=s[-2:]
    time_part=s[:-2]
    
    h, m, sec = time_part.split(':')
    h=int(h)
    
    if am_pm == "PM" and h!=12:
        h+=12
    elif am_pm=="AM" and h==12:
        h=0
        
    h_str = str(h).zfill(2)
    
    return f"{h_str}:{m}:{sec}"
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
