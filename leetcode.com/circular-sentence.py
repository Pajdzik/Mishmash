#!/bin/python3
# https://leetcode.com/problems/circular-sentence


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False

        index_of_last_letter = 1

        while index_of_last_letter < len(sentence):
            while (
                index_of_last_letter + 1 < len(sentence)
                and sentence[index_of_last_letter + 1] != " "
            ):
                index_of_last_letter += 1

            if index_of_last_letter + 1 >= len(sentence):
                break

            if sentence[index_of_last_letter] != sentence[index_of_last_letter + 2]:
                return False

            index_of_last_letter += 2

        return True

    def isCircularSentence_2(self, sentence: str) -> bool:
        words = sentence.split(" ")
        for i in range(len(words)):
            if words[i - 1][-1] != words[i][0]:
                return False
        return True


if __name__ == "__main__":

    def test(expected: bool, sentence: str):
        s = Solution()
        result = s.isCircularSentence(sentence)
        assert result == expected, f"{result=}, {expected=}, {sentence=}"

    test(True, "leetcode exercises sound delightful")
    test(False, "MuFoevIXCZzrpXeRmTssj lYSW U jM")
    test(False, "Leetcode is cool")
