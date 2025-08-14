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

        i = 0
        j = len(s) - 1

        while i < j:  # O(N/2) по времени
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(input()))
