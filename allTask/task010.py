import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Иванов Иван Иванович")
        self.geometry("600x400")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.create_calculator_tab()
        self.create_checkbox_tab()
        self.create_text_tab()

        self.create_menu()

    def create_calculator_tab(self):
        calculator_tab = ttk.Frame(self.notebook)
        self.notebook.add(calculator_tab, text="Калькулятор")

        tk.Label(calculator_tab, text="Первое число:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        self.num1_entry = tk.Entry(calculator_tab)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(calculator_tab, text="Операция:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        self.operation_var = tk.StringVar(value="+")
        operations = ["+", "-", "*", "/"]
        self.operation_dropdown = ttk.Combobox(
            calculator_tab,
            textvariable=self.operation_var,
            values=operations,
            state="readonly",
        )
        self.operation_dropdown.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(calculator_tab, text="Второе число:").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        self.num2_entry = tk.Entry(calculator_tab)
        self.num2_entry.grid(row=2, column=1, padx=5, pady=5)

        calculate_button = tk.Button(
            calculator_tab, text="Вычислить", command=self.calculate
        )
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(calculator_tab, text="Результат: ")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль!")
                result = num1 / num2
            else:
                result = "Неизвестная операция"

            self.result_label.config(text=f"Результат: {result}")

        except ValueError:
            self.result_label.config(text="Некорректный ввод")
        except ZeroDivisionError as e:
            self.result_label.config(text=str(e))

    def create_checkbox_tab(self):

        checkbox_tab = ttk.Frame(self.notebook)
        self.notebook.add(checkbox_tab, text="Чекбоксы")

        self.check_var1 = tk.BooleanVar()
        self.check_var2 = tk.BooleanVar()
        self.check_var3 = tk.BooleanVar()

        tk.Checkbutton(checkbox_tab, text="Первый", variable=self.check_var1).grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Checkbutton(checkbox_tab, text="Второй", variable=self.check_var2).grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Checkbutton(checkbox_tab, text="Третий", variable=self.check_var3).grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )

        tk.Button(
            checkbox_tab, text="Подтвердить", command=self.show_checkbox_selection
        ).grid(row=3, column=0, padx=5, pady=10)

    def show_checkbox_selection(self):
        selection = []
        if self.check_var1.get():
            selection.append("первый")
        if self.check_var2.get():
            selection.append("второй")
        if self.check_var3.get():
            selection.append("третий")

        if selection:
            messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selection)}")
        else:
            messagebox.showinfo("Выбор", "Ничего не выбрано")

    def create_text_tab(self):
        text_tab = ttk.Frame(self.notebook)
        self.notebook.add(text_tab, text="Текст")

        self.text_area = tk.Text(text_tab)
        self.text_area.pack(fill="both", expand=True, padx=5, pady=5)

    def create_menu(self):
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Открыть файл", command=self.open_file)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        self.config(menu=menu_bar)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    text = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, text)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
