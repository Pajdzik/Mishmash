#!/bin/python3
#https://www.hackerrank.com/challenges/new-year-chaos

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes_square(q):
    swaps = { i : 0 for i in q }
    total = 0
    
    for i in range(0, len(q)):
        for j in range(i + 1, len(q)):
            if (q[i] > q[j]):
                total += 1
                swaps[q[i]] += 1
                if (swaps[q[i]] > 2):
                    return "Too chaotic"
                
                q[i], q[j] = q[j], q[i]

    return total

def minimumBribes(arr):
    idx = [  for i in arr ]
    i = 0

    return i + idx


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        print(minimumBribes(q))
