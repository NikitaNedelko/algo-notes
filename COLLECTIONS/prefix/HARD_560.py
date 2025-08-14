def subarraySum(nums: list[int], k: int):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    current_prefix = 0
    last_prefix: dict[int, set[int]] = {0: {-1}}  # префикс -> частота
    # ! ОБЯЗАТЕЛЬНО учесть {0:1}
    ans: list[list[int]] = []

    for ind, num in enumerate(nums):
        current_prefix += num
        prev_prefix = current_prefix - k
        for index in last_prefix.get(prev_prefix, {}):
            ans.append([index + 1, ind])
        if current_prefix not in last_prefix:
            last_prefix[current_prefix] = set()
        last_prefix[current_prefix].add(ind)
        print(last_prefix)

    return ans


def run_tests():
    tests = [
        # format: (nums, k, expected)
        ([1, 1, 1], 2, [[0, 1], [1, 2]]),
        ([1, 2, 3], 3, [[0, 1], [2, 2]]),
        ([1, -1, 0], 0, [[0, 1], [2, 2], [0, 2]]),
        ([1], 1, [[0, 0]]),
        ([1], 2, []),
        ([0, 0, 0], 0, [[0, 0], [1, 1], [2, 2], [0, 1], [1, 2], [0, 2]]),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        result = subarraySum(nums, k)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        assert (
            result_sorted == expected_sorted
        ), f"Test {i} failed: got {result}, expected {expected}"
        print(f"Test {i} passed.")


if __name__ == "__main__":
    run_tests()
