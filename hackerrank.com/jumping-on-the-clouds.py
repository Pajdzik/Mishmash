#!/bin/python3
# https://www.hackerrank.com/challenges/jumping-on-the-clouds

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.

def jumpingOnClouds(c):
    length = len(c) - 1
    moves = 0
    i = 0

    while i < length:
        if i + 2 >= length:
            return moves + 1
        if c[i + 2] == 0:
            i = i + 2
        else:
            i = i + 1

        moves = moves + 1

    return moves


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
