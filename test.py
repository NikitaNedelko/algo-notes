import sys

# sys.stdin.readline / sys.stdout.write — быстрый I/O без лишнего форматирования
input = sys.stdin.readline
write = sys.stdout.write

MOD = 1_000_000_007


def main():
    n, k = map(int, input().split())

    N = k + n
    C = [[0] * (k + n + 1) for _ in range(k + n + 1)]
    for i in range(N + 1):
        C[i][0] = C[i][i] = 1
        for j in range(1, i):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

    dp = [0] * (n + 1)
    dp[0] = 1

    for v in range(1, n + 1):
        ndp = dp[:]
        max_t = n // v
        for s in range(0, n + 1):
            if dp[s] == 0:
                continue
            base = dp[s]
            for t in range(1, max_t + 1):
                s2 = s + t * v
                if s2 > n:
                    break
                ways = C[k + t - 1][t]
                ndp[s2] = (ndp[s2] + base * ways) % MOD
        dp = ndp

    write(str(dp[n]) + "\n")


if __name__ == "__main__":
    main()
