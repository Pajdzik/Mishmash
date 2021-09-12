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

        while right < len(s):
            if self.has_duplicates(s, left, right):
                max_length = max(max_length, right - left)
                left += 1
            else:
                right += 1
                    
        return max(max_length, right - left)

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


Solution().lengthOfLongestSubstring(" ")
