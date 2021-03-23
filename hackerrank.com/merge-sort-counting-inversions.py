#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-merge-sort/problem

import math
import os
import random
import re
import sys

def merge_sort(arr):
    pass

# Complete the countInversions function below.
def countInversions(arr):
    merge_sort(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
