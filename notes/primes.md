# 🔢 Простые числа и алгоритмы их нахождения

## 📌 Описание  
В этом разделе рассматриваются алгоритмы поиска простых чисел. В репозитории уже реализован **Решето Эратосфена**. В будущем планируется изучить более сложные методы.

## 📜 Алгоритмы

### Решето Эратосфена  
**Описание:**  
Алгоритм находит все простые числа до заданного `n` за **O(n log log n)**. Основан на последовательном вычеркивании кратных чисел.  

➕ Плюсы
- **Высокая эффективность:** Работает за время **O(n log log n)**, что делает его эффективным для нахождения простых чисел до больших значений.
- **Простота реализации:** Алгоритм легко реализуется, интуитивно понятен.
- **Подходит для больших чисел:** Может быстро обрабатывать большие значения `n`, в отличие от некоторых других методов, например, методом деления.

➖ Минусы
- **Занимает много памяти:** Для хранения всех чисел до `n` используется массив размера `n + 1`, что может потребовать значительных объемов памяти при больших значениях `n`.
- **Не оптимален для малых чисел:** Для небольших диапазонов другие методы, такие как тесты простоты или более простые алгоритмы, могут быть быстрее.

**📌 Реализация:**  
[🔗 sieve_of_eratosthenes.py](sieve_of_eratosthenes.py)  

```python
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]

 ```

## 🛠 В планах изучить:

- Расширенное решето Эратосфена (оптимизация с битовыми операциями)
- Решето Аткина (более эффективный алгоритм)
- Тесты простоты (Миллер-Рабин, Ферма)
- Факторизация чисел (метод Ферма, Полларда)