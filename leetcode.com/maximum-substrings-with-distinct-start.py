#!/bin/python3
# https://leetcode.com/problems/maximum-substrings-with-distinct-start/


class Solution:
    def maxDistinct(self, s: str) -> int:
        mem = set(s)
        return len(mem)


if __name__ == "__main__":
    assert Solution().maxDistinct("abab") == 2
    assert Solution().maxDistinct("abcd") == 4
    assert Solution().maxDistinct("aaaa") == 1
