#!/bin/python3
# https://leetcode.com/problems/ransom-note/

import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_histogram = collections.Counter(ransomNote)
        magazine_histogram = collections.Counter(magazine)

        for c, count in note_histogram.items():
            if magazine_histogram[c] < count:
                return False

        return True