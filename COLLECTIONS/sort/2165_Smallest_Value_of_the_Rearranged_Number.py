import sys

input = sys.stdin.readline


# ! Через частоту каждой цифры
def main():
    num = sorted(input().strip())
    not_zero_id = 0
    if num[0] == "0":
        for id, n in enumerate(num):
            if n != "0":
                not_zero_id = id
                break
    num[not_zero_id], num[0] = num[0], num[not_zero_id]
    print("".join(num))


if __name__ == "__main__":
    main()
