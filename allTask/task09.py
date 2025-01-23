import os


def read_data_from_file(filename):
    """Читает данные из файла и возвращает их."""
    with open(filename, "r") as f:
        data = {}

        # Читаем массивы
        arrays_data = []
        while True:
            line = f.readline()
            if not line:
                break
            numbers = [x for x in line.strip().split()]
            arrays_data.append(numbers)
        data["arrays"] = arrays_data

        # Читаем матрицу A
        matrix_a_data = []
        while True:
            line = f.readline()
            if not line:
                break
            row = [x for x in line.strip().split()]
            matrix_a_data.append(row)
        data["matrix_a"] = matrix_a_data

        # Читаем матрицу B
        matrix_b_data = []
        while True:
            line = f.readline()
            if not line:
                break
            row = [x for x in line.strip().split()]
            matrix_b_data.append(row)
        data["matrix_b"] = matrix_b_data

    return data


def write_results_to_file(filename, results):
    """Записывает результаты в файл."""
    with open(filename, "w") as f:
        f.write("----- Массивы -----\n")
        for i, arr in enumerate(results.get("arrays", [])):
            f.write(f"Массив {i+1}: {arr}\n")

        f.write("\n----- Матрица A -----\n")
        for row in results.get("matrix_a", []):
            f.write(str(row) + "\n")

        f.write("\n----- Матрица B -----\n")
        for row in results.get("matrix_b", []):
            f.write(str(row) + "\n")


if __name__ == "__main__":
    base_dir = r"D:\proj\vsuet\allTask"
    input_filename = os.path.join(base_dir, "Иванов_Иван_Иванович_ЗИТ24-1_vvod.txt")
    output_filename = os.path.join(base_dir, "Иванов_Иван_Иванович_ЗИТ24-1_vivod.txt")

    data = read_data_from_file(input_filename)
    write_results_to_file(output_filename, data)

    print(f"Данные скопированы из {input_filename} в {output_filename}")
