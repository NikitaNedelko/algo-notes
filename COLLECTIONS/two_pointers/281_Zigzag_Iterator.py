"""
https://leetcode.ca/2016-09-06-281-Zigzag-Iterator/
"""

from collections import deque


class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
        self.dq: deque[tuple[list[int], int]] = deque()
        if v1:
            self.dq.append((v1, 0))
        if v2:
            self.dq.append((v2, 0))

    def next(self) -> int:
        arr, id = self.dq.popleft()
        num = arr[id]
        id += 1
        if id < len(arr):
            self.dq.append((arr, id))
        return num

    def hasNext(self) -> bool:
        return len(self.dq) > 0
