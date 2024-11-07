#!/bin/python3
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero

# [16,17,71,62,12,24,14]


class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        bit_count = [0] * 24
        mask = 1

        for candidate in candidates:
            for mask_shift in range(len(bit_count)):
                if (mask << mask_shift) & candidate > 0:
                    bit_count[mask_shift] += 1

        return max(bit_count)


if __name__ == "__main__":

    def test(expected, candidates):
        result = Solution().largestCombination(candidates)
        assert result == expected, f"Expected {expected}, but got {result}"

    test(1, [8388608])
    test(4, [16, 17, 71, 62, 12, 24, 14])
