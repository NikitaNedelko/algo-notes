"""НЕ СДЕЛАЛ"""

"""H. Дерево отрезков с операцией на отрезке


Скорость работы: O(K log N)
Затрачено памяти: O(2*N - 1)
"""


def main():
    """Точка входа в программу"""

    # ввод данных
    _ = int(input())
    nums = list(map(int, input().split()))
    M = int(input())

    # массив для хранения отрезков с операцией
    list_of_operations: list[list[int]] = []

    for _ in range(M):  # O(M) по времени
        params = input().split()
        F = params[0]
        ID = int(params[1])
        if F == "a":
            L = int(params[1])
            R = int(params[2])
            I = int(params[3])

            for i in list_of_operations:
                if i[0] <= L <= i[1] and i[0] <= R  <= i[1]:
                    i[1] = L 
                    list_of_operations.append([R,i[1], I])

                else if i[0] <= L <= i[1]:
                else if i[0] <= R <= i[1]:

            list_of_operations.append([L, R, I])

            continue

        select_num = int(nums[ID])
        for i in list_of_operations:  # O(M) по времени
            if i[0] <= ID <= i[1]:
                select_num += i[2]
                break

        print(select_num)


if __name__ == "__main__":
    main()
"""
10
613 263 312 670 216 142 976 355 488 370
3
m 1 3
a 2 10 100
m 4 5
"""
