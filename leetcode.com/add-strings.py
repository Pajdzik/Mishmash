#!/bin/python3
# https://leetcode.com/problems/add-strings/

from linecache import cache


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1) - 1
        l2 = len(num2) - 1

        base = ord('0')
        carry = False

        max_length = max(len(num1), len(num2))
        result = [ "" ] * (max_length + 1)

        for i in range(0, max_length):
            char1 = num1[l1 - i] if i <= l1 else "0"
            char2 = num2[l2 - i] if i <= l2 else "0"

            digit1 = ord(char1) - base
            digit2 = ord(char2) - base

            added_digits = digit1 + digit2
            if carry:
                added_digits += 1
            
            result[max_length - i] = chr(base + (added_digits % 10))
            carry = added_digits >= 10

        if carry:
            result[0] = "1"

        return ''.join(result)
            
if __name__ == "__main__":
    assert(Solution().addStrings("123", "456") == "579")
    assert(Solution().addStrings("123", "1456") == "1579")
    assert(Solution().addStrings("99", "999") == "1098")