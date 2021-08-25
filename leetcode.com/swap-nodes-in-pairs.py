#!/bin/python3
# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        return_head = head.next

        previous = head
        current = head.next

        while current:
            next = current.next
            current.next = previous
            previous.next = next.next if next and next.next else next

            previous = next
            current = next.next if next else None

        return return_head

Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3))))