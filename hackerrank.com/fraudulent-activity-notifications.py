#!/bin/python3
#https://www.hackerrank.com/challenges/fraudulent-activity-notifications

from math import ceil, floor
import os
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    c = 0

    value_count = [0 for _ in range(max(expenditure) + 1)]
    for i in range(0, d):
        value_count[expenditure[i]] += 1

    median_i, median_j = (d - 1)//2 + 1, (d)//2 + 1

    for i in range(d, len(expenditure)):
        pos = 0
        m1, m2 = None, None
        for m in range(0, len(value_count)):
            pos += value_count[m]
            if m1 == None and pos >= median_i:
                m1 = m
            if pos >= median_j:
                m2 = m
                break

        last_element = expenditure[i]
        if last_element >= (m1 + m2):
            c += 1

        first_element = expenditure[i - d]

        value_count[first_element] -= 1
        value_count[last_element] += 1

    return c

if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input", "fraudulent-activity-notifications.03.txt"), "r") as f:
        # i = f.readlines()
        first_multiple_input = "5 4".rstrip().split()
        n = int(first_multiple_input[0])
        d = int(first_multiple_input[1])
        expenditure = list(map(int, "10 20 30 40 50".rstrip().split()))
        result = activityNotifications(expenditure, d)
