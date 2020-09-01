#!/bin/python3
#https://www.hackerrank.com/challenges/minimum-swaps-2

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != i + 1:
            for j in range(i + 1, len(arr)):
                if (arr[j] == i + 1):
                    arr[i], arr[j] = arr[j], arr[i]
                    count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
