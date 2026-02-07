#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(number: List[int], picked: List[bool], numbers: List[List[int]]):
            if len(number) == len(nums):
                numbers.append(number)

            for i in range(0, len(nums)):
                if picked[i]:
                    continue

                picked[i] = True
                number.append(nums[i])
                permute(number[:], picked, numbers)
                number.pop()
                picked[i] = False

        def dedup(numbers: List[List[int]]) -> List[List[int]]:
            s = set()
            result = []

            for number in numbers:
                key = ".".join([str(n) for n in number])
                if key in s:
                    continue

                s.add(key)
                result.append(number)

            return result

        picked = [False] * len(nums)
        numbers = []
        permute([], picked, numbers)
        return dedup(numbers)


if __name__ == "__main__":
    Solution().permuteUnique([1, 2, 3])
