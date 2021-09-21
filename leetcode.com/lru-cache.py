#!/bin/python3
# https://leetcode.com/problems/lru-cache/

from typing import Union

class Element:
    def __init__(self, key: Union[int, str], value: int, prev=None, next=None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.head: Element = Element("HEAD", None)
        self.tail: Element = Element("TAIL", None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
        self.capacity = capacity
        self.elements: dict[int, Element] = {}

    def get(self, key: int) -> int:
        if key not in self.elements:
            return -1

        element = self.elements[key]

        self.move_node(element)
        return element.value

    def put(self, key: int, value: int) -> None:
        element: Element = None
        if key in self.elements:
            element = self.elements[key]
            element.value = value
            self.move_node(element)
        else:
            self.length += 1
            element = Element(key, value, self.head, self.head.next)
            self.head.next.prev = element
            self.head.next = element

        self.elements[key] = element

        if self.length > self.capacity:
            del self.elements[self.tail.prev.key]
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.length -= 1

    def move_node(self, element: Element) -> None:
        prev_el = element.prev
        next_el = element.next

        prev_el.next = next_el
        next_el.prev = prev_el
        
        element.next = self.head.next
        element.prev = self.head

        self.head.next.prev = element
        self.head.next = element

    def print(self):
        curr = self.head
        while curr:
            print(curr.key, end=" -> ")
            curr = curr.next

        print(" (", end="")
        curr = self.tail
        while curr:
            print(curr.key, end=" -> ")
            curr = curr.prev
        print(")")

cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
val1 = cache.get(4)
val2 = cache.get(3)
val3 = cache.get(2)
val4 = cache.get(1)
cache.put(5, 5)
val5 = cache.get(1)
val6 = cache.get(2)
val7 = cache.get(3)
val8 = cache.get(4)
val9 = cache.get(5)
pass

# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# val1 = cache.get(1)
# cache.put(3, 3)
# val2 = cache.get(2)
# cache.put(4, 4)
# val3 = cache.get(1)
# val4 = cache.get(3)
# val5 = cache.get(4)