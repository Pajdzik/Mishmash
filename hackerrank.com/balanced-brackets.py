#!/bin/python3
#https://www.hackerrank.com/challenges/balanced-brackets

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        elif len(stack) == 0:
            return "NO"
        elif c == ')':
            if stack[-1] != '(':
                return "NO"
            else:
                stack.pop()
        elif c == '}':
            if stack[-1] != '{':
                return "NO"
            else:
                stack.pop()
        elif c == ']':
            if stack[-1] != '[':
                return "NO"
            else:
                stack.pop()

    return "YES" if len(stack) == 0 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
