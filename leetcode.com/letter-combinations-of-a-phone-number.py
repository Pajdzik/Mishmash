#!/bin/python3
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

phone_keyboard = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        combinations = phone_keyboard[digits[0]].copy()

        for digit in digits[1:]:
            new_combinations = []

            while len(combinations) > 0:
                combination = combinations.pop()
                
                for letter in phone_keyboard[digit]:
                    new_combinations.append(combination + letter)

            combinations = new_combinations

        return combinations

Solution().letterCombinations('234')