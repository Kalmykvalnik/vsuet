import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from pprint import pprint
import json


def get_repo_info():
    username = entry.get()
    if not username:
        messagebox.showerror("Ошибка", "Введите имя пользователя GitHub")
        return

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка ошибок
        user_data = response.json()

        # Извлекаем нужные данные
        selected_data = {
            "company": user_data.get("company"),
            "created_at": user_data.get("created_at"),
            "email": user_data.get("email"),
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "url": user_data.get("html_url"),  # Используем html_url вместо url
        }

        # Сохраняем в файл
        with open("user_info.json", "w") as f:
            json.dump(selected_data, f, indent=4)

        messagebox.showinfo("Успех", "Информация сохранена в файл user_info.json")
        pprint(selected_data)  # Вывод в консоль

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибка запроса: {e}")
    except json.JSONDecodeError as e:
        messagebox.showerror("Ошибка", f"Ошибка разбора JSON: {e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла неизвестная ошибка: {e}")


# Создаем главное окно
root = tk.Tk()
root.title("Информация о репозитории GitHub")

# Создаем метку и поле ввода
label = ttk.Label(root, text="Имя пользователя GitHub:")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=5)

# Создаем кнопку
button = ttk.Button(root, text="Получить информацию", command=get_repo_info)
button.pack(pady=10)

root.mainloop()
