#!/bin/python3
# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = None
        next = head

        while next:
            next_node = next.next
            next.next = current

            current = next
            next = next_node

        return current

Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
