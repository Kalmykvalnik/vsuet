import math


def calculate_area(shape, *args):
    """Вычисляет площадь геометрической фигуры."""
    if shape == "треугольник":
        a, b, c = args
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    elif shape == "квадрат":
        (a,) = args  # Распаковка кортежа
        area = a * a
        return area
    elif shape == "круг":
        (r,) = args  # Распаковка кортежа
        area = math.pi * r * r
        return area
    else:
        return None


def calculate_sum_and_average(arr):
    """Вычисляет сумму и среднее арифметическое элементов массива."""
    total_sum = sum(arr)
    average = total_sum / len(arr) if len(arr) > 0 else 0
    return total_sum, average


if __name__ == "__main__":
    # Задача 1: Площади фигур
    triangle_area = calculate_area("треугольник", 3, 4, 5)
    square_area = calculate_area("квадрат", 5)
    circle_area = calculate_area("круг", 3)

    print(f"Площадь треугольника: {triangle_area}")
    print(f"Площадь квадрата: {square_area}")
    print(f"Площадь круга: {circle_area}")

    # Задача 2: Суммы и средние арифметические
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [10, 20, 30]
    arr3 = [5, 10, 15, 20, 25, 30]

    sum1, avg1 = calculate_sum_and_average(arr1)
    sum2, avg2 = calculate_sum_and_average(arr2)
    sum3, avg3 = calculate_sum_and_average(arr3)

    print("\n----- Результаты для массивов -----")
    print(f"Массив 1: Сумма = {sum1}, Среднее = {avg1}")
    print(f"Массив 2: Сумма = {sum2}, Среднее = {avg2}")
    print(f"Массив 3: Сумма = {sum3}, Среднее = {avg3}")
