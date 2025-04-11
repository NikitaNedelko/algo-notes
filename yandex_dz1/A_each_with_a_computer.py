"""A. Каждому по компьютеру

Скорость работы: O(N log N)
Затрачено памяти: O(N + M)
"""


def main():
    """Точка входа в программу"""
    N, _ = map(int, input().split())  # O(1) по времени

    groups = list(
        sorted(
            [(id + 1, number) for id, number in enumerate(map(int, input().split()))],
            key=lambda x: x[1],
            reverse=True,
        )
    )  # O(N log N) по времени
    audiences = list(
        sorted(
            [(id + 1, number) for id, number in enumerate(map(int, input().split()))],
            key=lambda x: x[1],
            reverse=True,
        )
    )  # O(M log M) по времени

    # Ввод = O(N log N + M log M)

    ans = [0 for _ in range(N)]  # O(N) по времени
    ans_count = 0

    last_group_id = 0

    for id_a, y in audiences:  # O(M) по времени
        for i in range(last_group_id, N):  # O(N) по времени
            id_g, x = groups[i]
            if y > x:
                ans_count += 1
                ans[id_g - 1] = id_a
                last_group_id = i + 1
                break
            last_group_id = i

    # Обработка O(M + N)

    print(ans_count)
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
