#!/bin/python3
#https://www.hackerrank.com/challenges/pairs

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs_poly(k, arr):
    c = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] - arr[j] == k:
                c += 1

    return c

def binary_search(el, arr):
    l = 0
    r = len(arr)

    while l <= r:
        idx = int((l + r) / 2)
        if idx >= len(arr):
            return -1
        elif el == arr[idx]:
            return idx
        elif el < arr[idx]:
            r = idx - 1
        else:
            l = idx + 1

    return -1

def pairs(k, arr):
    c = 0
    sarr = sorted(arr)

    for x in sarr:
        diff = k + x
        y = binary_search(diff, sarr)

        if y != -1:
            c += 1

    return c

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
