"""B. Индекс максимума на отрезке

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
    tree: list[tuple[float, int]] = (  # O(N) по времени
        (new_len - 1) * [(float("-inf"), 0)]
        + [(x, id + 1) for id, x in enumerate(nums)]
        + [(float("-inf"), 0)] * (new_len - N)
    )

    # заполняем узлы дерева
    for i in range(new_len - 2, -1, -1):  # O(N - 1) по времени
        max_num = max(tree[i * 2 + 1][0], tree[i * 2 + 2][0])
        id = 0
        if tree[i * 2 + 1][0] == max_num:
            id = tree[i * 2 + 1][1]
        if tree[i * 2 + 2][0] == max_num:
            id = tree[i * 2 + 2][1]
        tree[i] = (max_num, id)

    for i in range(K):  # O(K) по времени
        L, R = map(int, input().split())
        ans: list[tuple[float, int]] = []
        left = L + new_len - 2
        right = R + new_len - 2

        max_num = float("-inf")

        while left <= right:  # O(log N) по времени
            if left % 2 == 0:
                max_num = max(max_num, tree[left][0])
                ans.append(tree[left])
                if left == right:
                    break
                left += 1
            if right % 2 == 1:
                max_num = max(max_num, tree[right][0])
                ans.append(tree[right])
                right -= 1
            left -= 1
            left //= 2
            right -= 2
            right //= 2

        # считаем количество максимумов
        id_max = 0

        for i in ans:  # O(log N) по времени
            if i[0] == max_num:
                id_max = i[1]
                break

        print(id_max)


if __name__ == "__main__":
    main()

"""
8
3 7 4 5 6 2 9 8
3

9
3 7 4 5 6 2 9 8 0 
3

16
4 7 9 2 1 6 3 9 4 7 1 4 9 9 3 8
1
3 13
"""
