#!/bin/python3
#https://www.hackerrank.com/challenges/luck-balance

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    not_important = []
    important = []

    for c in contests:
        if c[1] == 0:
            not_important.append(c[0])
        else:
            important.append(c[0])

    important = sorted(important, reverse=True)

    balance = sum(not_important) + sum(important[:k]) - sum(important[k:])
    
    return balance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()