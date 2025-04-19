"""F. Ближайшее большее число справа


Скорость работы: O(K log ^ 2 N)
Затрачено памяти: O(2*N - 1)
"""


def main():
    """Точка входа в программу"""
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    # расширяем массив до ближайшей степени двойки и выделяем место для дерева
    new_len = 1 << (N - 1).bit_length()
    nums = (new_len - 1) * [0] + nums + [float("-inf")] * (new_len - N)

    # заполняем узлы дерева
    for i in range(new_len - 2, -1, -1):  # O(N) по времени
        nums[i] = max(nums[i * 2 + 1], nums[i * 2 + 2])

    for i in range(K):  # O(K) по времени
        F, I, X = map(int, input().split())

        if F == 0:
            # обновляем элементы дерева
            nums[new_len - 2 + I] = X
            i = new_len - 2 + I
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

        units_left: list[list[int]] = []
        units_right: list[list[int]] = []

        left = I + new_len - 2
        right = new_len * 2 - 2

        while left <= right:  # O(log N) по времени
            if left % 2 == 0:
                units_left.append(
                    [left, int(nums[left] if nums[left] != float("-inf") else -1)]
                )
                left += 1
            if right % 2 == 1:
                units_right.append(
                    [right, int(nums[right] if nums[right] != float("-inf") else -1)]
                )
                right -= 1
            left -= 1
            left //= 2
            right -= 2
            right //= 2

        found = False

        for i in units_left + units_right[::-1]:  # O(log N) по времени
            if X - i[1] <= 0:
                id = i[0]
                while True:  # O(log N) по времени
                    if id * 2 + 2 > len(nums):
                        print(id - new_len + 2)
                        found = True
                        break
                    left = nums[id * 2 + 1]
                    right = nums[id * 2 + 2]
                    if X - left <= 0:
                        id = id * 2 + 1
                    else:
                        id = id * 2 + 2
                if found:
                    break

        if not found:
            print(-1)


if __name__ == "__main__":
    main()
