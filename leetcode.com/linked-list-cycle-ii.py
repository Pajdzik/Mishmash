#!/bin/python3
# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head.next:
            return None
            
        node = head

        slow = node.next
        fast = slow.next

        while fast:
            if node == slow:
                return node

            if slow == fast:
                node = node.next
                slow = node.next
                fast = slow.next

            slow = slow.next
            fast = fast.next.next if fast.next else None

        node = node.next

        return None

    def detectCycle_cache(self, head: ListNode) -> ListNode:
        cache = set()

        while head:
            if head in cache:
                return head

            cache.add(head)
            head = head.next

        return None

if __name__ == "__main__":
    element4 = ListNode(4)
    element2 = ListNode(2, ListNode(0, element4))
    element4.next = element2
    root = ListNode(3, element2)
    assert(Solution().detectCycle(root) == element2)
