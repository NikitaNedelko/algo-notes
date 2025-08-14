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

        len_nums = len(seats)

        for index, seat in enumerate(seats):
            if seat == 1:
                right_index = index
                if left_index == -1:
                    max_len = max_len if max_len > right_index else right_index
                else:
                    current_len = (right_index - left_index) // 2
                    max_len = max_len if max_len > current_len else current_len
                left_index = right_index

        if right_index != len_nums - 1:
            current_len = len_nums - 1 - right_index
            max_len = max_len if max_len > current_len else current_len

        return max_len
