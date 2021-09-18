#!/bin/python3
# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def get_length(self, head: ListNode) -> int:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        length_a = self.get_length(headA)
        length_b = self.get_length(headB)

        diff = 0
        fast, slow = None, None
        if length_a > length_b:
            diff = length_a - length_b
            fast, slow = headA, headB
        else:
            diff = length_b - length_a
            fast, slow = headB, headA

        while diff > 0:
            fast = fast.next
            diff -= 1

        while fast and slow:
            if slow == fast:
                return fast
            fast = fast.next
            slow = slow.next

        return None

    def getIntersectionNode_cache(self, headA: ListNode, headB: ListNode) -> ListNode:
        cache = set()

        while headA or headB:
            if headA:
                if headA:
                    if headA in cache:
                        return headA
                    else:
                        cache.add(headA)
                        headA = headA.next
            
            if headB:
                if headB:
                    if headB in cache:
                        return headB
                    else:
                        cache.add(headB)
                        headB = headB.next

        return None

tail = ListNode(8, ListNode(4, ListNode(5)))
root_a = ListNode(4, ListNode(1, tail))
root_b = ListNode(5, ListNode(6, ListNode(1, tail)))

Solution().getIntersectionNode(root_a, root_b)