"""https://leetcode.com/problems/product-of-array-except-self/"""


class Solution(object):

    def multiply(self, nums: list[int]):
        ans = 1
        for i in nums:
            ans *= i
        return ans

    def productExceptSelf(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size_nums = len(nums)
        answ = [1] * size_nums

        # заполняем с лева на право
        prefix = 1
        for i in range(size_nums):
            answ[i] = prefix
            prefix *= nums[i]

        # заполняем с права на лево
        postfix = 1
        for i in range(size_nums - 1, -1, -1):
            answ[i] *= postfix
            postfix *= nums[i]

        return answ

        #! ОЧЕНЬ МЕДЛЕННО
        # prefix: list[int] = list(nums)
        # postfix: list[int] = []
        # ans: list[int] = []

        # size = len(nums)

        # for _ in range(size):
        #     current_num = prefix.pop(0)
        #     new_num = self.multiply(prefix) * self.multiply(postfix)
        #     print(
        #         f"current_num: {current_num}, prefix: {prefix}, postfix: {postfix}, new_num: {new_num}"
        #     )
        #     ans.append(new_num)
        #     postfix.append(current_num)

        # return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(solution.productExceptSelf([0, 0]))  # [0, 0]
    print(solution.productExceptSelf([1, 2, 3]))  # [6, 3, 2]
