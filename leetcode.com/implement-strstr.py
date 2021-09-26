#!/bin/python3
# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or needle == "":
            return 0

        step = 0
        steps = [ 0 for _ in range(len(needle)) ]
        i = 1
        while i < len(needle):
            if needle[i] == needle[step]:
                step += 1
                steps[i] = step
                i += 1
            else:
                if step != 0:
                    step = steps[step - 1]
                else:
                    i += 1

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == len(needle):
                    return i - j
            else:
                if j > 0:
                    j = steps[j - 1]
                else:
                    i += 1

        return -1

result = Solution().strStr("mississippi", "issip")
assert(result > 0)