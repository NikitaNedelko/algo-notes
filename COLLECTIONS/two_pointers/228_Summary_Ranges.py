"""
https://leetcode.com/problems/summary-ranges/description/
"""


class Solution(object):
    def summaryRanges(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        start = 0

        if not nums:
            return [""]

        answ: list[str] = []

        for id in range(1, len(nums)):
            if nums[id - 1] + 1 != nums[id]:
                if start == id - 1:
                    answ.append(str(nums[start]))
                else:
                    answ.append(str(nums[start]) + "->" + str(nums[id - 1]))
                start = id

        if start == len(nums) - 1:
            answ.append(str(nums[start]))
        else:
            answ.append(str(nums[start]) + "->" + str(nums[-1]))

        return answ


if __name__ == "__main__":
    solution = Solution()
    print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))
