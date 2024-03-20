#!/bin/python3
# https://leetcode.com/problems/merge-in-between-linked-lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start_node = list1
        length = b - a + 1
        while start_node and a > 1:
            start_node = start_node.next
            a -= 1

        end_node = start_node
        while end_node and length >= 0:
            end_node = end_node.next
            length -= 1

        start_node.next = list2
        while start_node.next:
            start_node = start_node.next

        start_node.next = end_node

        return list1


def print_list(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    def get_list_node(values: list[int]) -> ListNode:
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def test(expected: ListNode, list1: ListNode, a: int, b: int, list2: ListNode):
        result = Solution().mergeInBetween(list1, a, b, list2)
        while expected:
            assert result.val == expected.val, f"Expected: {
                expected.val}, but got: {result.val}"
            expected = expected.next
            result = result.next

    test(get_list_node([10, 1, 13, 1000000, 1000001, 1000002, 5]), get_list_node(
        [10, 1, 13, 6, 9, 5]), 3, 4, get_list_node([1000000, 1000001, 1000002]))
