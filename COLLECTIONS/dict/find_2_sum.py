"""Необходимо найти 2 числа из массива, сумма которых будет равна target


Скорость работы: O(n)
Затрачено памяти: O(n)
"""


class Solution(object):

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        is_seen: dict[int, int] = {}

        for id_first, num_first in enumerate(nums):
            second = target - num_first
            if second in is_seen:  # O(1) по времени,НО O(n) если in is_seen.items()
                return [is_seen[second], id_first]
            is_seen[num_first] = id_first

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([2, 3, 4], 6))
