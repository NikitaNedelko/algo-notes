"""C. Интернет

Скорость работы: -
Затрачено памяти: O (31)
"""


def main():
    """Точка входа в программу"""
    M = int(input())

    sec = list(map(int, input().split()))

    ost: int = M
    cost = 0

    while ost != 0:
        max_cpd = -1
        best_time = 0
        best_price = 0
        for i in range(31):
            cur_time = sec[i]
            cur_cpd = cur_time / 2**i
            sec[i] = cur_time if cur_time < ost else ost
            if max_cpd < cur_cpd:
                max_cpd = cur_cpd
                best_time = cur_time
                best_price = 2**i

        count = ost // best_time

        ost -= count * best_time
        cost += best_price * count

    print(cost)


if __name__ == "__main__":
    main()
