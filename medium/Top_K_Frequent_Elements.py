"""Top K Frequent Elements"""


class Solution(object):
    def topKFrequent(self, nums: list[int], k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter: dict[int, int] = {}

        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        freq: set[int] = set()
        max_freq = float("-inf")

        for count in counter.values():
            max_freq = max_freq if max_freq > count else count
            freq.add(count)

        frequency: list[list[int]] = [[] for _ in range(int(max_freq) + 1)]

        for num, count in counter.items():
            frequency[count].append(num)

        ans: list[int] = []

        for i in frequency[::-1]:
            if len(i) == 0:
                continue
            for j in i:
                ans.append(j)
                k -= 1
                if k == 0:
                    return ans


if __name__ == "__main__":
    solution = Solution()
    arr = list(map(int, input().split()))
    k = int(input())
    print(solution.topKFrequent(arr, k))

"""
1 1 1 2 2 3
"""
