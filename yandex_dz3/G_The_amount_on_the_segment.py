"""G. Сумма на отрезке


Скорость работы:
Затрачено памяти:
"""


def main():
    """Точка входа в программу"""
    N, K = map(int, input().split())
    nums = [0] * N

    # расширяем массив до ближайшей степени двойки и выделяем место для дерева
    new_len = 1 << (N - 1).bit_length()
    nums = (new_len - 1) * [0] + nums + [0] * (new_len - N)

    for _ in range(K):  # O(K) по времени
        F, L, R = input().split()
        left = int(L) + new_len - 2
        right = int(R) + new_len - 2

        if F == "A":
            # обновляем элементы дерева
            nums[new_len - 2 + int(L)] = int(R)
            j = new_len - 2 + int(L)
            while j >= 0:  # O(log N) по времени
                if j % 2 == 1:
                    j = (j - 1) // 2
                else:
                    j = (j - 2) // 2
                new_num = nums[j * 2 + 1] + nums[j * 2 + 2]
                if nums[j] == new_num:
                    break
                nums[j] = new_num

            continue

        ans: list[float] = []

        while left <= right:  # O(log N) по времени
            if left % 2 == 0:
                ans.append(nums[left])
                left += 1
            if right % 2 == 1:
                ans.append(nums[right])
                right -= 1
            left -= 1
            left //= 2
            right -= 2
            right //= 2

        print(sum(ans))


if __name__ == "__main__":
    main()
