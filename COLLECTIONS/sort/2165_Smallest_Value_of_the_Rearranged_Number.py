import sys

input = sys.stdin.readline
write = sys.stdout.write


def main():
    s = input().strip()
    freq = [0] * 10

    for ch in s:
        freq[ord(ch) - 48] += 1

    res: list[str] = []
    for i in range(1, 10):
        if freq[i]:
            res.append(str(i))
            freq[i] -= 1
            break

    for i in range(10):
        if freq[i]:
            res.extend([str(i) * freq[i]])

    write("".join(res))


if __name__ == "__main__":
    main()
