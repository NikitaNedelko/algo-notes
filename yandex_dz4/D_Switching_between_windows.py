"""D. Переключение между окнами

Скорость работы: O(N)
Затрачено памяти: O(N)
"""

import sys

# import cProfile
# from typing import Union, Callable, Dict
from collections import deque


def main():
    """Точка входа в программу"""

    n = int(sys.stdin.readline())

    apps: deque[str] = deque()

    # output: deque[str] = deque()

    for _ in range(n):

        cmd = sys.stdin.readline().strip()

        if cmd.startswith("Run"):
            app = cmd[4:]

            apps.append(app)
            print(app)
            # output.append(app)

        elif cmd.startswith("Alt+Tab"):
            count_tab = cmd.count("+Tab")

            if len(apps) > 0:
                index = -count_tab % len(apps) - 1
                app = apps[index]
                print(app)
                # output.append(app)
                del apps[index]
                apps.append(app)


if __name__ == "__main__":
    # cProfile.run("main()", "result.prof")
    main()
