"""
по скорости: O(n)
по памяти: O(n)
"""

from collections import defaultdict
import sys

input = sys.stdin.readline

MOD = 1000000007


def main():
    _ = int(input())
    arr = list(map(int, input().strip().split()))
    freq: defaultdict[int, int] = defaultdict(int)
    for num in arr:
        freq[num] += 1

    ans = 1
    for f in freq.values():
        ans = (ans * (f + 1)) % MOD

    print((ans - 1) % MOD)


if __name__ == "__main__":
    main()
