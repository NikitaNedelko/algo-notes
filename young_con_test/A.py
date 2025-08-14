"""A. Электросамокаты

Скорость работы: O(N)
Затрачено памяти: O(N)
"""

import sys


def main():
    """Точка входа в программу"""

    input = sys.stdin.readline

    N = int(input())
    input_speeds: list[int] = list(map(int, input().split()))  # O(N) по памяти

    sum_speeds = 0
    min_speed = float("inf")

    for id_house in range(N - 1):  # O(N) по времени
        speed = input_speeds[id_house]
        min_speed = speed if speed < min_speed else min_speed
        sum_speeds += int(min_speed)

    print(sum_speeds)


if __name__ == "__main__":
    main()

"""
10
9 10 7 6 7 5 6 7 3 2



"""
