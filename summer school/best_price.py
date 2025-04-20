"""
сколько существует пар дней (x, y) такие, что:

x < y (сначала покупаешь, потом продаёшь);

p[x] < p[y] (цена в день покупки меньше цены в день продажи).


Скорость работы: O(200 * N)
Затрачено памяти: O(200 + N)
"""


def main():
    """Точка входа в программу"""

    n = int(input())
    prices: list[int] = []  # O(N) по памяти
    max_price = -1
    for _ in range(n):  # O(N) по времени
        price = int(input())
        prices.append(price)
        if price > max_price:
            max_price = price

    count_of_price: list[int] = [0] * (max_price + 2)  # O(200) по памяти
    num_pairs = 0

    for i in reversed(prices):  # O(N) по времени
        num_pairs += sum(count_of_price[i + 1 : max_price + 1])  # O(200) по времени
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
