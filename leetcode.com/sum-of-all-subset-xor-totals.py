#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional

"""
[2, 5, 6]
.
[] [x, x, x]
..
[2] [o, x, x]
[5] [x, o, x]
[6] [x, x, o]
...
[2, 5] [o, o, x]
[2, 6] [o, x, o]
[5, 6] [x, o, o]
....
[2, 5, 6] [o, o, o]


"""


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def list_xor(picked: List[bool]):
            xor = 0
            for i, num in enumerate(nums):
                if picked[i]:
                    xor = xor ^ num
            return xor

        def count_xors(picked: List[bool], i: int) -> int:
            if i >= len(nums):
                return list_xor(picked)

            count = 0

            next_picked_when_picked = picked[:]
            next_picked_when_picked[i] = True
            count += count_xors(next_picked_when_picked, i + 1)

            next_picked_when_not_picked = picked[:]
            next_picked_when_not_picked[i] = False
            count += count_xors(next_picked_when_not_picked, i + 1)

            return count

        return count_xors([False] * len(nums), 0)


if __name__ == "__main__":
    sol = Solution().subsetXORSum([5, 1, 6])
    assert sol == 28
