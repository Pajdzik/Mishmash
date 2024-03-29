#!/bin/python3
#https://www.hackerrank.com/challenges/flipping-bits

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    max_value = 2**32 - 1
    return max_value - n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
