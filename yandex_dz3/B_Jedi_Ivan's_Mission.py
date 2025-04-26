"""B. Jedi Ivan's Mission

Скорость работы: O(N^2)
Затрачено памяти: O(N^2)
"""


def main() -> list[int]:
    """Точка входа в программу"""

    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]  # O(N^2) по памяти

    ans = [0] * N  # O(N) по памяти

    for i in range(N):  # O(N) по времени
        for j in range(N):  # O(N) по времени
            if i != j:
                ans[i] |= nums[i][j]

    return ans


if __name__ == "__main__":
    print(*main())
