"""E. K-й ноль


Скорость работы: O(K log ^ 2 N)
Затрачено памяти: O(2*N - 1)
"""


def main():
    """Точка входа в программу"""
    N = int(input())
    nums = list(map(int, input().split()))
    K = int(input())

    # расширяем массив до ближайшей степени двойки и выделяем место для дерева
    new_len = 1 << (N - 1).bit_length()
    nums = (
        (new_len - 1) * [0] + [1 if i == 0 else 0 for i in nums] + [0] * (new_len - N)
    )

    # заполняем узлы дерева
    for i in range(new_len - 2, -1, -1):  # O(N) по времени
        nums[i] = nums[i * 2 + 1] + nums[i * 2 + 2]

    ans: list[int] = []

    for i in range(K):  # O(K) по времени
        params = input()
        if params[0] == "u":
            f, l, r = params.split()
            k = 0
        else:
            f, l, r, k = params.split()
            k = int(k)
        L = int(l)
        R = int(r)
        F = f
        left = int(L) + new_len - 2
        right = int(R) + new_len - 2

        if F == "u":
            # обновляем элементы дерева
            nums[new_len - 2 + int(L)] = 0 if int(R) != 0 else 1
            i = new_len - 2 + int(L)
            while i != 0:  # O(log N) по времени
                if i % 2 == 1:
                    i = (i - 1) // 2
                else:
                    i = (i - 2) // 2
                new_count = nums[i * 2 + 1] + nums[i * 2 + 2]
                if nums[i] == new_count:
                    break
                nums[i] = new_count

            continue

        units_left: list[list[int]] = []
        units_right: list[list[int]] = []

        while left <= right:  # O(log N) по времени
            if left % 2 == 0:
                units_left.append([left, int(nums[left]), 0])
                left += 1
            if right % 2 == 1:
                units_right.append([right, int(nums[right]), 1])
                right -= 1
            left -= 1
            left //= 2
            right -= 2
            right //= 2

        for i in units_left + units_right[::-1]:  # O(log N) по времени
            if k - i[1] <= 0:
                id = i[0]
                while k != 0:  # O(log N) по времени
                    if id * 2 + 2 > len(nums):
                        ans.append(id - new_len + 2)
                        break
                    left = nums[id * 2 + 1]
                    right = nums[id * 2 + 2]
                    if k - left <= 0:
                        id = id * 2 + 1
                    else:
                        k -= left
                        id = id * 2 + 2
            k -= i[1]
            if k <= 0:
                break

        if k > 0:
            ans.append(-1)
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
