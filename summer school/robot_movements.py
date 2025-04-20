"""
Дан список перемещений робота — каждое перемещение: откуда и куда он поехал.

Задача: определить начальный адрес (где началась доставка) и конечный адрес (где робот закончил свой путь).
"""


def main():
    """Точка входа в программу."""
    n = int(input())  # количество перемещений
    num_of_visits: dict[str, int] = {}

    for _ in range(n):
        street1, num1, street2, num2 = input().split()
        street1 = street1 + " " + num1
        street2 = street2 + " " + num2
        num_of_visits[street1] = num_of_visits.get(street1, 0) - 1
        num_of_visits[street2] = num_of_visits.get(street2, 0) + 1

    start = None
    num_call = 0
    end = None
    for street, num in num_of_visits.items():
        if num == -1:
            num_call += 1
            start = street
        elif num == 1:
            num_call += 1
            end = street
        if num_call >= 3:
            print(-1)
            return
    if start is None or end is None:
        print(-1)
        return

    print(start, end)


if __name__ == "__main__":
    main()
