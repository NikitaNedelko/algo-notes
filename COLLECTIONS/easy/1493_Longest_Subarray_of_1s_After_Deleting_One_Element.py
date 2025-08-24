class Solution(object):
    def longestSubarray(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev_count = 0
        cur_count = 0

        max_len = 0

        flag = 0

        for num in nums:
            cur_count += 1
            if num == 0:
                flag = 1
                cur_count -= 1
                max_len = (
                    max_len
                    if max_len > prev_count + cur_count
                    else prev_count + cur_count
                )
                prev_count = cur_count
                cur_count = 0

        if cur_count != 0:
            cur_count -= 0 if flag else 1
            max_len = (
                max_len if max_len > prev_count + cur_count else prev_count + cur_count
            )

        return max_len


if __name__ == "__main__":
    cl = Solution()
    print(cl.longestSubarray([1, 1, 0, 1]))  # 3
    print(cl.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
    print(cl.longestSubarray([1, 1, 1]))  # 2
    print(cl.longestSubarray([0, 0, 0]))  # 0
