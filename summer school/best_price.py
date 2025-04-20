"""
сколько существует пар дней (x, y) такие, что:

x < y (сначала покупаешь, потом продаёшь);

p[x] < p[y] (цена в день покупки меньше цены в день продажи).


Скорость работы: O(200 * N)
Затрачено памяти: O(N)
"""


def main():
    """Точка входа в программу."""
    _ = int(input())
    prices = list(map(int, input().split()))  # O(N) по времени
    max_price = max(prices) + 1  # O(N) по времени
    count_of_price: dict[int, int] = {
        i: 0 for i in range(1, max_price)
    }  # O(200) по времени

    num_pairs = 0

    for i in prices[::-1]:  # O(N) по времени
        for j in range(i + 1, max_price):  # O(200) по времени
            num_pairs += count_of_price[j]
        count_of_price[i] += 1

    print(num_pairs)


if __name__ == "__main__":
    main()


"""
1 5 4 6 2 

1 - 4 
2 - 0
3 - -1
4 - 1
5 - 1
6 - 0
7 - -1

1 5
1 4
1 6
1 2
5 6
4 6

1 1 5 4 6 2 2

1 2
2 2
3 0
4 1
5 1
6 1

sum = 1*1 + 1*1 + 1*2 + 1*1 + 1*1 + 1*1 + 1*2 + 3 

"""
