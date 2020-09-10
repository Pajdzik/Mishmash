#!/bin/python3
#https://www.hackerrank.com/challenges/max-array-sum

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    max_arr = arr.copy()

    max_arr[0] = arr[0]
    max_arr[1] = max(arr[0], arr[1])
    global_max = max_arr[1]

    for i in range(2, len(arr)):
        past_two_value = max_arr[i - 2]
        global_max = max(past_two_value, past_two_value + arr[i], arr[i], global_max)
        max_arr[i] = global_max

    return global_max
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
