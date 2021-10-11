#!/bin/python3
# https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0

        diff = nums[1] - nums[0]
        curr_length = 2
        result = 0

        for i in range(2, len(nums)):
            new_diff = nums[i] - nums[i - 1]
            if new_diff == diff:
                curr_length += 1

                if curr_length >= 3:
                    result += curr_length - 2
            else:
                diff = new_diff
                curr_length = 2

        return result
        
    def numberOfArithmeticSlices_iterative(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0

        prev = nums[0]
        curr = nums[1]
        diff = curr - prev

        count = 0
        curr_sequence_len = 2

        def get_seqs_count(seq_length: int) -> int:
            n = curr_sequence_len - 2
            seq_count = (n * (n + 1)) // 2
            return seq_count

        for i in range(2, len(nums)):
            next = nums[i]

            if diff == next - curr:
                curr_sequence_len += 1
            else:
                if curr_sequence_len >= 3:
                    count += get_seqs_count(curr_sequence_len)

                curr_sequence_len = 2
                diff = next - curr

            prev, curr = curr, next

        if curr_sequence_len >= 3:
            count += get_seqs_count(curr_sequence_len)

        return count

if __name__ == "__main__":
    Solution().numberOfArithmeticSlices([1, 2, 3, 4, 5])
            