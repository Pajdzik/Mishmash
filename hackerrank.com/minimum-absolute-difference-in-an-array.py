#!/bin/python3
#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference_abs(arr):
    mindiff = abs(arr[0] - arr[1])

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff < mindiff:
                mindiff = diff

    return mindiff

def minimumAbsoluteDifference_square(arr):
    mindiff = abs(arr[0] - arr[1])
    minsqaure = mindiff * mindiff

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            square = (arr[i] - arr[j]) * (arr[i] - arr[j])
            if square < minsqaure:
                minsqaure = square

    return int(math.sqrt(minsqaure)) 

def minimumAbsoluteDifference(arr):
    sarr = sorted(arr)
    mindiff = abs(sarr[0] - sarr[1])

    for i in range(len(sarr) - 1):
        diff = abs(sarr[i] - sarr[i + 1])
        if diff < mindiff:
            mindiff = diff

    return mindiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
