#!/bin/python3
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        index = 0

        if len(strs) == 1:
            return strs[0]

        while True:
            if len(strs[0]) > index:
                letter_to_test = strs[0][index]
            else:
                return prefix

            for str in strs:
                if index >= len(str) or str[index] != letter_to_test:
                    return prefix

            prefix += letter_to_test
            index += 1

result = Solution().longestCommonPrefix([""])
print(result)