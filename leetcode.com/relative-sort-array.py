#!/bin/python3
# https://leetcode.com/problems/relative-sort-array

from collections import Counter


class Solution:
    def relativeSortArray(
        self, longerArray: list[int], orderArray: list[int]
    ) -> list[int]:
        freq = Counter(longerArray)

        result = []
        for num in orderArray:
            result.extend([num] * freq[num])
            del freq[num]

        for num, count in sorted(freq.items()):
            result.extend([num] * count)

        return result


if __name__ == "__main__":

    def test(expected: list[int], longerArray: list[int], orderArray: list[int]):
        s = Solution()
        result = s.relativeSortArray(longerArray, orderArray)
        assert result == expected, f"expected {expected} but got {result}"

    test([22, 28, 8, 6, 17, 44], [28, 6, 22, 8, 44, 17], [22, 28, 8, 6])

    test(
        [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
        [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
        [2, 1, 4, 3, 9, 6],
    )
