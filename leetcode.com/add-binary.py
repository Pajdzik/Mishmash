#!/bin/python3
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        (a, b) = (a, b) if len(a) > len(b) else (b, a)
        result = [ None for _ in range(len(a))]
        carry = False

        for i in range(0, len(a)):
            if a[len(a) - i - 1] == '1' and (i < len(b) and b[len(b) - i - 1] == '1'):
                result[len(a) - i - 1] = '1' if carry else '0'
                carry = True
            elif a[len(a) - i - 1] == '0' and (i >= len(b) or b[len(b) - i - 1] == '0'):
                result[len(a) - i - 1] = '1' if carry else '0'
                carry = False
            else:
                result[len(a) - i - 1] = '0' if carry else '1'

        if carry:
            result.insert(0, '1')

        return ''.join(result)

res = Solution().addBinary("11", "1")
print(res)