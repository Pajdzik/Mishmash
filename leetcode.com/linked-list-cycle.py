#!/bin/python3
# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while True:
            if fast == None or fast.next == None:
                return False

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True