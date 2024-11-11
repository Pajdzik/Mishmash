#!/bin/python3
# https://leetcode.com/problems/prime-subtraction-operation


import bisect
from typing import List, Optional


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def find_prime(num: int, nxt: int) -> Optional[int]:
            primes = [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
                101,
                103,
                107,
                109,
                113,
                127,
                131,
                137,
                139,
                149,
                151,
                157,
                163,
                167,
                173,
                179,
                181,
                191,
                193,
                197,
                199,
                211,
                223,
                227,
                229,
                233,
                239,
                241,
                251,
                257,
                263,
                269,
                271,
                277,
                281,
                283,
                293,
                307,
                311,
                313,
                317,
                331,
                337,
                347,
                349,
                353,
                359,
                367,
                373,
                379,
                383,
                389,
                397,
                401,
                409,
                419,
                421,
                431,
                433,
                439,
                443,
                449,
                457,
                461,
                463,
                467,
                479,
                487,
                491,
                499,
                503,
                509,
                521,
                523,
                541,
                547,
                557,
                563,
                569,
                571,
                577,
                587,
                593,
                599,
                601,
                607,
                613,
                617,
                619,
                631,
                641,
                643,
                647,
                653,
                659,
                661,
                673,
                677,
                683,
                691,
                701,
                709,
                719,
                727,
                733,
                739,
                743,
                751,
                757,
                761,
                769,
                773,
                787,
                797,
                809,
                811,
                821,
                823,
                827,
                829,
                839,
                853,
                857,
                859,
                863,
                877,
                881,
                883,
                887,
                907,
                911,
                919,
                929,
                937,
                941,
                947,
                953,
                967,
                971,
                977,
                983,
                991,
                997,
            ]

            index = bisect.bisect_left(primes, num - nxt)

            while index < len(primes) and num - primes[index] >= nxt:
                index += 1

            if index >= len(primes):
                return 10000

            return primes[index]

        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            nxt = nums[i + 1]

            if nxt > num:
                continue

            prime_to_subtract = find_prime(num, nxt)
            nums[i] -= prime_to_subtract
            if nums[i] <= 0:
                return False

        return True


def invoke():
    def test(expected: bool, nums: List[int]):
        solution = Solution()
        result = solution.primeSubOperation(nums)
        assert result == expected, f"Expected {expected}, but got {result}"

    test(True, [4, 9, 6])
    test(True, [15, 20, 17, 7, 16])
    test(False, [2, 2])
    test(False, [5, 8, 3])


if __name__ == "__main__":
    invoke()
