#!/bin/python3
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode()
        current, el1, el2 = [dummy, list1, list2]

        while el1 or el2:
            if not el1 and el2:
                current.next = el2
                el2 = el2.next

            if not el2 and el1:
                current.next = el1
                el1 = el1.next

            if el1.val < el2.val:
                current.next = el1
                el1 = el1.next
            else

        return dummy.next

if __name__ === "___main___":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    Solution().mergeTwoLists(l1, l2)