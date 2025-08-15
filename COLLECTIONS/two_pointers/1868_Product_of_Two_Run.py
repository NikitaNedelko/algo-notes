"""
затрачено времени:
затрачено памяти:
"""


def multiplyRLE(
    encoded1: list[list[int]], encoded2: list[list[int]]
) -> list[list[int]]:
    answer: list[list[int]] = []

    i = j = 0
    v1 = v2 = 0
    c1 = c2 = 0

    while i < len(encoded1) or j < len(encoded2):
        if c1 == 0:
            v1, c1 = encoded1[i]
            i += 1
        if c2 == 0:
            v2, c2 = encoded2[j]
            j += 1

        current_c = min(c1, c2)
        product = v1 * v2

        if answer and answer[-1][0] == product:
            answer[-1][1] += current_c
        else:
            answer.append([product, current_c])

        c1 -= current_c
        c2 -= current_c

    return answer


def multiplyRLE2(
    encoded1: list[list[int]], encoded2: list[list[int]]
) -> list[list[int]]:
    answer: list[list[int]] = []

    first_count = 0
    second_count = 0

    first_len = len(encoded1)
    second_len = len(encoded2)

    while first_count != first_len and second_count != second_len:
        first_node: list[int] = encoded1[first_count]
        second_node: list[int] = encoded2[second_count]
        current_first_len = first_node[1]
        current_second_len = second_node[1]
        if current_first_len < current_second_len:
            second_node[1] -= current_first_len
            answer.append([second_node[0] * first_node[0], current_first_len])
            first_count += 1
        elif current_first_len > current_second_len:
            first_node[1] -= current_second_len
            answer.append([second_node[0] * first_node[0], current_second_len])
            second_count += 1
        elif current_first_len == current_second_len:
            answer.append([second_node[0] * first_node[0], current_first_len])
            first_count += 1
            second_count += 1

    if first_count == first_len:
        for i in range(second_count, second_len):
            answer.append(encoded2[i])
    if second_count == second_len:
        for i in range(first_count, first_len):
            answer.append(encoded1[i])

    return answer


if __name__ == "__main__":
    # Пример входных данных
    encoded1 = [[1, 3], [2, 2]]  # [1, 1, 1, 2, 2]
    encoded2 = [[4, 2], [3, 3]]  # [4, 4, 3, 3, 3]

    # Ожидаемый результат:
    # [1*4, 1*4, 1*3, 2*3, 2*3] = [4, 4, 3, 6, 6] → [[4,2],[3,1],[6,2]]

    result = multiplyRLE(encoded1, encoded2)
    print("Результат:", result)

    # Пример входных данных
    encoded1 = [[1, 4], [2, 2], [3, 4]]
    encoded2 = [[1, 2], [2, 3], [3, 2], [4, 3]]

    # Ожидаемый результат:
    # [1*4, 1*4, 1*3, 2*3, 2*3] = [4, 4, 3, 6, 6] → [[4,2],[3,1],[6,2]]

    result = multiplyRLE(encoded1, encoded2)
    print("Результат:", result)
