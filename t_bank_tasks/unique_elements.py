import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for l in range(n):
        freq: dict[int, int] = {}
        for r in range(l, min(n, l + 10)):
            freq[a[r]] = freq.get(a[r], 0) + 1
            length = r - l + 1
            if length >= 3:
                found = False
                for i in range(l, r - 1):
                    for j in range(i + 1, r):
                        for k in range(j + 1, r + 1):
                            if a[j] - a[i] == a[k] - a[j]:
                                ans += 1
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break

    print(ans)


if __name__ == "__main__":
    main()
