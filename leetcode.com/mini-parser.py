#!/bin/python3
#https://leetcode.com/problems/mini-parser

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""

from typing import Tuple, Union


class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

"""
[123,[456,[789]]]

root = ()

[ -> load list
] -> return list 

"""

class Solution:
    def deserialize(self, s: str):
        def load_number(s: str, i: int) -> Tuple[NestedInteger, int]:
            result = 0
            sign = 1

            if s[i] == '-':
                sign = -1
                i += 1

            while i < len(s) and s[i] not in [',', '[', ']']:
                result *= 10
                result += int(s[i])
                i += 1

            return NestedInteger((sign * result)), i


        def deserialize_rec(s: str, i: int) -> Tuple[NestedInteger, int]:
            if i >= len(s):
                # single number case
                return None, i
            elif s[i] == '[':
                parent = NestedInteger()
                i += 1

                while i < len(s) and s[i] != ']':
                    value, i = deserialize_rec(s, i)
                    if value is not None:
                        parent.add(value)
                    if i < len(s) and s[i] == ',':
                        # continue loading numbers
                        i += 1

                return parent, (i + 1)
            else:
                return load_number(s, i)

        res, _ = deserialize_rec(s, 0)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.deserialize("324"))
    # print(solution.deserialize("[123,[456,[789]]]"))