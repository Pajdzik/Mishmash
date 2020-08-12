#!/bin/python3
#https://www.hackerrank.com/challenges/two-strings

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d1 = set(s1)
    d2 = set(s2)

    if any(d1.intersection(d2)):
        return "YES"
    else:
        return "NO"

def twoStrings_slow(s1, s2):
    for c1 in s1:
        for c2 in s2:
            if c1 == c2:
                return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        fptr.write(result + '\n')

    fptr.close()
