#!/bin/python3
#https://www.hackerrank.com/challenges/sherlock-and-anagrams

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    duplicates = { }
    for c in s:
        duplicates[c] = 1 if c not in duplicates else duplicates[c] + 1

    dup_chars = [c for c in duplicates.keys() if duplicates[c] > 1]

    if (any(dup_chars)):
        return 0

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
