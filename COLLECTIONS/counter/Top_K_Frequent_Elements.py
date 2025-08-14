from collections import Counter


class Solution(object):
    def topKFrequent(self, nums: list[int], k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        return dict(Counter(nums).most_common(k)).keys()
        # O(n log k), где n - длина массива, k - количество уникальных элементов

    def topKFrequent2(self, nums: list[int], k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count: dict[int, int] = {}
        heap: list[list[int]] = []  # самые частотные

        for num in nums:  # O(n) по времени
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            # O(m) по времени, где m - количество уникальных элементов
            if len(heap) < k:
                heap.append([freq, num])
                if len(heap) == k:
                    heap.sort(key=lambda x: x[0])
            else:
                if freq > heap[0][0]:
                    heap[0] = [freq, num]
                    heap.sort(key=lambda x: x[0])  # O(k log k) по времени

        return [num for _, num in heap]


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(solution.topKFrequent([1], 1))  # [1]
    print(solution.topKFrequent([4, 4, 4, 5, 5, 6], 2))  # [4, 5]
