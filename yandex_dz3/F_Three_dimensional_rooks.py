"""H. Звезды


Скорость работы: O(N + K)
Затрачено памяти: O(N)
"""


def main():
    """Точка входа в программу"""

    N, K = map(int, input().split())

    x_cord: set[int] = set()  # O(N) по памяти
    y_cord: set[int] = set()  # O(N) по памяти
    z_cord: set[int] = set()  # O(N) по памяти

    for _ in range(K):  # O(K) по времени
        x, y, z = map(int, input().split())
        x_cord.add(x)
        y_cord.add(y)
        z_cord.add(z)

    if len(x_cord) == N and len(y_cord) == N and len(z_cord) == N:
        print("YES")
    else:
        print("NO")
        for i in range(1, N + 1):  # Ось X
            for j in range(1, N + 1):  # Ось Y
                for k in range(1, N + 1):  # Ось Z
                    if i not in x_cord and j not in y_cord and k in z_cord:
                        print(i, j, k)
                        return
                    if i not in x_cord and j in y_cord and k not in z_cord:
                        print(i, j, k)
                        return
                    if i in x_cord and j not in y_cord and k not in z_cord:
                        print(i, j, k)
                        return
                    if i not in x_cord and j not in y_cord and k not in z_cord:
                        print(i, j, k)
                        return


if __name__ == "__main__":
    main()
