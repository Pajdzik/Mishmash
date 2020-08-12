#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-bubble-sort

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for i in range(0, len(a)):
        for j in range(0, len(a) - 1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
