#!/bin/python3
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1

        root = ListNode(None)
        node = root

        while l1 or l2:
            if l1 and ((l1 and not l2) or (l1.val < l2.val)):
                node.next = l1
                l1 = l1.next
            elif l2:
                node.next = l2
                l2 = l2.next

            node = node.next

        return root.next

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        
        while l1 or l2:
            if (l1 and l2 and l1.val <= l2.val) or (l1 and not l2):
                node.next = l1
                l1 = l1.next
            elif l2:
                node.next = l2
                l2 = l2.next
                
            node = node.next
                
        return dummy.next

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

Solution().mergeTwoLists(l1, l2)