import math
from itertools import product


def gcd_list(lst):
    result = lst[0]
    for num in lst[1:]:
        result = math.gcd(result, num)
    return result


def main(n, a):
    mod = 998244353
    total = 0

    # Для каждого a_i, генерируем список возможных b_i
    b_options = []
    for ai in a:
        options = []
        for bi in range(ai, ai * 2 + 1):  # bi >= ai
            if math.gcd(ai, bi) == 1:
                options.append(bi)
        b_options.append(options)

    # Генерируем все возможные комбинации b
    for b_seq in product(*b_options):
        if gcd_list(b_seq) == 1:
            prod = 1
            for bi in b_seq:
                prod = (prod * bi) % mod
            total = (total + prod) % mod

    return total


if __name__ == "__main__":
    print(main(int(input()), list(map(int, input().split()))))
