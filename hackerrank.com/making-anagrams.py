#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-making-anagrams

import math
import os
import random
import re
import sys

def countCharacters(word):
    d = {}
    for c in word:
        d[c] = 1 if c not in d else d[c] + 1

    return d

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    aa = countCharacters(a)
    bb = countCharacters(b)

    count = 0
    for c in aa:
        if c in bb:
            count += abs(aa[c] - bb[c])
        else:
            count += aa[c]

    for c in bb:
        if c not in aa:
            count += bb[c]

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
