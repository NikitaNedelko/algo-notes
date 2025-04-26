"""B. Jedi Ivan's Mission

Скорость работы: O(N^2)
Затрачено памяти: O(N^2)
"""


def main():
    """Точка входа в программу"""

    N = int(input())
    nums = list(map(int, input().split()))

    max_len = max(nums).bit_length()

    # переводим числа в список битов
    bits = [list(bin(x)[2:].zfill(max_len)) for x in nums]

    # считаем сумму единиц по каждой строке
    sum_ones = []
    total_ones = 0

    for i in range(N):
        current_sum = bits[i].count("1")
        total_ones += current_sum
        sum_ones[i] = current_sum

    if total_ones % 2 != 0:
        print("impossible")
        return

    res = bits[0]


if __name__ == "__main__":
    print(*main())

"""
a[0] =  7 → 0111  
a[1] = 10 → 1010  
a[2] = 11 → 1011

N1
a[0] =  7 → 0111  
a[1] = 10 → 1010  
a[2] = 11 → 1011
"""
