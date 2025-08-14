"""704. Binary Search

Скорость работы: O(N)
Затрачено памяти: O(1)
"""


class Solution(object):

    def maxProfit(self, prices: list[int]):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_num = float("inf")
        max_num = float("-inf")
        max_benefit = 0

        for num in prices:  # O(N) по времени
            if num < min_num:
                benefit = max_num - min_num
                max_benefit = benefit if benefit > max_benefit else max_benefit
                min_num = num
                max_num = num
            if num > max_num:
                max_num = num

        benefit = max_num - min_num
        max_benefit = benefit if benefit > max_benefit else max_benefit

        return max_benefit

        # Это медленнее работает в среднем

        # max_benefit = 0
        # min_price = float("inf")

        # for num in prices:
        #     min_price = num if num < min_price else min_price
        #     benefit = num - min_price
        #     max_benefit = benefit if benefit > max_benefit else max_benefit

        # return max_benefit


if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input().split()))
    print(solution.maxProfit(nums))

"""
7 1 5 3 6 4
2 1 2 0 1
"""
