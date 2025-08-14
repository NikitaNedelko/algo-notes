"""20. Valid Parentheses


Скорость работы: O(N)
Затрачено памяти: O(N/2)
"""


class Solution(object):

    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        stack: list[str] = []  # O(N/2) по памяти

        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for char in s:  # O(N) по времени
            if stack and stack[-1] == char:  # закрывающаяся скобка
                stack.pop()
                continue
            if char in brackets:  # открывающаяся скобка
                stack.append(brackets[char])
                continue
            return False

        return not stack


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid(input()))
