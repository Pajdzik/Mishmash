#!/bin/python3
# https://leetcode.com/problems/find-common-characters


from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        char_counters = [Counter(word) for word in words]

        letters_present_in_every_word = []
        for c in range(ord("a"), ord("z") + 1):
            count = sum([1 if chr(c) in cc else 0 for cc in char_counters])
            if count == len(words):
                letters_present_in_every_word.append(chr(c))

        result = []
        for l in letters_present_in_every_word:
            min_count = min([counter[l] for counter in char_counters])
            result.extend([l] * min_count)

        return result


if __name__ == "__main__":

    def test(expected: list[str], words: list[str]):
        s = Solution()
        result = s.commonChars(words)
        assert result == expected, f"expected {expected} but got {result}"

    test(["e", "l", "l"], ["bella", "label", "roller"])
    test(["c", "o"], ["cool", "lock", "cook"])
