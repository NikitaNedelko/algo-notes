"""https://leetcode.com/problems/valid-anagram/"""

from collections import (
    Counter,
)  # обычная мапа которая за один проход считает количество вхождений каждого символа в строке


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        cnt_letters_s = Counter(
            s
        )  # Само создание O (n) по скорости И добавление O(1) как у dict
        cnt_letters_t = Counter(t)

        print(
            f"Counter for s: {cnt_letters_s}"
        )  # ПРИ ВЫВОДЕ СОРТИРУЕТ O( n log(k) ), но если написать print(dict(cnt_letters_s)) то не сортирует
        print(
            f"Counter elements for s: {cnt_letters_s.most_common(2)}"
        )  # Скорость работы O(n log k), где n - длина строки, k - количество уникальных символов

        if cnt_letters_s != cnt_letters_t:
            return False

        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        cnt_letters: dict[str, int] = {}

        for i in s:
            cnt_letters[i] = cnt_letters.get(i, 0) + 1

        for i in t:
            cnt_letters[i] = cnt_letters.get(i, 0) - 1
            if cnt_letters[i] < 0:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("annnnnagram", "nnnnaggaram"))
    # print(solution.isAnagram("rat", "car"))          # False
    # print(solution.isAnagram("listen", "silent"))    # True
    # print(solution.isAnagram("hello", "world"))      # False
    # print(solution.isAnagram("", ""))                 # True
