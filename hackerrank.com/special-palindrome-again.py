#!/bin/python3
#https://www.hackerrank.com/challenges/special-palindrome-again

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(length, s):
    sub_strings = []

    c_current = s[0]
    c_count = 1
    for i in range(1, length):
        c = s[i]
        if c != c_current:
            sub_strings.append((c_current, c_count))
            c_current = c
            c_count = 1
        else:
            c_count += 1
    
    # last element of the list
    sub_strings.append((c_current, c_count))

    count = 0

    for sub in sub_strings:
        # n + (n - 1) + (n - 2) + ... + 1
        count += (sub[1] * (sub[1] + 1)) // 2

    for i in range(1, len(sub_strings) - 1):
        middle = sub_strings[i]

        if middle[1] != 1:
            continue

        left = sub_strings[i - 1]
        right = sub_strings[i + 1]

        if left[0] == right[0]:
            count += min(left[1], right[1])

    return count
    

if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)
