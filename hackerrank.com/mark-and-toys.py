#!/bin/python3
#https://www.hackerrank.com/challenges/mark-and-toys

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sortedPrices = sorted(prices)
    count = 0

    for price in sortedPrices:
        if (k - price) > 0:
            count += 1
            k -= price

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
