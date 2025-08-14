"""C. Дек с защитой от ошибок

Скорость работы: O(N)
Затрачено памяти: O(N)
"""

import sys

# import cProfile
from typing import Union, Callable, Dict
from collections import deque


class Deque:
    """Реализация дека"""

    __slots__ = ("_dq",)

    def __init__(self):
        """Инициализирует пустую двустороннюю дека (deque)."""
        self._dq: deque[int] = deque()

    def push_front(self, num: int) -> str:
        """Добавляет элемент x в начало дека."""
        self._dq.appendleft(num)
        return "ok"

    def push_back(self, num: int) -> str:
        """Добавляет элемент x в конец дека."""
        self._dq.append(num)
        return "ok"

    def pop_front(self) -> Union[int, str]:
        """Удаляет и возвращает элемент из начала дека."""
        return "error" if not self._dq else self._dq.popleft()

    def pop_back(self) -> Union[int, str]:
        """Удаляет и возвращает элемент из конца дека."""
        return "error" if not self._dq else self._dq.pop()

    def front(self) -> Union[int, str]:
        """Возвращает элемент из начала дека без его удаления."""
        return "error" if not self._dq else self._dq[0]

    def back(self) -> Union[int, str]:
        """Возвращает элемент из конца дека без его удаления."""
        return "error" if not self._dq else self._dq[-1]

    def size(self) -> int:
        """Возвращает количество элементов в деку."""
        return len(self._dq)

    def clear(self) -> str:
        """Очищает дек, удаляя все элементы."""
        self._dq.clear()
        return "ok"


def main():
    """Точка входа в программу"""

    dq = Deque()

    commands: Dict[str, Callable[..., Union[int, str]]] = {
        "push_front": dq.push_front,
        "push_back": dq.push_back,
        "pop_front": dq.pop_front,
        "pop_back": dq.pop_back,
        "front": dq.front,
        "back": dq.back,
        "size": dq.size,
        "clear": dq.clear,
    }

    output: list[Union[int, str]] = []  # Храним результат работы программы

    for line in sys.stdin:
        cmd = line.strip().split()
        do = cmd[0]

        if do == "exit":
            output.append("bye")
            print("\n".join(map(str, output)))
            return

        if do in ("push_front", "push_back"):
            output.append(commands[do](int(cmd[1])))
        else:
            output.append(commands[do]())


if __name__ == "__main__":
    # cProfile.run("main()", "result.prof")
    main()
