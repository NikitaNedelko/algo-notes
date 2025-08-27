"""125. Valid Palindrome


Скорость работы: O(N/2)
Затрачено памяти: O(N)
"""


class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # ! самый быстрый способ

        # заменить все, кроме 0-9A-Za-z, на ""
        # + это более одного символа

        # t = re.sub(r"[^0-9A-Za-z]+", "", s).lower()
        # return t == t[::-1]

        if not s:
            return False

        s = s.lower()

        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(input()))
