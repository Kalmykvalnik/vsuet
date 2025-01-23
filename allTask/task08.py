import random


def process_matrix_above_diagonal(matrix):
    """
    Вычисляет сумму и количество положительных элементов матрицы над главной диагональю.
    """
    n = len(matrix)
    total_sum = 0
    positive_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                total_sum += matrix[i][j]
                positive_count += 1

    return total_sum, positive_count


def modify_matrix_rows(matrix):
    """
    Находит максимальный и минимальный элементы в каждой строке матрицы и
    меняет их местами с первым и последним элементами строки.
    """
    for row in matrix:
        if not row:  # Проверка на пустую строку
            continue

        min_val = row[0]
        max_val = row[0]
        min_idx = 0
        max_idx = 0

        for i, val in enumerate(row):
            if val < min_val:
                min_val = val
                min_idx = i
            if val > max_val:
                max_val = val
                max_idx = i

        # Swap min with first
        row[0], row[min_idx] = row[min_idx], row[0]

        # Swap max with last, handle potential overlap
        if max_idx != 0:
            if max_idx == len(row) - 1:

                if min_idx == len(row) - 1:
                    pass
                else:
                    row[max_idx], row[-1] = row[-1], row[max_idx]
            else:
                row[max_idx], row[-1] = row[-1], row[max_idx]

    return matrix


if __name__ == "__main__":
    # Задача 1: Обработка матрицы выше диагонали
    matrix_a = [[1, 2, 3, 4], [-1, 5, 6, 7], [0, -2, 8, 9], [2, 5, 1, 7]]
    sum_above, count_above = process_matrix_above_diagonal(matrix_a)
    print("----- Задача 1: Сумма и количество положительных над диагональю -----")
    print(f"Сумма: {sum_above}, Количество: {count_above}")

    # Задача 2: Модификация строк матрицы
    matrix_b = [[2, 8, 1, 9, 4], [10, 3, 12, 1, 5], [7, 2, 6, 11, 3]]
    modified_matrix_b = modify_matrix_rows(matrix_b)
    print("\n----- Задача 2: Модифицированная матрица B -----")
    for row in modified_matrix_b:
        print(row)

    # Пример со случайными матрицами
    rows_a = 4
    cols_a = 4
    rows_b = 3
    cols_b = 5

    random_matrix_a = [
        [random.randint(-10, 10) for _ in range(cols_a)] for _ in range(rows_a)
    ]
    random_matrix_b = [
        [random.randint(-10, 10) for _ in range(cols_b)] for _ in range(rows_b)
    ]

    print("\n----- Пример со случайными матрицами -----")
    print("Случайная матрица A:", random_matrix_a)
    sum_above_random_a, count_above_random_a = process_matrix_above_diagonal(
        random_matrix_a
    )
    print(f"Сумма: {sum_above_random_a}, Количество: {count_above_random_a}")
    modified_matrix_random_b = modify_matrix_rows(random_matrix_b)
    print("Модифицированная случайная матрица B:", modified_matrix_random_b)
