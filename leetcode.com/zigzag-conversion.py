#!/bin/python3
# https://leetcode.com/problems/zigzag-conversion/

# 0     4      8      12
# 1  3  5  7   9  11  13
# 2     6     10 

# 0 4 8 11   1 3 5 7 9 11 13  2 6 10


# 0        6          12
# 1     5  7      11  13
# 2  4     8  10      14
# 3        9          15

# 0 6 12   1 5 7 11 13  2 4 8 10 14   3 9 15


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
            
        result = []
        i = 0
        cycleLen = numRows * 2 - 2

        for i in range(numRows):
            for j in range(i, len(s), cycleLen):
                result.append(s[j])
                if 0 < i < numRows - 1 and j + cycleLen - (2*i) < len(s):
                    result.append(s[j + cycleLen - (2*i)])


        return ''.join(result)
