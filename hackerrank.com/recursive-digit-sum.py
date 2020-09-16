#!/bin/python3
#https://www.hackerrank.com/challenges/recursive-digit-sum

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def digits_sum(n):
    if n // 10 == 0:
        return n

    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10

    return digits_sum(sum(digits))

def superDigit(n, k):
    number = int(str(n) * k)
    return digits_sum(number)

if __name__ == '__main__':
    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    print(str(result) + '\n')
