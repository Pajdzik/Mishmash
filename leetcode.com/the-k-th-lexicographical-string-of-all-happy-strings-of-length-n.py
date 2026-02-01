#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional

"""
0: 
1: a b c
2: aa ab ac  ba bb bc  ca cb cc
3: aaa aab aac  aba abb abc  aca acb acc
   baa bab bac  bba bbb bbc  bca bcb bcc

"""


class Solution:
    def getHappyString(self, word_len: int, k: int) -> str:
        alphabet = ["a", "b", "c"]
        last_alphabet_char_index = len(alphabet) - 1

        def is_happy(word: list[int]) -> bool:
            for i in range(len(word) - 1):
                if word[i] == word[i + 1]:
                    return False

            return True

        def generate() -> str:
            count = k
            word = [0] * word_len
            last_letter_index = word_len - 1
            index = last_letter_index

            while count > 0:
                if is_happy(word):
                    count -= 1
                    if count == 0:
                        return "".join([alphabet[i] for i in word])

                reset = False
                i = index
                while i >= 0 and word[i] >= last_alphabet_char_index:
                    # reset the current letter
                    word[i] = 0
                    i -= 1
                    if i < 0:
                        return ""
                    reset = True

                if reset:
                    index = last_letter_index

                word[i] += 1

            return ""

        return generate()


if __name__ == "__main__":
    assert Solution().getHappyString(2, 7) == ""
    assert Solution().getHappyString(1, 4) == ""
    assert Solution().getHappyString(3, 9) == "cab"
    assert Solution().getHappyString(1, 3) == "c"
