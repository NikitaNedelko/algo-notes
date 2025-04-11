"""B. Ни больше ни меньше

Скорость работы: # O(N * T) по времени
Затрачено памяти: # O(N) по времени
"""


def main(N: int, nums: list[int]):
    """Находит минимальной количество отрезков"""
    ans: list[int] = []
    current_len = 0
    min_num = N + 1
    for current in nums:  # O(N) по времени
        if current < current_len + 1 or min_num < current_len + 1:
            min_num = N + 1
            ans.append(current_len)
            current_len = 0
        current_len += 1
        min_num = min_num if min_num < current else current

    ans.append(current_len)

    print(len(ans))
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):  # O(T) по времени
        N = int(input())
        nums = list(map(int, input().split()))
        main(N, nums)  # O(N + N) по времени
