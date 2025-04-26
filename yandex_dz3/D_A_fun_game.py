"""D. Забавная игра

N - длинна двоичной записи числа

Скорость работы: O(2*N)
Затрачено памяти: O(N)
"""


def main():
    """Точка входа в программу"""

    num = bin(int(input()))[2:]  # O(N) по памяти

    max_len = 0
    max_id = 0

    current_len = 0
    current_id = 0

    for id, bit in enumerate(num + num):  # O(2*N) по времени
        if bit == "1":
            if current_len == 0:
                current_id = id
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_id = current_id
            current_id = 0
            current_len = 0

    print(int(num[max_id:] + num[:max_id], 2))


if __name__ == "__main__":
    main()

"""
МОЖНО ЕЩЕ оптимизировать память: не создавать num + num, а работать с num[i % N]
"""
