#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-recursive-staircase

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    s1, s2, s3 = 1, 2, 4

    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    result = 0

    for i in range(4, n + 1):
        result = s1 + s2 + s3
        s1 = s2
        s2 = s3
        s3 = result

    return result

if __name__ == '__main__':
    s = int(input())

    for s_itr in range(s):
        n = int(input())
        res = stepPerms(n)
        print(str(res) + '\n')
