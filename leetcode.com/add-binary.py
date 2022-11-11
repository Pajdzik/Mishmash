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
    
    def addBinary2(self, a: str, b: str) -> str:
        l = 1
        carry = 0
        result = []

        while l <= max(len(a), len(b)):
            ai = int(a[-l]) if l <= len(a) else 0
            bi = int(b[-l]) if l <= len(b) else 0

            si = ai + bi + carry

            result.append(str(si % 2))
            carry = si // 2
            l += 1

        if carry:
            result.append("1")
        result.reverse()
        return ''.join(result)

res = Solution().addBinary("11", "1")
print(res)