#!/bin/python3
# https://leetcode.com/problems/roman-to-integer/

numerals = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1 
}

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0

        while i < len(s):
            for numeral in numerals.keys():
                if len(numeral) == 1 and numeral == s[i]:
                    result += numerals[numeral]
                    i += 1
                    break
                elif len(numeral) == 2 and numeral[0] == s[i] and i + 1 < len(s) and numeral[1] == s[i + 1]:
                    result += numerals[numeral]
                    i += 2
                    break

        return result

Solution().romanToInt("IV")
