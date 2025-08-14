"""
Используется очередь (FIFO) для хранения только тех запросов, которые попадают в окно [t - 3000, t].

Шаги:
На каждый вызов ping(t) добавляешь t в конец очереди.

Удаляешь из начала очереди все значения < t - 3000.

Возвращаешь длину очереди — это и есть количество активных запросов за последние 3000 мс.

Затрачено времени: O(1)
затрачено памяти: O(1)
"""

from collections import deque


class RecentCounter(object):
    def __init__(self):
        self.queue: deque[int] = deque()

    def ping(self, t: int):
        self.queue.append(t)
        while self.queue[0] < (t - 3000):
            self.queue.popleft()

        return len(self.queue)
