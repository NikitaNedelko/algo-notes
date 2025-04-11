"""D. Рюкзак: наибольший вес

Скорость работы: O (N * M)
Затрачено памяти: O (M)
"""


def main():
    """Точка входа в программу"""
    _, M = map(int, input().split())
    golds = list(map(int, input().split()))

    backpack = [0 for _ in range(M + 1)]  # O(M+1) по времени

    for i in golds:  # O(N) по времени
        for j in range(M, i - 1, -1):  # O(M - i) по времени
            backpack[j] = max(backpack[j], backpack[j - i] + i)

    print(backpack[M])


if __name__ == "__main__":
    main()
