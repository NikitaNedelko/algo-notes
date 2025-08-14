"""
Егор с друзьями гуляли по городу N и нашли карту метро. В этом городе целых  веток метро, у каждой ветки свое расписание. Изучив расписание, они обнаружили, что по ветке  поезд начинает ходить в  секунду с начала дня, и каждый новый поезд начинает маршрут после предыдущего спустя  секунд. Теперь им захотелось научиться в некоторые моменты времени для ветки и времени определять, когда они увидят поезд после прихода на станцию.

Скорость работы: O(N)
Затрачено памяти: O(N)

тест:
3
0 1
2 3
1 4
5
1 2
2 6
3 6
2 5
3 8

2
8
9
5
9
"""

import sys


def main():
    n = int(sys.stdin.readline().strip())

    stations: list[tuple[int, int]] = []

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().strip().split())
        stations.append((a, b))

    q = int(sys.stdin.readline().strip())

    ans: list[int] = []

    for _ in range(q):
        t, d = map(int, sys.stdin.readline().strip().split())
        a, b = stations[t - 1]
        ans.append(d + (b - (d - a) % b) % b)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
