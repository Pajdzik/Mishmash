#!/bin/python3
# https://leetcode.com/problems/circular-sentence


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
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
    test(False, "Leetcode is cool")
