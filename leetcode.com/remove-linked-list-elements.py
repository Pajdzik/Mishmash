#!/bin/python3
# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev = dummy
        curr = head

        while curr:
            while curr and curr.val == val:
                curr = curr.next

            prev.next = curr
            prev, curr = curr, (curr.next if curr else None)

        return dummy.next