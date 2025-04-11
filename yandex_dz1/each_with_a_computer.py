def main():
    N, _ = map(int, input().split())
    groups = dict(
        sorted(
            {
                id + 1: number for id, number in enumerate(map(int, input().split()))
            }.items(),
            key=lambda x: x[1],
            reverse=True,
        )
    )
    audiences = dict(
        sorted(
            {
                id + 1: number for id, number in enumerate(map(int, input().split()))
            }.items(),
            key=lambda x: x[1],
            reverse=True,
        )
    )
    ans = [0 for _ in range(N)]
    ans_count = 0

    group_generator = ((id_g, x) for id_g, x in groups.items())
    id_g, x = next(group_generator)

    last_id = list(groups.keys())[-1]

    for id_a, y in audiences.items():
        is_last = (id_g, x) != (last_id, groups[last_id])
        while is_last:
            if y > x:
                ans_count += 1
                ans[id_g - 1] = id_a
                id_g, x = next(group_generator)
                break
            id_g, x = next(group_generator)
            is_last = (id_g, x) != (last_id, groups[last_id])
        if not is_last and y > x:
            ans_count += 1
            ans[id_g - 1] = id_a
            break

    print(ans_count)
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
