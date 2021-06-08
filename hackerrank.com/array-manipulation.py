#!/bin/python3
# https://www.hackerrank.com/challenges/crush/problem

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    arr = [0 for _ in range(n)]

    for query in queries:
        left = query[0] - 1
        right = query[1] - 1
        value = query[2]

        for i in range(left, right + 1):
            arr[i] += value

    max = arr[0]
    for i in arr:
        if i > max:
            max = i

    return max
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')

    # fptr.close()
