#!/bin/python3
# https://leetcode.com/problems/merge-k-sorted-lists/

import math
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            res = ListNode()
            current = res

            while list1 or list2:
                if list1 and list2:
                    if list1.val > list2.val:
                        current.next = list2
                        list2 = list2.next
                    else:
                        current.next = list1
                        list1 = list1.next
                else:
                    if list1:
                        current.next = list1
                        list1 = list1.next
                    else:
                        current.next = list2
                        list2 = list2.next

                current = current.next

            return res.next
         
        if not lists:
            return None

        step = 1
        while step < len(lists):
            for i in range(0, len(lists), step * 2):
                list2 = lists[i + step] if i + step < len(lists) else None
                merged = mergeTwoLists(lists[i], list2)
                lists[i] = merged

            step *= 2

        return lists[0]

    def mergeKLists_bruteforce(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        
        while True:
            min_value, min_i = math.inf, -1

            for i, l in enumerate(lists):
                if not l:
                    continue

                if l.val < min_value:
                    min_value, min_i = l.val, i

            if min_i == -1:
                break

            current.next = lists[min_i]
            current = current.next
            lists[min_i] = lists[min_i].next

        return result.next

