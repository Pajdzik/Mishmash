#!/bin/python3
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
from platform import node
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        resultRoot = ListNode(None, None)
        result = resultRoot
        carry = False
        debug = []

        while node1 != None or node2 != None or carry:
            value = 1 if carry else 0

            carry = False
            if node1 and node2:
                value += node1.val + node2.val
            elif node1:
                value += node1.val
            elif node2:
                value += node2.val

            if value > 9:
                carry = True
                value -= 10

            result.next = ListNode(value, None)
            debug.append(value)
            result = result.next

            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next

        return resultRoot.next

l1 = ListNode(9, ListNode(9)) 
l2 = ListNode(9)
Solution().addTwoNumbers(l1, l2)