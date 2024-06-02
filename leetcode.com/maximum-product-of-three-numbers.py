#!/bin/python3
# https://leetcode.com/problems/maximum-product-of-three-numbers

import heapq


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)

        if sorted_nums[-1] <= 0 or sorted_nums[0] >= 0:
            # signs are not mixed
            return sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3]

        return max(
            sorted_nums[0] * sorted_nums[1] * sorted_nums[-1],
            sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3],
        )

    def maximumProduct_positive(self, nums: list[int]) -> int:
        max_heap = nums[:3]
        heapq.heapify(max_heap)

        for n in nums[3:]:
            if max_heap[2] < n:
                heapq.heappushpop(max_heap, n)

        return max_heap[0] * max_heap[1] * max_heap[2]


if __name__ == "__main__":

    def test(expected: int, args: list[int]):
        result = Solution().maximumProduct(args)
        assert result == expected, f"{result} != {expected}"

    test(
        943695360,
        [
            722,
            634,
            -504,
            -379,
            163,
            -613,
            -842,
            -578,
            750,
            951,
            -158,
            30,
            -238,
            -392,
            -487,
            -797,
            -157,
            -374,
            999,
            -5,
            -521,
            -879,
            -858,
            382,
            626,
            803,
            -347,
            903,
            -205,
            57,
            -342,
            186,
            -736,
            17,
            83,
            726,
            -960,
            343,
            -984,
            937,
            -758,
            -122,
            577,
            -595,
            -544,
            -559,
            903,
            -183,
            192,
            825,
            368,
            -674,
            57,
            -959,
            884,
            29,
            -681,
            -339,
            582,
            969,
            -95,
            -455,
            -275,
            205,
            -548,
            79,
            258,
            35,
            233,
            203,
            20,
            -936,
            878,
            -868,
            -458,
            -882,
            867,
            -664,
            -892,
            -687,
            322,
            844,
            -745,
            447,
            -909,
            -586,
            69,
            -88,
            88,
            445,
            -553,
            -666,
            130,
            -640,
            -918,
            -7,
            -420,
            -368,
            250,
            -786,
        ],
    )
    test(1120, [-8, -7, -2, 10, 20])
    test(39200, [-100, -98, -1, 2, 3, 4])
    test(6, [1, 2, 3])
    test(24, [1, 2, 3, 4])
    test(60, [1, 2, 3, 4, 5])
    test(-6, [-1, -2, -3, -4])
