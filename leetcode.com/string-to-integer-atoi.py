#!/bin/python3
# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def is_digit(self, c: str) -> bool:
        return ord("0") <= ord(c) <= ord("9")

    def myAtoi(self, s: str) -> int:
        digits = []
        sign = None

        start_index = None
        for i in range(len(s)):
            c = s[i]
            if not sign and c == " ":
                continue
            elif not sign and c == "+":
                sign = 1
            elif not sign and c == "-":
                sign = -1
            elif self.is_digit(c):
                start_index = i
                break
            else:
                return 0

        if start_index == None:
            return 0
        
        digit_loaded = False
        for i in range(start_index, len(s)):
            c = s[i]
            if not self.is_digit(c):
                if digit_loaded:
                    break
                else:
                    return 0
            else:
                digit_loaded = True
                digit = ord(c) - 48
                digits.append(digit)

        if not sign:
            sign = 1

        base = 1 * sign
        number = 0
        for n in range(0, len(digits)):
            digit = digits[len(digits) - 1 - n]
            number += digit * base
            base *= 10

            if number >= 2**31 - 1:
                return 2**31 - 1
            elif number <= -(2**31):
                return -(2**31)

        number = number
        return number

if __name__ == "__main__":
    Solution().myAtoi("21474836460")