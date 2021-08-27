#!/bin/python3
# https://leetcode.com/problems/palindrome-linked-list/

import re
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def __init__(self) -> None:
        self.front_node = None

    def check(self, back_node: Optional[ListNode]):
        if back_node == None:
            return True
        else:
            if self.check(back_node.next) == False:
                return False
            else:
                equal = self.front_node.val == back_node.val
                self.front_node = self.front_node.next
                return equal

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_node = head
        return self.check(head)

result = Solution().isPalindrome(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))
print(result)