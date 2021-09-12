#!/bin/python3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def has_duplicates(self, s: str, left: int, right: int) -> bool:
        chars = set()
        for i in range(left, right + 1):
            if s[i] in chars:
                return True
            
            chars.add(s[i])
        
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = max_length = 0
        indexes = {}

        while right < len(s):
            c = s[right]
            
            if c in indexes:
                new_left = indexes[c] + 1
                for i in range(left, new_left):
                    del indexes[s[i]]
                left = new_left
                indexes[c] = right
            else:
                indexes[c] = right

            max_length = max(max_length, right - left + 1)
            right += 1
            
        return max_length

    def lengthOfLongestSubstring_bf(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            chars = set([ s[i] ])
            length = 1
            for j in range(i + 1, len(s)):
                if s[j] not in chars:
                    length += 1
                    chars.add(s[j])
                else:
                    break
            
            if length > max_length:
                max_length = length

        return max_length


Solution().lengthOfLongestSubstring("abcabcbb")
