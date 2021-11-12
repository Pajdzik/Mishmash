#!/bin/python3
# https://leetcode.com/problems/logger-rate-limiter/

from typing import Deque

class Logger:
    def __init__(self):
        self.queue = Deque()
        self.set = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.queue and self.queue[0][1] + 10 <= timestamp:
            old_message, _ = self.queue.popleft()
            self.set.remove(old_message)

        if message in self.set:
            return False
        else:
            self.queue.append((message, timestamp))
            self.set.add(message)
            return True

if __name__ == "__main__":
    logger = Logger()
    assert(logger.shouldPrintMessage(0, "A"))
    assert(logger.shouldPrintMessage(0, "B"))
    assert(logger.shouldPrintMessage(0, "C"))
    assert(not logger.shouldPrintMessage(0, "A"))
    assert(not logger.shouldPrintMessage(0, "B"))
    assert(not logger.shouldPrintMessage(0, "C"))
    assert(logger.shouldPrintMessage(11, "A"))
    assert(logger.shouldPrintMessage(11, "B"))
    assert(logger.shouldPrintMessage(11, "C"))
    assert(not logger.shouldPrintMessage(11, "A"))

