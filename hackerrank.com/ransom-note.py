#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-ransom-note

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d = {}
    for word in magazine:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

    for word in note:
        if word not in d:
            print("No")
            return
        else:
            if d[word] == 0:
                print("No")
                return
            d[word] -= 1

    print("Yes")

if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
