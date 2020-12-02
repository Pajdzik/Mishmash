#!/bin/python3
#https://www.hackerrank.com/challenges/largest-rectangle

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    for b in h:
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
