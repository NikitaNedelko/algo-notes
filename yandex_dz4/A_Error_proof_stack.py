"""A. Error-proof stack

Скорость работы: O(N)
Затрачено памяти: O(N)
"""

from collections import deque
from typing import Union, Callable, Dict


class Stack:
    """Реализация стека"""

    __slots__ = ("_stack",)

    def __init__(self):
        self._stack: deque[int] = deque()

    def push(self, num: int) -> str:
        """добавляет число в стек и выводит ok"""

        self._stack.append(num)
        return "ok"

    def pop(self) -> Union[int, str]:
        """удаляет и выводит последний элемент или "error", если стек пуст"""

        return "error" if not self._stack else self._stack.pop()

    def back(self) -> Union[int, str]:
        """выводит последний элемент без удаления или "error", если стек пуст"""

        return "error" if not self._stack else self._stack[-1]

    def size(self) -> int:
        """выводит количество элементов"""
        return len(self._stack)

    def clear(self) -> str:
        """очищает стек и выводит ok"""
        self._stack.clear()
        return "ok"


def main():
    """Точка входа в программу"""

    stack = Stack()

    commands: Dict[str, Callable[[], Union[int, str]]] = {
        "pop": stack.pop,
        "back": stack.back,
        "size": stack.size,
        "clear": stack.clear,
    }

    while True:

        cmd = input().split()

        do = cmd[0]

        if do == "push":
            print(stack.push(int(cmd[-1])))
        elif do == "exit":
            print("bye")
            break
        else:
            print(commands[do]())


if __name__ == "__main__":
    main()
