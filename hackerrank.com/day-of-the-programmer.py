#!/bin/python3
#https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    cal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if ((year > 1918) and (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        cal[1] = 29
    elif ((year < 1918) and (year % 4 == 0)):
        cal[1] = 29

    if year == 1918:
        cal[1] = 15

    dth = 256
    month = 0
    day = 0

    for i in range(0, len(cal)):
        if (dth < cal[i]):
            month = i
            day = dth
            break

        dth = dth - cal[i]
        

    return "{:02d}.{:02d}.{}".format(day, month + 1, year)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip())
    result = dayOfProgrammer(year)
    fptr.write(result + '\n')
    fptr.close()
