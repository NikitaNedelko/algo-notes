"""B. A queue with error protection

Скорость работы: O(N)
Затрачено памяти: O(N)
"""

from typing import Union, Callable, Dict

from collections import deque


class Queue:
    """Реализация очереди"""

    __slots__ = ("_queue",)

    def __init__(self):
        self._queue: deque[int] = deque()

    def push(self, num: int) -> str:
        """Добавляет в очередь число n и выводит ok"""
        self._queue.append(num)
        return "ok"

    def pop(self) -> Union[int, str]:
        """Удаляет и выводит первый элемент или "error", если очередь пуста"""
        return "error" if not self._queue else self._queue.popleft()

    def front(self) -> Union[int, str]:
        """Выводит значение первого элемента или "error", если очередь пуста"""
        return "error" if not self._queue else self._queue[0]

    def size(self) -> int:
        """выводит количество элементов"""
        return len(self._queue)

    def clear(self) -> str:
        """Очищает очередь и выводит ok"""
        self._queue.clear()
        return "ok"


def main():
    """Точка входа в программу"""

    queue = Queue()

    commands: Dict[str, Callable[[], Union[int, str]]] = {
        "pop": queue.pop,
        "front": queue.front,
        "size": queue.size,
        "clear": queue.clear,
    }

    while True:
        cmd = input().split()

        do = cmd[0]

        if do == "push":
            print(queue.push(int(cmd[-1])))
        elif do == "exit":
            print("bye")
            break
        else:
            print(commands[do]())


if __name__ == "__main__":
    main()
