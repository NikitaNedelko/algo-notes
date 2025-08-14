from collections import defaultdict


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    cnt_left = defaultdict(int)
    cnt_right = defaultdict(int)

    for num in a:
        cnt_right[num] += 1

    ans = 0

    for j in range(n):
        cnt_right[a[j]] -= 1

        for x in range(1, 11):
            y = a[j]
            z = 2 * y - x
            if 1 <= z <= 10:
                ans += cnt_left[x] * cnt_right[z]

        cnt_left[a[j]] += 1

    print(ans)


if __name__ == "__main__":
    main()
