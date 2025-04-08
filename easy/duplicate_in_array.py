"""Есть ли в массиве дубликат цифры"""

"""
Скорость работы: O(n) 
Затрачено памяти: O(m) 
"""


class Solution:
    def containsDuplicate(self, nums: list[int]):
        seen: set[int] = set()
        for i in nums:  # O(n) по времени
            if i in seen:  # O(1) по времени
                return True
            seen.add(i)  # O(m) по размеру
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate(list(map(int, input().split()))))
