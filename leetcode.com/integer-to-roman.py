#!/bin/python3
# https://leetcode.com/problems/integer-to-roman/

numerals = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_number = ""
        while num > 0:
            for (dec_numeral, roman_numeral) in numerals.items():
                if num >= dec_numeral:
                    roman_number += roman_numeral
                    num -= dec_numeral
                    break

        return roman_number

Solution().intToRoman(20)