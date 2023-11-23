#!/bin/python3
# https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_counter = {
            'A': 0,
            'E': 0,
            'I': 0,
            'O': 0,
            'U': 0,
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }

        vowel_indices = []
        s_array = list(s)

        for i, c in enumerate(s_array):
            if c in vowel_counter:
                vowel_counter[c] += 1
                vowel_indices.append(i)

        vowel_index_index = 0
        for vowel in vowel_counter:
            while vowel_index_index < len(vowel_indices) and vowel_counter[vowel] > 0:
                vowel_index = vowel_indices[vowel_index_index]
                s_array[vowel_index] = vowel
                vowel_index_index += 1
                vowel_counter[vowel] -= 1

        return ''.join(s_array)


if __name__ == "__main__":
    def test(expected: str, s: str):
        result = Solution().sortVowels(s)
        if expected != result:
            raise AssertionError(f'Expected {expected} was {result}')

    test("lEOtcede", "lEetcOde")
    test("lYmpH", "lYmpH")
