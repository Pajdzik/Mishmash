#!/bin/python3
# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
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