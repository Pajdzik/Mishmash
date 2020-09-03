#!/bin/python3
#https://www.hackerrank.com/challenges/frequency-queries

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    ans = list()
    stack = dict()

    for query in queries:
        command = query[0]
        argument = query[1]
        
        if command == 1:
            if argument in stack:
                stack[argument] += 1
            else:
                stack[argument] = 1

        elif command == 2:
            if argument not in stack:
                continue

            stack[argument] -= 1
            if stack[argument] == 0:
                del stack[argument]

        else:
            if argument > 10**6:
                ans.append(0)
            else:
                ans.append(1 if argument in stack.values() else 0)

    return ans

if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input", "frequency-queries.08.txt"), "r") as f:
        inp = f.readlines()

        q = int(inp[0].strip())

        queries = []

        for i in range(q):
            queries.append(list(map(int, inp[i + 1].rstrip().split())))

        ans = freqQuery(queries)
