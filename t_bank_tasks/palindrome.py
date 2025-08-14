"""
Недавно Кирилл нашел строку из четырех символов. Ему стало интересно, является ли она почти палиндромом. Строка называется почти палиндромом, если из нее можно удалить один символ, чтобы она читалась слева направо также, как и справа налево.
Помогите Кириллу это проверить.

Скорость работы: O(N)
Затрачено памяти: O(N)

тест:
acba = YES
"""

import sys


def isPal(s):
    l = 0
    r = len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        r -= 1  # сократить до одной
        l += 1
    return True


def main():
    s = sys.stdin.readline().strip()

    for id_rm in range(len(s)):
        if isPal(s[:id_rm] + s[id_rm + 1 :]):
            return "YES"

    return "NO"


if __name__ == "__main__":
    print(main())
