#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n=len(arr)
    pozitifSayi=0
    negatifSayi=0
    notrSayi=0
    
    
    for sayi in arr:
        if  sayi>0:
              pozitifSayi+=1
        elif sayi<0:
              negatifSayi+=1
        else:
              notrSayi+=1
               
    pozitifOrani= pozitifSayi/n
    negatifOrani= negatifSayi/n
    notrOrani=notrSayi/n            

    print(f"{pozitifOrani:.6f}")
    print(f"{negatifOrani:.6f}")
    print(f"{notrOrani:.6f}")





if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
