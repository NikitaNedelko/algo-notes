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

    set_cords = set(map(tuple, cords))

    min_x = min(x for x, _ in set_cords)
    max_x = max(x for x, _ in set_cords)

    middle_x = min_x + max_x

    for x, y in cords:
        opposite_x = middle_x - x
        if (opposite_x, y) not in set_cords:
            return False

    return True


if __name__ == "__main__":
    print(main([[1, 1], [3, 1], [2, 1]]))
