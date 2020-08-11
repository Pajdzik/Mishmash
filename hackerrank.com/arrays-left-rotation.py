#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-array-left-rotation

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    arr = a.copy()
    for i in range(0, len(a)):
        arr[(i - d) % len(a)] = a[i]

    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
