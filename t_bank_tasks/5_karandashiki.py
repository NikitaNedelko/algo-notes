"""
по времени: O(n^2 log n)
по памяти: O(n)
"""

import sys

input = sys.stdin.readline
write = sys.stdout.write

MOD = 1000000007


def main():
    n, k = map(int, input().split())
    inv = [0] * (n + 1)
    inv[1] = 1
    for t in range(2, n + 1):
        inv[t] = MOD - (MOD // t) * inv[MOD % t] % MOD

    dp = [0] * (n + 1)
    dp[0] = 1

    for v in range(1, n + 1):
        ndp = dp[:]
        max_t = n // v

        for s in range(n + 1):
            base = dp[s]
            if base == 0:
                continue

            ways = k % MOD
            jump = v
            t = 1
            while t <= max_t and s + jump <= n:
                ndp[s + jump] = (ndp[s + jump] + base * ways) % MOD
                t += 1
                jump += v
                if t <= max_t and s + jump <= n:
                    ways = (ways * (k + t - 1)) % MOD
                    ways = (ways * inv[t]) % MOD

        dp = ndp
    write(str(dp[n]) + "\n")


if __name__ == "__main__":
    main()
