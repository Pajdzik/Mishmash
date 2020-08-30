#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-ice-cream-parlor

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_map = { }
    dups_map = { }

    for i in range(len(cost)):
        if cost[i] in cost_map:
            if cost[i] in dups_map:
                dups_map[cost[i]].append(i)
            else:
                dups_map[cost[i]] = [cost_map[cost[i]], i]

        cost_map[cost[i]] = i 
        

    for c1 in cost_map:
        c2 = money - c1
        if c1 == c2 and c1 in dups_map:
            print('%d %d' % (dups_map[c1][0] + 1, dups_map[c2][1] + 1))
            return 
        if c1 != c2 and c2 in cost_map:
            print('%d %d' % (cost_map[c1] + 1, cost_map[c2] + 1))
            return


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input", "hash-tables-ice-cream-parlor.10.txt"), "r") as f:
        inp = f.readlines()
        idx = 0
        t = int(inp[idx])
        idx += 1

        for t_itr in range(t):
            money = int(inp[idx])
            idx += 1

            n = int(inp[idx])
            idx += 1

            cost = list(map(int, inp[idx].rstrip().split()))
            idx += 1

            whatFlavors(cost, money)
