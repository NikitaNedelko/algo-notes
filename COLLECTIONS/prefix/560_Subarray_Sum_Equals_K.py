class Solution(object):

    def subarraySum(self, nums: list[int], k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        current_prefix = 0
        last_prefix: dict[int, int] = {0: 1}  # префикс -> частота
        # ! ОБЯЗАТЕЛЬНО учесть {0:1}

        for num in nums:
            current_prefix += num
            prev_prefix = current_prefix - k
            count += last_prefix.get(prev_prefix, 0)
            last_prefix[current_prefix] = last_prefix.get(current_prefix, 0) + 1

        return count


if __name__ == "__main__":
    cl = Solution()
    print(cl.subarraySum([1], 0))
