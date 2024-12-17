def print_odd_numbers_descending():
    """
    Запрашивает у пользователя два целых числа A и B (A > B) и выводит
    все нечетные числа от A до B включительно в порядке убывания.
    """

    while True:
        try:
            A = int(input("Введите целое число A: "))
            B = int(input("Введите целое число B: "))
            if A > B:
                break  # Выход из цикла, если A > B
            else:
                print("Ошибка: A должно быть больше B. Попробуйте еще раз.")
        except ValueError:
            print(
                "Ошибка: Введены некорректные данные. Пожалуйста, введите целые числа."
            )

    for num in range(A, B - 1, -1):
        if num % 2 != 0:  # Проверка на нечетность
            print(num)


# Вызов функции
print_odd_numbers_descending()
