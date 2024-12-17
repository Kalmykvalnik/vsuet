def print_numbers_range():
    """Запрашивает у пользователя два целых числа A и B и выводит
    все числа от A до B включительно в порядке возрастания, если A < B,
    или в порядке убывания в противном случае.
    """

    while True:
        try:
            A = int(input("Введите целое число A: "))
            B = int(input("Введите целое число B: "))
            break  # Выход из цикла, если ввод успешен
        except ValueError:
            print(
                "Ошибка: Введены некорректные данные. Пожалуйста, введите целые числа."
            )

    if A < B:
        for num in range(A, B + 1):
            print(num)
    else:
        for num in range(A, B - 1, -1):
            print(num)


# Вызов функции
print_numbers_range()
