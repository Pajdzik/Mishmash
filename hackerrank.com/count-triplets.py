#!/bin/python3
#https://www.hackerrank.com/challenges/count-triplets-1

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets_polynomial(arr, r):
    sarr = sorted(arr)
    c = 0

    for i in range(0, len(sarr) - 2):
        for j in range(i + 1, len(sarr) - 1):
            for k in range(j + 1, len(sarr)):
                if (r * sarr[i] == sarr[j] and r * sarr[j] == sarr[k]):
                    c += 1

    return c

def countTriplets_polynomial2(arr, r):
    filterred_arr = filter(lambda x: x == 1 or x % r == 0, arr)
    sarr = sorted(filterred_arr)
    l = len(sarr)
    c = 0

    for i in range(l - 2):
        d1 = sarr[i]
        for j in range(i + 1, l - 1):
            d2 = sarr[j]
            if d2 > d1 * r:
                break

            if d2 == d1 * r:
                for k in range(j + 1, l):
                    d3 = sarr[k]
                    if d3 > d2 * r:
                        break

                    if d3 == d2 * r:
                        c += 1
    return c

def countTriplets_old(arr, r):
    c = 0
    filterred_arr = list(filter(lambda x: x == 1 or x % r == 0, arr))

    visited = set()
    sarr = { }
    for x in filterred_arr:
        sarr[x] = sarr[x] + 1 if x in sarr else 1

    for i in filterred_arr:
        if (i in visited):
            continue

        visited.add(i)
        ir = i * r
        irr = i * r * r

        if r != 1 and ir in sarr and irr in sarr and arr.index(i) < arr.index(ir) < arr.index(irr):
            c += sarr[i] * sarr[ir] * sarr[irr]

        if r == 1 and sarr[i] >= 3:
            ic = sarr[i]
            c += int((math.factorial(ic)) / (6 * math.factorial(ic - 3)))

    return c

def countTriplets_fail_06_10(arr, r):
    count = 0
    hist = {}
    for d in sorted(arr):
        if d == 1 or d % r == 0:
            hist[d] = hist[d] + 1 if d in hist else 1

    keys = hist.keys()
    if r == 1:
        for e in keys:
            c = hist[e]
            count += int((c * (c-1) * (c-2))/6)

        return count

    for em in keys:
        cm = hist[em]
        el = em / r
        eh = em * r
        if cm == 0 or el not in hist or eh not in hist:
            continue
       
        count += hist[el] * cm * hist[eh]

    return count

def countTriplets(arr, r):
    count = 0
    pairs = {}
    hist = {}

    for x in arr[::-1]:
        rx = r * x
        rrx = r * rx

        count += pairs.get((rx, rrx), 0)
        pairs[(x, rx)] = pairs.get((x, rx), 0) + hist.get(rx, 0)
        hist[x] = hist.get(x, 0) + 1

    return count

if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input", "count-triplets.061339347780085.txt"), "r") as f:
        i = f.readlines()
        nr = i[0].rstrip().split()
        n = int(nr[0])
        r = int(nr[1])
        arr = list(map(int, ("".join(i[1:])).rstrip().split()))
        ans = countTriplets(arr, r)
        print(ans)
        # ans = countTriplets([1, 10, 10, 100], 10)
        # print(ans)