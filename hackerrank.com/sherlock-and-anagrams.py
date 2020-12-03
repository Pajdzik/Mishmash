#!/bin/python3
#https://www.hackerrank.com/challenges/sherlock-and-anagrams

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0

    for i in range(len(s)):
        for j in range(len(s) - 1, i, -1):
            if s[i] == s[j]:
                count += countAnagrams(s, i, j)

    return count

def countAnagrams(s, i, j):
    c = 0
    si = set()
    sj = set()

    while i < j and si == sj:
        si.add(i)
        sj.add(j)
        i += 1
        j -= 1

        if si != sj:
            c += 1

        print(str([s[x] for x in si]) + " | " + str([s[x] for x in sj]))

    return c

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(str(result) + '\n')