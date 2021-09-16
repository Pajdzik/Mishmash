#!/bin/python3
# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, substring: str, word: str) -> bool:
        if len(substring) > len(word):
            return False

        histogram_sub = [0] * (ord('z') - ord('a') + 1)
        histogram_word = [0] * (ord('z') - ord('a') + 1)

        for i in range(len(substring)):
            histogram_sub[ord(substring[i]) - ord('a')] += 1
            histogram_word[ord(word[i]) - ord('a')] += 1

        matching = 0
        for i in range(len(histogram_sub)):
            if histogram_sub[i] == histogram_word[i]:
                matching += 1

        if matching == len(histogram_word):
            return True

        i = 0
        while i < len(word) - len(substring):
            old_char = word[i]
            old_index = ord(old_char) - ord('a')
            new_char = word[i + len(substring)]
            new_index = ord(new_char) - ord('a')

            histogram_word[old_index] -= 1

            if histogram_word[old_index] == histogram_sub[old_index]:
                matching += 1
            elif histogram_word[old_index] + 1 == histogram_sub[old_index]:
                matching -= 1

            histogram_word[new_index] += 1

            if histogram_word[new_index] == histogram_sub[new_index]:
                matching += 1
            elif histogram_word[new_index] - 1 == histogram_sub[new_index]:
                matching -= 1

            if matching == len(histogram_word):
                return True

            i += 1

        return False


Solution().checkInclusion("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine")