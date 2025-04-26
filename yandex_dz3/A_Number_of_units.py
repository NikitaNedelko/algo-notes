"""A. Количество единиц

Скорость работы:
Затрачено памяти:
"""


def main() -> int:
    """Точка входа в программу"""

    return bin(int(input())).count("1")


if __name__ == "__main__":
    print(main())
