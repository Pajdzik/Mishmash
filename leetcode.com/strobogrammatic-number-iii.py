#!/bin/python3
# https://leetcode.com/problems/strobogrammatic-number-iii/

strobogrammatic_map = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}

def check_if_strobogrammatic(num: str):
        for i in range(0, len(num) // 2 + 1):
            other_letter = num[len(num) - i  - 1]
            if num[i] not in strobogrammatic_map:
                return False
            if other_letter not in strobogrammatic_map:
                return False
            if num[i] != strobogrammatic_map[other_letter]:
                return False

        return True

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        total_count = 0
        for n in range(int(low), int(high) + 1):
            number = str(n)
            if number[0] == 0 or any(map(lambda x: x not in strobogrammatic_map, number)):
                continue

            if check_if_strobogrammatic(number):
                total_count += 1

        return total_count
