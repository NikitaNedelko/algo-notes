"""H. Звезды

N максимум равен 128

Скорость работы: O(N^3)
Затрачено памяти: O(N^3)
"""


def main():
    """Точка входа в программу"""
    _ = int(input())

    starts: dict[tuple[int, int, int], int] = dict()  # O(N^3) по памяти

    while True:
        code = list(map(int, input().split()))
        action = code[0]
        if action == 1:
            _, x, y, z, k = code
            starts[(x, y, z)] = starts.get((x, y, z), 0) + k
        if action == 2:
            _, x1, y1, z1, x2, y2, z2 = code
            total = 0
            for (x, y, z), num in starts.items():  # O(N^3) по времени
                if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2:
                    total += num
            print(total)
        if action == 3:
            return


if __name__ == "__main__":
    main()
