"""D. Распределенное хранение

Скорость работы: O(N - 1)
Затрачено памяти: O(N)
"""

import sys
from collections import deque


# def main():
#     """Точка входа в программу"""

#     input = sys.stdin.readline

#     N = int(input())
#     nums = deque(map(int, input().split()))  # O(N) по памяти

#     max_len = 1
#     current_len = 1

#     for id, num in enumerate(nums):  # O(N - 1) по времени
#         if id + 1 == N:
#             break
#         if num >= nums[id + 1]:
#             current_len += 1
#         else:
#             max_len = current_len if current_len > max_len else max_len
#             break

#     print(max_len if max_len > N - max_len else N - max_len)


# if __name__ == "__main__":
#     main()

"""D. Распределенное хранение

Скорость работы: O(3N)
Затрачено памяти: O(3N)
"""


def main():
    """Точка входа в программу"""

    input = sys.stdin.readline

    N = int(input())
    nums = list(map(int, input().split()))  # O(N) по памяти

    prefix_min = [nums[0]] + [0] * (N - 1)  # O(N) по памяти
    postfix_max = [0] * (N - 1) + [nums[-1]]  # O(N) по памяти

    len = 0
    max_len = 0

    for id in range(1, N):  # O(N) по времени
        prefix_min[id] = min(prefix_min[id - 1], nums[id])

    for id in range(N - 2, -1, -1):  # O(N) по времени
        postfix_max[id] = max(postfix_max[id + 1], nums[id])

    del nums

    for mx, mn in zip(postfix_max, prefix_min):  # O(N) по времени
        if mn >= mx:
            max_len = len
        len += 1

    print(max_len)


if __name__ == "__main__":
    main()

"""
ОТВЕТ не может равняться N

Входные данные:
3
2 5 1
Ожидаемый результат:
2

Входные данные:
4
3 3 2 1
Ожидаемый результат:
3

Входные данные:
5
7 5 5 3 1
Ожидаемый результат:
4

Входные данные:
6
10 9 8 8 7 5
Ожидаемый результат:
5

Входные данные:
4
1 1 2 2
Ожидаемый результат:
2

Входные данные:
3
1 3 2
Ожидаемый результат:
2
"""
