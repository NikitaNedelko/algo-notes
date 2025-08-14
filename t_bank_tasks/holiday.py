import heapq
import sys

input = sys.stdin.readline


def main(n: int, nums: list[int]) -> int:
    """Точка входа в программу"""

    if n < 2:
        return 0

    prev = [-1] + list(range(n - 1))
    next = list(range(1, n)) + [-1]
    used = [False] * n

    heap: list[tuple[int, int]] = []
    for i in range(n - 1):
        heapq.heappush(heap, (-(abs(nums[i] - nums[i + 1])), i))

    ans = 0
    while heap:
        diff, i = heapq.heappop(heap)
        j = next[i]
        if j == -1 or used[i] or used[j]:
            continue

        ans += -diff
        used[i] = used[j] = True
        l = prev[i]
        r = next[j]

        if l != -1:
            next[l] = r
        if r != -1:
            prev[r] = l
        if l != -1 and r != -1 and not used[l] and not used[r]:
            heapq.heappush(heap, (-(abs(nums[l] - nums[r])), l))

    return ans


if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(main(n, nums))
