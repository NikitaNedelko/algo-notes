import sys

input = sys.stdin.readline


def main(n: int, cost_swap: int, cost_change: int, s: str):
    """Точка входа в программу"""

    open_b = 0
    close_b = 0

    for ch in s:
        if ch == "(":
            open_b += 1
        else:
            if open_b > 0:
                open_b -= 1
            else:
                close_b += 1

    swaps = min(open_b, close_b)
    changes = abs(open_b - close_b)

    cost_combo = swaps * cost_swap + changes // 2 * cost_change

    if open_b == 0 or close_b == 0:
        changes = changes // 2
    cost_all_changes = (open_b + close_b) * cost_change

    cost_all_swaps = float("inf")
    if open_b != 0 and close_b != 0 and open_b == close_b:
        cost_all_swaps = (
            (open_b + close_b) // 2 * cost_swap
            if (open_b + close_b) % 2 == 0
            else float("inf")
        )

    return int(min(cost_combo, cost_all_changes, cost_all_swaps))


if __name__ == "__main__":
    n, cost_swap, cost_change = map(int, input().strip().split())
    s = input().strip()
    print(main(n, cost_swap, cost_change, s))

"""
2 100 1
))

2 100 1
((

2 1 100
))

2 1 100
((

2 100 1
)()(

2 1 100
)()(

2 100 1
)(((

2 1 100
)(((
"""
