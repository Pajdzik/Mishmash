#!/bin/python3
#https://www.hackerrank.com/challenges/sherlock-and-valid-string

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    odd = 0
    cc = d[s[0]]
    for c in d.values():
        if cc != c:
            odd += 1

        if odd >= 2:
            return "NO"

    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
