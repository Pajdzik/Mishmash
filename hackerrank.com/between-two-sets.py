#!/bin/python3
#https://www.hackerrank.com/challenges/between-two-sets/problem

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    if (len(a) == 0 or len(b) == 0):
        return 0

    total = 0
    amin = min(a)
    bmax = max(b)

    for i in range(amin, bmax + 1):
        aa = all([(i % aa) == 0 for aa in a])
        bb = aa and all([bb % i == 0 for bb in b])

        if bb:
            total += 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
