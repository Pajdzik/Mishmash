#!/bin/python3
#https://www.hackerrank.com/challenges/angry-children

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    sarr = sorted(arr)
    min = sarr[k - 1] - sarr[0]

    for i in range(len(sarr) - k + 1):
        m = sarr[i + k - 1] - sarr[i]
        if m < min:
            min = m

    return min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
