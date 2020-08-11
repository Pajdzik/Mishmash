#!/bin/python3
#https://www.hackerrank.com/challenges/repeated-string

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    acount = 0
    for c in s:
        if c == 'a':
            acount += 1
    
    l = len(s)

    acount = acount * int(n / l)

    ll = int(n % l)

    if ll > 0:
        ss = s[:ll]
        for c in ss:
            if c == 'a':
                acount += 1

    return acount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()
