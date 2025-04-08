"""Даны две строки s и t. Верните true если t является анаграммой (перестановлены местами символы строки t) s, и false в противном случае."""

"""
Скорость работы: O(n) 
Затрачено памяти: O(m), m - количество уникальных символов 
"""


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        cnt_letters: dict[str, int] = {}

        for i in s:  # O(n) по времени
            if i not in cnt_letters:  # O(1) по времени
                cnt_letters[i] = 0  # O(m) по памяти
            cnt_letters[i] += 1

        for i in t:  # O(n) по времени
            if i not in cnt_letters:  # O(1) по времени
                cnt_letters[i] = 0  # O(m) по памяти
            cnt_letters[i] -= 1

        for i in cnt_letters:  # O(n) по времени
            if cnt_letters[i] != 0:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("asdfg", "gfdsa"))
    print(solution.isAnagram("adfg", "gfdsa"))
