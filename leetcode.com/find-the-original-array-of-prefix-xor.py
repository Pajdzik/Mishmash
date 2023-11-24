#!/bin/python3
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        for i in range(len(pref) - 1, 0, -1):
            pref[i] = pref[i] ^ pref[i - 1]

        return pref

    def findArray_mask(self, pref: list[int]) -> list[int]:
        result = pref[:1]

        xor_of_processed_numbers = result[-1]

        for i in range(1, len(pref)):
            xor_result = pref[i]
            mask = 1

            num2 = 0

            while mask <= max(xor_of_processed_numbers, xor_result):
                b1 = xor_of_processed_numbers & mask
                b2 = xor_result & mask

                if b1 != b2:
                    num2 += mask

                mask <<= 1

            result.append(num2)
            xor_of_processed_numbers ^= num2

        return result


if __name__ == "__main__":
    def test(expected: list[int], pref: list[int]):
        result = Solution().findArray(pref)
        if expected != result:
            raise AssertionError(f'Expected {expected} was {result}')

    test([5, 7, 2, 3, 2], [5, 2, 0, 3, 1])
"""
I: [5,2,0,3,1]
1 ^ 3 = 2
3 ^ 0 = 3
0 ^ 2 = 2
2 ^ 5 = 7

O: [5,7,2,3,2]
"""

"""
I: [5,2,0,3,1]
O: [5,7,2,3,2]

5
-
5 ^ x = 2
101 ^ x = 010
10

0 ^ x = 0 => 0
0 ^ x = 1 => 1
1 ^ x = 0 => 1
1 ^ x = 1 => 0
"""

"""
[5, 7, 2, 3, 2]
5
5 ^ 7 = 2
2 ^ 2 = 0
0 ^ 3 = 3
3 ^ 2 = 1
"""
