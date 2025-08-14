from collections import Counter
from heapq import nlargest


class Solution(object):
    def topKFrequent(self, nums: list[int], k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #! Самое быстрое решение
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        return [num for num, _ in nlargest(k, count.items(), key=lambda x: x[1])]


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(solution.topKFrequent([1], 1))  # [1]
    print(solution.topKFrequent([4, 4, 4, 5, 5, 6], 2))  # [4, 5]
