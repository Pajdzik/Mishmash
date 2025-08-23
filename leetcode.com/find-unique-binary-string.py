#!/bin/python3
# https://leetcode.com/problems/find-unique-binary-string/


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        s = set()

        for b in nums:
            n = int(b, 2)
            s.add(n)

        i = 0
        while True:
            if i not in s:
                break
            i += 1

        return bin(i)[2:].rjust(len(nums[0]), "0")


if __name__ == "__main__":
    Solution().findDifferentBinaryString(["00", "10"])
    Solution().findDifferentBinaryString(["00", "01"])
    Solution().findDifferentBinaryString(["01", "10"])
