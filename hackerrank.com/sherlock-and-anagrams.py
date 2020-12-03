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

    for start in range(len(s) - 1):
        for length in range(1, len(s) - start + 1):
            word = sorted(s[start:start + length])

            for c in range(start + 1, len(s) - length + 1):
                palindrome = sorted(s[c:c + length])

                if word == palindrome:
                    count += 1

    return count

if __name__ == '__main__':
    q = 1#int(input())

    for q_itr in range(q):
        s = 'kkkk'#input()

        result = sherlockAndAnagrams(s)
        print(str(result) + '\n')