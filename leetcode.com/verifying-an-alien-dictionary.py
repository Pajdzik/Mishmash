#!/bin/python3
# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def compare(self, word: str, otherWord: str, order: str) -> int:
        for i in range(max(len(word), len(otherWord))):
            if i == len(word):
                return -1
            elif i == len(otherWord):
                return 1
            elif order.index(word[i]) < order.index(otherWord[i]):
                return -1
            elif order.index(word[i]) > order.index(otherWord[i]):
                return 1
            elif i + 1 == len(word) == len(otherWord) > 1:
                return 0

    def isAlienSorted(self, words: list[str], order: str) -> bool:
        for i in range(len(words) - 1):
            if self.compare(words[i], words[i + 1], order) > 0:
                return False

        return True

result = Solution().isAlienSorted(["l","h"], "xkbwnqozvterhpjifgualycmds")
print(result)