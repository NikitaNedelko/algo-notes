"""
по скорости: O(n)
по памяти: O(n)
"""

import sys

input = sys.stdin.readline
write = sys.stdout.write


def main():
    n = int(input())
    l = [0] * (n + 1)  # O(n)
    r = [0] * (n + 1)  # O(n)
    a = [0] * (n + 1)  # O(n)

    for i in range(1, n + 1):  # O(n)
        li, ri, ai = map(int, input().split())
        l[i] = li
        r[i] = ri
        a[i] = ai

    A = [0] * (n + 1)  # O(n)
    for i in range(1, n + 1):  # O(n)
        A[i] = A[i - 1] + a[i]

    INF = float("inf")
    ML = [INF] * (n + 1)  # O(n)
    for s in range(2, n + 1):  # O(n)
        ML[s] = ML[s - 1] if ML[s - 1] < (l[s] - A[s - 1]) else (l[s] - A[s - 1])

    MR = [INF] * (n + 2)  # O(n)
    for s in range(n - 1, 0, -1):  # O(n)
        cap_tail_from_s = r[s] - (A[n] - A[s])
        MR[s] = MR[s + 1] if MR[s + 1] < cap_tail_from_s else cap_tail_from_s

    ans = 0
    totalA = A[n]
    for s in range(1, n + 1):  # O(n)
        left_gain = A[s - 1] + (ML[s] if ML[s] < 0 else 0)
        right_gain = (totalA - A[s]) + (MR[s] if MR[s] < 0 else 0)
        total = a[s] + left_gain + right_gain
        if total > ans:
            ans = total

    write(str(ans) + "\n")


if __name__ == "__main__":
    main()
