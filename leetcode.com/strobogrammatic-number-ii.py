#!/bin/python3
# https://leetcode.com/problems/strobogrammatic-number-ii/

from cmath import sin


strobogrammatic_map = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}

def gen_next(nums: list[str], is_final: bool) -> list[str]:
    result = []

    for num in nums:
        if not is_final:
            result.append('0' + num + '0')
            
        result.append('1' + num + '1')
        result.append('6' + num + '9')
        result.append('8' + num + '8')
        result.append('9' + num + '6')

    return result

class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        singles = ['0', '1', '8']
        doubles = ['11', '69', '88', '96']

        words, i = None, None
        if n % 2 == 0:
            words, i = doubles, 2
            if n > 2:
                doubles.append('00')
        else:
            words, i = singles, 1

        while i < n:
            i += 2
            words = gen_next(words, i == n)

        return words

Solution().findStrobogrammatic(4)
