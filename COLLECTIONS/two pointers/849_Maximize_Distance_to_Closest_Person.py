"""
Найти пустое место (0), где минимальное расстояние до ближайшего занятого (1) — максимально возможное.

Затрачено времени: O(n)
Затрачено памяти: O(1)
"""


class Solution(object):

    def maxDistToClosest(self, seats: list[int]):
        """
        :type seats: List[int]
        :rtype: int
        """

        max_len = 0
        left_index = -1
        right_index = -1

        for index, seat in enumerate(seats):
            if seat == 1:
                right_index = index
                if left_index == -1:
                    max_len = max(max_len, right_index)
                else:
                    max_len = max(max_len, (right_index - left_index) // 2)
                left_index = right_index

        if right_index != len(seats) - 1:
            max_len = max(max_len, len(seats) - 1 - right_index)

        return max_len
