#!/bin/python3
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        result = 0
        for operation in operations:
            if operation[0] == "-" or operation[-1] == "-":
                result -= 1
            else:
                result += 1

        return result
