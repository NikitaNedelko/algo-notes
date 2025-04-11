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

        numDic = {}  # O(n) по памяти

        n = len(nums)

        for first_id in range(n):  # O(n) по времени
            second = target - nums[first_id]
            if second in numDic:  # O(1) по времени
                return [first_id, numDic[second]]
            numDic[nums[first_id]] = first_id  # O(1) по времени

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([2, 3, 4], 6))
