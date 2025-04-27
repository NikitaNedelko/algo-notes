"""356. Line Reflection

Условие:
Дано множество точек на плоскости. Нужно определить, существует ли вертикальная прямая x = k, относительно которой всё множество симметрично.

Входные данные:

Массив points, где каждая точка представлена как список из двух целых чисел [x, y].

Размер массива до 10⁴ точек.

Координаты точек по модулю не превышают 10⁴.

Выходные данные:

Вернуть True, если существует такая прямая симметрии.

Вернуть False, если не существует.


Скорость работы: O(2*N)
Затрачено памяти: O(N)
"""


def main(cords: list[list[int]]):
    """Точка входа в программу"""

    cords_set: set[tuple[int, int]] = set()  # O(N) по памяти

    min_x = float("inf")
    max_x = float("-inf")

    for x, y in cords:  # O(N) по времени
        max_x = x if x > max_x else max_x
        min_x = x if x < min_x else min_x
        cords_set.add((x, y))

    middle_x = (max_x + min_x) / 2

    for x, y in cords_set:  # O(N) по времени
        opposite_x = middle_x - x + middle_x
        opposite_y = y
        if (opposite_x, opposite_y) not in cords_set:
            return False

    return True


if __name__ == "__main__":
    print(main([[1, 1], [3, 1], [2, 1]]))
