# 1. Вычисление x^n / n! с использованием рекурсии


def power_factorial_recursive(x, n):
    """
    Вычисляет x^n / n! с использованием рекурсии.

    Args:
        x: Основание степени (натуральное число).
        n: Показатель степени (натуральное число).

    Returns:
        Значение выражения x^n / n!.
    """
    if n == 0:
        return 1.0  # Базовый случай: x^0 / 0! = 1 / 1 = 1
    else:
        return (x * power_factorial_recursive(x, n - 1)) / n


# Пример использования:
x = 2
n = 5
result = power_factorial_recursive(x, n)
print(f"{x}^{n} / {n}! = {result}")


# 2. Поиск максимального числа в последовательности с рекурсией (без глобальных переменных и параметров)


def find_max_recursive():
    """
    Считывает последовательность натуральных чисел с клавиатуры,
    завершающуюся числом 0, и возвращает наибольшее значение.
    Не использует глобальные переменные и не принимает параметры.
    """
    try:
        num = int(input())
    except ValueError:
        print("Ошибка: Введите целое число.")
        return find_max_recursive()  # Повторяем ввод

    if num == 0:
        return float(
            "-inf"
        )  # Базовый случай: конец последовательности, возвращаем отрицательную бесконечность
    else:
        max_rest = find_max_recursive()
        return num if num > max_rest else max_rest


# Пример использования:
print("Введите последовательность чисел, заканчивающуюся 0:")
max_value = find_max_recursive()
print(f"Максимальное значение в последовательности: {max_value}")
