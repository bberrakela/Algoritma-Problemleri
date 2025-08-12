#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s_lower = s.lower()
    unique_letters = set()
    
    for char in s_lower:
        if 'a' <= char <= 'z':
            unique_letters.add(char)
            
    if len(unique_letters) == 26:
        return "pangram"
    else:
        return "not pangram"
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
