def print_numbers_range():
    """Запрашивает у пользователя два целых числа A и B (A < B)
    и выводит все числа от A до B включительно.
    """
    while True:
        try:
            A = int(input("Введите целое число A: "))
            B = int(input("Введите целое число B: "))
            if A < B:
                break  # Выход из цикла, если условие A < B выполняется
            else:
                print("Ошибка: A должно быть меньше B. Попробуйте еще раз.")
        except ValueError:
            print(
                "Ошибка: Введены некорректные данные. Пожалуйста, введите целые числа."
            )

    for num in range(A, B + 1):
        print(num)


# Вызов функции
print_numbers_range()
