"""704. Binary Search

Скорость работы: O(log N)
Затрачено памяти: O(1)
"""

from typing import List


class Solution(object):

    def search(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1

        while left <= right:  # O(log N) по времени

            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input().split()))
    target = int(input())
    print(solution.search(nums, target))

"""
-1 0 3 5 9 12
9
"""
