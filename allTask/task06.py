def process_integer_array():
    """
    Ввод массива целых чисел, поиск максимума и вывод массива в обратном порядке.
    """
    n = int(input("Введите количество элементов массива целых чисел: "))
    arr = []
    for i in range(n):
        element = int(input(f"Введите элемент массива {i+1}: "))
        arr.append(element)

    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element

    print("Максимальный элемент:", max_element)

    print("Массив в обратном порядке:")
    for i in range(n - 1, -1, -1):
        print(arr[i], end=" ")
    print()


def process_float_array():
    """
    Заменяет все нулевые элементы в массиве действительных чисел на среднее
    арифметическое всех элементов.
    """
    n = int(input("Введите количество элементов массива действительных чисел: "))
    arr = []
    for i in range(n):
        element = float(input(f"Введите элемент массива {i+1}: "))
        arr.append(element)

    total_sum = sum(arr)
    average = total_sum / n

    for i in range(n):
        if arr[i] == 0:
            arr[i] = average

    print("Массив после замены нулей:")
    print(arr)


if __name__ == "__main__":
    print("----- Задача 1: Поиск максимума и обратный вывод -----")
    process_integer_array()

    print("\n----- Задача 2: Замена нулей на среднее -----")
    process_float_array()
