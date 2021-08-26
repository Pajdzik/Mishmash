#!/bin/python3
# https://leetcode.com/problems/rotate-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        if k == 0 or head.next is None:
            return head

        curr = head
        length = 1

        while curr.next:
            length += 1
            curr = curr.next

        tail = curr
        
        if k % length == 0:
            return head
        if k > length:
            k = k % length
        n = length - k

        curr = head
        while curr and n > 1:
            curr = curr.next
            n -= 1

        new_head = curr.next
        tail.next = head
        curr.next = None

        return new_head

Solution().rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 10)