import sys
from collections import defaultdict
from heapq import nlargest


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    intervals = []
    all_days = set()

    for _ in range(n):
        l, r, c = map(int, input().split())
        intervals.append((l, r, c))
        all_days.add(l)
        all_days.add(r)

    all_days = sorted(all_days)
    day_to_idx = {day: i for i, day in enumerate(all_days)}

    day_jobs = defaultdict(list)
    for l, r, c in intervals:
        l_idx = day_to_idx[l]
        r_idx = day_to_idx[r]
        for day in range(l_idx, r_idx + 1):
            day_jobs[day].append(c)

    total_income = 0

    for day in sorted(day_jobs.keys()):
        workers = day_jobs[day]
        best_m = nlargest(m, workers)
        total_income += sum(best_m)

    print(total_income)


if __name__ == "__main__":
    main()

"""
Вася работает таксистом для души, а вообще у него есть бизнес — таксопарк.

Вася владеет 
M
M одинаковыми автомобилями такси. У него есть 
N
N знакомых, которые взяли себе отпуска и хотели бы попробовать поработать в такси. Для каждого из знакомых известны даты отпуска, 
i
i-ый знакомый находится в отпуске с дня 
l
i
l 
i
​
  до дня 
r
i
r 
i
​
  включительно. Каждый знакомый готов выйти на работу в такси в любой из дней отпуска, но если Вася его не позовет, то он будет просто отдыхать.

Вася хорошо знает своих знакомых и для каждого из них определил, какую цену на аренду автомобиля на день можно назначить этому человеку. Цена аренды для разных знакомых может отличаться.

Помогите Васе определить, какое максимальное количество денег он может заработать, сдавая в аренду автомобили своим знакомым.

Формат ввода
В первой строке записано два числа 
N
N и 
M
M (
1
≤
M
,
N
≤
200
000
1≤M,N≤200000) — количество знакомых и автомобилей Васи.

В следующих 
N
N строках дано описание знакомых Васи. Каждое описание состоит из трёх чисел 
l
i
l 
i
​
 , 
r
i
r 
i
​
  и 
c
i
c 
i
​
  (
1
≤
l
i
≤
r
i
≤
1
0
8
1≤l 
i
​
 ≤r 
i
​
 ≤10 
8
 , 
1
≤
c
i
≤
10
000
1≤c 
i
​
 ≤10000) — номер первого и последнего дня отпуска 
i
i-го знакомого и цена, которую он готов платить за аренду автомобиля.

Формат вывода
Выведите одно число — максимальный заработок Васи.

3 2
1 3 3
1 5 1
2 4 2

"""
