"""F. Рюкзак: наибольшая стоимость с восстановлением ответа

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
        golds[i].append(i + 1)

    backpack = [0 for _ in range(M + 1)]  # O(M+1) по времени
    choice: list[list[int]] = [[] for _ in range(M + 1)]  # O(M+1) по времени

    for weight, price, id in golds:  # O(N) по времени
        for j in range(M, weight - 1, -1):  # O(M - i) по времени
            if backpack[j - weight] + price > backpack[j]:
                backpack[j] = backpack[j - weight] + price
                choice[j] = choice[j - weight] + [id]

    for i in choice[M]:  # O(M) по времени
        print(i)


if __name__ == "__main__":
    main()

"""
4 6
2 4 1 2
7 2 5 1
"""
