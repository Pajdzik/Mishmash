#!/bin/python3
#https://www.hackerrank.com/challenges/fraudulent-activity-notifications

import math
import os
import random
import re
import sys

def median(arr):
    data = sorted(arr)
    l = len(data)
    l2 = int(l / 2)
    med = ((data[l2] + data[l2 - 1]) / 2.0) if l % 2 == 0 else data[l2]
    return med

# Quickselect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    c = 0

    for i in range(d, len(expenditure)):
        med = median(expenditure[i - d:i])
        if expenditure[i] >= 2 * med:
            c += 1

    return c

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = "5 3".split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, "10 20 30 40 50".rstrip().split()))
    result = activityNotifications(expenditure, d)
    #fptr.write(str(result) + '\n')
    #fptr.close()
