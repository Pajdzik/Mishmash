#!/bin/python3
#https://www.hackerrank.com/challenges/greedy-florist/problem

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(friends_count, prices):
    cost = 0
    
    prices = sorted(prices, reverse=True)
    for i in range(len(prices)):
        cost += prices[i] * (1 + (i // friends_count))

    return cost


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)

