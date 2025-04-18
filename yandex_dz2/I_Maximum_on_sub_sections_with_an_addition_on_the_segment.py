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
        params = input()
        if params[0] == "m":
            F, L, R = params.split()
        else:
            F, L, R, I = params.split()
        left = int(L) + new_len - 2
        right = int(R) + new_len - 2

        # вершины которые покрывают наш отрезок
        peaks: list[list[int]] = []

        while left <= right:  # O(log N) по времени
            if left % 2 == 0:
                peaks.append([int(nums[left]), left])
                left += 1
            if right % 2 == 1:
                peaks.append([int(nums[left]), right])
                right -= 1
            left -= 1
            left //= 2
            right -= 2
            right //= 2

        if F == "a":

            # print(peaks)

            for num, id in peaks:
                next_increment = int(I)
                while id > 0:
                    if next_increment == 0:
                        break
                    if id % 2 == 0:
                        root = nums[(id - 2) // 2]
                        if num != root and nums[id - 1] != root:
                            difference = root - max(num, nums[id - 1])
                            nums[id] += difference
                            nums[id - 1] += difference
                        nums[id] += next_increment
                        next_increment = abs(root - max(nums[id], nums[id - 1]))
                        id = (id - 2) // 2
                        continue
                    else:
                        root = nums[(id - 1) // 2]
                        if num != root and nums[id + 1] != root:
                            difference = root - max(num, nums[id + 1])
                            nums[id] += difference
                            nums[id + 1] += difference
                        nums[id] += next_increment
                        next_increment = abs(root - max(nums[id], nums[id + 1]))
                        id = (id - 1) // 2
                nums[0] += next_increment
            continue

        peek: list[int] = []
        # нахождение максимума
        for num, id in peaks:
            sum = 0
            while id > 0:
                if id % 2 == 0:
                    root = nums[(id - 2) // 2]
                    if num != root and nums[id - 1] != root:
                        sum += abs(root - max(nums[id], nums[id - 1]))
                    id = (id - 2) // 2
                    continue
                else:
                    root = nums[(id - 1) // 2]
                    if num != root and nums[id + 1] != root:
                        sum += abs(root - max(nums[id], nums[id + 1]))
                    id = (id - 1) // 2

            peek.append(int(sum + num))

        ans.append(max(peek))

    print(*ans)


if __name__ == "__main__":
    main()
"""
10
613 263 312 670 216 142 976 355 488 370
3
m 1 3
a 2 10 100
m 4 5
"""
