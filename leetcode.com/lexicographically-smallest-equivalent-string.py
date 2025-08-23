#!/bin/python3
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        alphabet = {}

        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]

            l1 = alphabet[c1] if c1 in alphabet else set(c2)
            l2 = alphabet[c2] if c2 in alphabet else set(c1)

            l12 = l1.union(l2).union(set([c1, c2]))
            for c in l12:
                alphabet[c] = l12

        alphabet_with_sorted_letters = {}
        for l, ls in alphabet.items():
            alphabet_with_sorted_letters[l] = sorted(ls)[0]

        result = [
            (
                alphabet_with_sorted_letters[c]
                if c in alphabet_with_sorted_letters
                else c
            )
            for c in baseStr
        ]
        return "".join(result)


if __name__ == "__main__":
    Solution().smallestEquivalentString("parker", "morris", "parser")
