#!/bin/python3
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/


from typing import Counter, List, Optional


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        alphabet = set([chr(c) for c in range(ord("a"), ord("z") + 1)])
        consonants = alphabet.symmetric_difference(vowels)
        counter = Counter()

        for c in s:
            counter[c] += 1

        max_vowel_count = max([counter[c] for c in vowels])
        max_consonant_count = max([counter[c] for c in consonants])

        return max_vowel_count + max_consonant_count


if __name__ == "__main__":
    Solution().maxFreqSum("fgadfwfweffew")
