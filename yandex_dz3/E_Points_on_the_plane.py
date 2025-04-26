"""E. Points on the plane

Скорость работы:
Затрачено памяти:
"""


def main():
    """Точка входа в программу"""

    x, y = map(int, input().split())

    print(x ^ y)

    x, c = map(int, input())

    print(x ^ c)


if __name__ == "__main__":
    main()
