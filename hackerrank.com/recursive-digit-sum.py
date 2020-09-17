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

    sum_of_digits = 0
    while n > 0:
        sum_of_digits += (n % 10)
        n = n // 10

    return digits_sum(sum_of_digits)

def superDigit(n, k):
    # proof: http://applet-magic.com/digitsummod9.htm
    res = ((n % 9) * (k % 9)) % 9
    return res or 9

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    result = superDigit(n, k)
    print(str(result) + '\n')
