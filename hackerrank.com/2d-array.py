#!/bin/python3
#https://www.hackerrank.com/challenges/2d-array/

import math
import os
import random
import re
import sys

def getSum(ii, jj, arr):
    sum = 0

    for i in range(ii, ii + 3):
        for j in range(jj, jj + 3):
                sum += arr[i][j]

    sum -= (arr[ii + 1][jj] + arr[ii + 1][jj + 2])

    return sum

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = -9 * 9
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr[i]) - 2):
            sum = getSum(i, j, arr)
            if sum > maxSum:
                maxSum = sum
    
    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
