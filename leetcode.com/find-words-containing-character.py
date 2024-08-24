#!/bin/python3
# https://leetcode.com/problems/find-words-containing-character

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, el in enumerate(words):
            if x in el:
                result.append(i)

        return result
