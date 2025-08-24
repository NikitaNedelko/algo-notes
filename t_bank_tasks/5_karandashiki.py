"""
по скорости: O(n^2 log n)
по памяти: O(n)
"""

import sys

input = sys.stdin.readline
write = sys.stdout.write

MOD = 1_000_000_007


def main():
    """точка входа в программу"""
    n, k = map(int, input().split())

    inv = [0] * (n + 1)  # O(n)
    inv[1] = 1
    for t in range(2, n + 1):  # O(n)
        inv[t] = MOD - (MOD // t) * inv[MOD % t] % MOD
    # Итог O(n) по времени и памяти

    # число способов получить сумму s
    dp = [0] * (n + 1)  # O(n)
    dp[0] = 1

    for v in range(1, n + 1):
        ndp = dp[:]  # O(n)
        max_t = n // v

        for s in range(n + 1):  # O(n)
            base = dp[s]
            if base == 0:
                continue

            ways = k % MOD
            jump = v
            t = 1
            while t <= max_t and s + jump <= n:  # O(n/v)
                ndp[s + jump] = (ndp[s + jump] + base * ways) % MOD
                t += 1
                jump += v
                if t <= max_t and s + jump <= n:
                    ways = (ways * (k + t - 1)) % MOD
                    ways = (ways * inv[t]) % MOD

        dp = ndp

    # Итог O(n) по памяти и O(n^2 + n^2 log n) времени

    write(str(dp[n]) + "\n")


if __name__ == "__main__":
    main()
