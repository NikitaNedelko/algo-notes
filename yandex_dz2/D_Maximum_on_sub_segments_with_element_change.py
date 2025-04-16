"""D. Максимум на подотрезках с изменением элемента


Скорость работы: O(K log N)
Затрачено памяти: O(2*N - 1)
"""


def main():
    """Точка входа в программу"""
    N = int(input())
    nums = list(map(int, input().split()))
    K = int(input())

    # расширяем массив до ближайшей степени двойки и выделяем место для дерева
    new_len = 1 << (N - 1).bit_length()
    nums = (new_len - 1) * [0] + nums + [float("-inf")] * (new_len - N)

    # заполняем узлы дерева
    for i in range(new_len - 2, -1, -1):
        nums[i] = max(nums[i * 2 + 1], nums[i * 2 + 2])

    ans: list[float] = []

    for i in range(K):  # O(K) по времени
        F, L, R = input().split()
        left = int(L) + new_len - 2
        right = int(R) + new_len - 2

        if F == "u":
            # обновляем элементы дерева
            nums[new_len - 2 + int(L)] = int(R)
            i = new_len - 2 + int(L)
            while i != 0:  # O(log N) по времени
                if i % 2 == 1:
                    i = (i - 1) // 2
                else:
                    i = (i - 2) // 2
                new_max = max(nums[i * 2 + 1], nums[i * 2 + 2])
                if nums[i] == new_max:
                    break
                nums[i] = new_max

            continue

        max_num = float("-inf")

        while left <= right:  # O(log N) по времени
            if left % 2 == 0:
                max_num = max(max_num, nums[left])
                left += 1
            if right % 2 == 1:
                max_num = max(max_num, nums[right])
                right -= 1
            left -= 1
            left //= 2
            right -= 2
            right //= 2

        ans.append(max_num)

    print(*ans)


if __name__ == "__main__":
    main()
"""
10
613 263 312 670 216 142 976 355 488 370
4
s 2 7
s 4 8
u 7 969
s 2 7
"""
