"""G. Две стены

Скорость работы:
Затрачено памяти:
"""


def main():
    """Точка входа в программу"""

    N, K = map(int, input().split())

    bricks: dict[int, list[int]] = {}  # длинна всех кирпичей по цвету
    bricks_id: dict[int, list[tuple[int, int]]] = {}  # длина и id кирпичей

    # вводим все кирпичи по каждому цвету
    for idx in range(1, N + 1):
        L, color = map(int, input().split())
        if color not in bricks:
            bricks[color] = [0]
            bricks_id[color] = []
        bricks[color][0] += L
        bricks[color].append(L)
        bricks_id[color].append((L, idx))

    # проверка что количество цветов >= K
    for i in range(1, K + 1):
        if i not in bricks:
            print("NO")
            return

    min_len = float("inf")  # минимальная длинна одного цвета
    id_min = -1  # id кирпича с минимальной длинной

    for id, i in bricks.items():
        if i[0] < min_len:
            min_len = i[0]
            id_min = id

    # print(f"min = {bricks[id_min]}")

    combinations = [None for _ in range(int(min_len // 2) + 1)]
    combinations[0] = []  # пустая комбинация для суммы 0

    for i, idx in bricks_id[id_min]:
        for j in range(int(min_len // 2), i - 1, -1):
            if combinations[j - i] is not None and combinations[j] is None:
                combinations[j] = combinations[j - i] + [idx]

    valid = None
    for i in range(len(combinations) - 1, 1, -1):
        if combinations[i] is not None:
            valid = combinations[i]
            break

    if valid is None:
        print("NO")
        return

    print("YES")
    print(*sorted(valid))


if __name__ == "__main__":
    main()


"""

Суть:       две прямоугольный стены, в которых попарно слои j одинакового цвета и одинаковой высоты, но ширина может быть разной . 
Ввод:       N (количество кирпичей) , K (высота)
            L длинна - C цвет
Вывести:    YES/NO если можно построить стенки
            номера кирпичей из которых сделана первая стена 

Идеи:       1) вводим все кирпичи по каждому цвету
            2) смотрим самую короткую длину у какого цвета, затем смотрим какие у него есть комбинации с не пересекающимися кирпичами 
            (надо искать комбинации до половинны всей длинны кирпичей тк если мы знаем как сделать 4 то знаем что из оставшихся будет 6 И 
            при этом кирпичи не будут пересекаться в 4 и 6 комбинации  )
            3) затем ищем эталонные (те комбинации которые в минимуме длине) комбинации в каждом цвете
            чтобы подтвердить, что в цвете, есть такое же комбинации с не пересекающимися кирпичами, нужно найти в комбинациях нового цвета (для 4 и 6 сейчас напишу)
            4 in и (6 in или (n - 6) in )
            4) если находим то YES 

            Можно ли при вводе сразу что посчитать ? 
            все комбинации длин кирпичей нельзя, так как нам нужна сумма всех кирпичей, оттуда мы и будем начинать расчет комбинаций

            Откидываем все цвета которые больше K. т.к. "первый горизонтальный слой кирпичиков в стене будет первого цвета, второй — второго и т. д."
            сначала надо проверить можем ли мы вообще такую высоту сделать,  ПО УСЛОВИЮ УЖЕ ЕСТЬ ТАКОЕ 

            
7 2
3 1
4 2
3 1
4 2
3 1
4 2
3 1

"""
