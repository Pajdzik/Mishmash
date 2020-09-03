#!/bin/python3
#https://www.hackerrank.com/challenges/frequency-queries

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    ans = []
    stack = {}
    count = {}

    for query in queries:
        command = query[0]
        argument = query[1]
        
        if command == 1:
            if argument in stack:
                no = stack[argument]
                stack[argument] = no + 1
                count[no] -= 1
                if no + 1 in count:
                    count[no + 1] += 1
                else:
                    count[no + 1] = 1
            else:
                stack[argument] = 1
                count[1] = count[1] + 1 if 1 in count else 1

        elif command == 2:
            if argument not in stack:
                continue

            no = stack[argument]
            stack[argument] = no - 1
            count[no] -= 1
            if no - 1 in count:
                count[no - 1] += 1
            else:
                count[no - 1] = 1

        else:
            ans.append(1 if argument in count and count[argument] > 0 else 0)

    return ans

if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input", "frequency-queries.08.txt"), "r") as f:
        inp = f.readlines()

        q = int(inp[0].strip())

        queries = []

        for i in range(q):
            queries.append(list(map(int, inp[i + 1].rstrip().split())))

        ans = freqQuery(queries)
