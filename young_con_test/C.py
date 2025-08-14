import sys
import math
from collections import deque

# from itertools import combinations
# from bisect import bisect_left
# from functools import cmp_to_key


def distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    """Возвращает расстояние между двумя точками"""
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def main():
    input = sys.stdin.readline

    N, M, K = map(int, input().split())

    num_of_close = N + M - K
    num_of_open = K

    ans_id = ""

    if N <= num_of_close:
        ans_id += "-1"
        for i in range(num_of_close, M + N):
            ans_id += "\n" + str(i + 1)
        print(ans_id)
        return

    elif M <= num_of_close:
        ans_id += "-1"
        for i in range(M + N - num_of_close):
            ans_id += "\n" + str(i + 1)
        print(ans_id)
        return

    kap: deque[tuple[int, ...]] = deque()
    gop: deque[tuple[int, ...]] = deque()

    for i in range(N):
        kap.append(tuple(map(int, input().split())))

    for i in range(M):
        gop.append(tuple(map(int, input().split())))

    # Определяем основную и второстепенную сеть
    if N >= M:
        main_stores = kap
        close_stores = gop
        base_indices = list(range(1, N + 1))  # индексы основной сети
        other_indices = list(range(N + 1, N + M + 1))  # индексы второй сети
    else:
        main_stores = gop
        close_stores = kap
        base_indices = list(range(N + 1, N + M + 1))
        other_indices = list(range(1, N + 1))

    # Число дополнительных магазинов, которые нужно добрать из другой сети
    need_extra = K - len(main_stores)

    distance: list[tuple[int, int, int]] = []

    for id, point in  


if __name__ == "__main__":
    main()
