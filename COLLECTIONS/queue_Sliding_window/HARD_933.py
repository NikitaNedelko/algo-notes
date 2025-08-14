"""
Реализуй класс RecentUserCounter, который отслеживает события ping(t, user_id), и сохраняет только те события, которые произошли за последние k миллисекунд (скользящее окно).

Метод get_active_users(x) должен возвращать список user_id, у которых было более x вызовов ping за последние k миллисекунд.


Затрачено времени:
затрачено памяти:
"""

from collections import deque


class RecentUserCounter(object):
    def __init__(self, t: int):
        """
        t - интервал времени после которого удаляем все вызовы
        """
        self.t = t
        self.queue: deque[list[int]] = deque()  # last all calls
        self.dict: dict[int, int] = {}  # user_id -> num of calls

    def ping(self, user_id: int, t: int):
        self.dict[user_id] = self.dict.get(user_id, 0) + 1

        while self.queue[0][1] < (t - self.t):
            current_user_id = self.queue[0][0]
            self.dict[current_user_id] -= 1
            self.queue.popleft()

        self.queue.append([user_id, t])

    def get_active_users(self, x: int):
        ans: list[int] = []
        for user_id, _ in self.dict.items():
            if self.dict[user_id] >= x:
                ans.append(user_id)

        return [user_id for user_id, _ in self.dict.items() if self.dict[user_id] >= x]
