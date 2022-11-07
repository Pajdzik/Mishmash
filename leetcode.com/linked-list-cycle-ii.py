#!/bin/python3
# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if fast == slow:
                break

        if not fast or not fast.next:
            return None

        node = head
        while node != fast:
            node = node.next
            fast = fast.next

        return node

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
