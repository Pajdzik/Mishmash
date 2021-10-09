#!/bin/python3
# https://leetcode.com/problems/decode-ways/

class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def numDecodings(self, s: str, index: int = 0) -> int:
        if index in self.cache:
            return self.cache[index]

        count = None
        if index < len(s) and s[index] == '0':
            count = 0
        elif index >= len(s) - 1:
            count = 1
        else:
            count = self.numDecodings(s, index + 1)
            if s[index] == '1' or (s[index] == '2' and s[index + 1] < '7'):
                count += self.numDecodings(s, index + 2)

        self.cache[index] = count
        return count

if __name__ == "__main__":
    assert(Solution().numDecodings("1123") == 5)
            