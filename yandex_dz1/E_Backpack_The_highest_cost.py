"""E. Рюкзак: наибольшая стоимость

Скорость работы: O (N * M)
Затрачено памяти: O (M)
"""


def main():
    """Точка входа в программу"""
    _, M = map(int, input().split())
    weight = list(map(int, input().split()))
    price = list(map(int, input().split()))

    golds: list[list[int]] = [[] for _ in range(len(weight))]
    for i in range(len(weight)):  # O(N) по времени
        golds[i].append(weight[i])
        golds[i].append(price[i])

    backpack = [0 for _ in range(M + 1)]  # O(M+1) по времени

    for weight, price in golds:  # O(N) по времени
        for j in range(M, weight - 1, -1):  # O(M - i) по времени
            backpack[j] = max(backpack[j], backpack[j - weight] + price)

    print(backpack[M])


if __name__ == "__main__":
    main()
