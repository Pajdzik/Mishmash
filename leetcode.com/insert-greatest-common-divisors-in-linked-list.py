#!/bin/python3
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

from functools import cache
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        @cache
        def find_gcd(a, b):
            if b == 0:
                return a
            return find_gcd(b, a % b)

        curr = head

        while curr.next:
            next = curr.next
            gcd = find_gcd(curr.val, curr.next.val)
            curr.next = ListNode(gcd, next)
            curr = next

        return head
