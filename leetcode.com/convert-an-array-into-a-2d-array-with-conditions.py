#!/bin/python3
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions

from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result = []
        last_row = {}

        for num in nums:
            row_index = 0
            if num in last_row:
                row_index = last_row[num]

            last_row[num] = row_index + 1

            if len(result) <= row_index:
                result.append([])

            result[row_index].append(num)

        return result

    def findMatrix_counter(self, nums: list[int]) -> list[list[int]]:
        counter = Counter(nums)

        result = []

        while counter:
            result.append(list(counter.keys()))
            to_remove = []

            for k in counter:
                new_count = counter[k] - 1
                if new_count:
                    counter[k] = new_count
                else:
                    to_remove.append(k)

            for k in to_remove:
                del counter[k]

        return result


if __name__ == "__main__":

    def test(expected: list[list[int]], nums: list[int]):
        s = Solution()
        result = s.findMatrix(nums)
        assert result == expected, f"expected {expected} but got {result}"

    test([[1, 3, 4, 2], [1, 3], [1]], [1, 3, 4, 1, 2, 3, 1])
