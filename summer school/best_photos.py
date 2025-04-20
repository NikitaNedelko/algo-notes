"""
Лиза должна оказаться на каждом снимке!
Между снимками она может:

сдвинуться ровно на 1 клетку по стороне (вверх, вниз, влево, вправо).

нельзя оставаться в той же клетке два снимка подряд.

нельзя прыгать дальше чем на 1 клетку.

"""


def main():
    n, m = map(int, input().split())  # размеры поля
    k = int(input())  # количество снимков

    # координаты снимков: список прямоугольников
    snapshots: list[tuple[int, int, int, int]] = []
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        snapshots.append((x1, y1, x2, y2))

    # начальные возможные позиции: все клетки первого прямоугольника
    current_positions: set[tuple[int, int]] = set()
    x1, y1, x2, y2 = snapshots[0]
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            current_positions.add((x, y))

    # переход по каждому снимку начиная со второго
    for snap in snapshots[1:]:
        x1, y1, x2, y2 = snap
        next_positions: set[tuple[int, int]] = set()

        for x, y in current_positions:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 4 направления
                nx, ny = x + dx, y + dy

                # Проверка границ снимка и поля
                if x1 <= nx <= x2 and y1 <= ny <= y2:
                    next_positions.add((nx, ny))

        # если нет куда идти — сразу "NO"
        if not next_positions:
            print("NO")
            return

        current_positions = next_positions

    print("YES")


if __name__ == "__main__":
    main()


"""
100 100
3
5 5 6 7
3 3 8 6
7 4 7 4

100 100
4
5 5 6 7
3 3 8 6
7 4 7 4
7 4 7 4

 """
