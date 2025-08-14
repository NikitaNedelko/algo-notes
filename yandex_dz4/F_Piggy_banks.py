"""F. Piggy banks

Скорость работы: O(N)
Затрачено памяти: O(N)
"""

import sys
from collections import deque


def main():

    N = int(sys.stdin.readline().strip())

    banks: dict[int, tuple[int, int]] = dict()

    # ввод исходных данных
    for id_bank in range(N):
        id_key = int(sys.stdin.readline().strip())
        banks[id_bank] = (id_key, 0)

    def fill_coef(banks: dict[int, tuple[int, int]]):
        """Считаем сколько разбитая банка может открыть банок в будущем"""
        visited: deque[int] = deque()
        for id, count in enumerate(banks):

            if count != 0:
                continue
            current_bank_id = id + 1

            while current_bank_id not in visited:

                # если мы попали в кольцо которое уже считали
                if banks[current_bank_id][1] != 0:
                    current_count = banks[current_bank_id][0]
                    current_bank_id = banks[current_bank_id][1]

                visited.append(id)
                current_bank_id, _ = banks[current_bank_id]

            for id in visited:
                current_count = len(visited) - 1

                # если мы попали в кольцо
                if id == current_bank_id:
                    for id in visited:
                        banks[id] = (current_count, current_bank_id)
                        visited.popleft()
                    break

                banks[id] = (current_count, current_bank_id)
                visited.popleft()

    while 0 != len(banks):
        visited: deque[int] = deque([0] * len(banks.values()))

    return True


if __name__ == "__main__":
    main()

"""
сделать dict со всеми шкатулками и ключами в них  
создаем массив в котором позиция это номер шкатулки, на число в этой позиции это количество шкатулок которые потом получится открыть 
при подсчете количества шкатулок которые модно открыть, создадим стек и будем добавлять id каждой шкатулки которую посетили, 
если id повторился - это значит кольцо и мы должны количество шкатулок которое открывает эта шкатулка написать на все след шкатулки в этом кольце   
пример: 4->3->2->->1->3 => получим такие веса 
4=3
3=2
2=2
1=2
затем берем самую большую шкатулку с весом и разбиваем ее, удаляем все шкатулки которые разбили и открыли со словаря banks и потом опять считаем веса для каждой шкатулки  

0 можно сразу разъебать 
"""
