import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # type: ignore
import math

# Функция для вычисления формулы для задания 1
def calculate_task_1():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        z = float(entry_z.get())

        # Формула для задания 1
        beta = math.sqrt(10 * (x ** (1/3) + x ** (y + z)) * ((math.asin(z) ** 2) - abs(x - y)))
        result_label.config(text=f"Результат: {beta:.5f}", fg="black")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения")
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль")

# Функция для вычисления формулы для задания 2
def calculate_task_2():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())

        # В зависимости от условия вычисляем l
        if 1 <= x < 5:
            l = (f(x) ** 2) + math.atan(f(x))
        elif y > x:
            l = ((y - f(x)) ** 2) + math.atan(f(x))
        else:
            l = ((y + f(x)) ** 3) + 0.5

        result_label.config(text=f"Результат: {l:.5f}", fg="black")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения")

# Пример функции f(x) для задания 2
def f(x):
    return math.cos(x)  # Здесь можно менять на нужную функцию

# Окно для задания 1
def open_task_1():
    task_window = tk.Toplevel(root)
    task_window.title("Задание 1")

    # Загрузка и отображение изображения формулы 1
    image_path = r"C:\Users\gatal\Desktop\Шарага\Обеспечение качества\Lab_4\formula1.png"
    equation_image = Image.open(image_path)
    equation_image = equation_image.resize((400, 100), Image.Resampling.LANCZOS)
    equation_photo = ImageTk.PhotoImage(equation_image)
    image_label = tk.Label(task_window, image=equation_photo)
    image_label.image = equation_photo
    image_label.pack(pady=10)

    # Поля ввода для задания 1
    tk.Label(task_window, text="Введите значение X:").pack()
    global entry_x
    entry_x = tk.Entry(task_window)
    entry_x.pack()

    tk.Label(task_window, text="Введите значение Y:").pack()
    global entry_y
    entry_y = tk.Entry(task_window)
    entry_y.pack()

    tk.Label(task_window, text="Введите значение Z:").pack()
    global entry_z
    entry_z = tk.Entry(task_window)
    entry_z.pack()

    # Кнопка для вычисления и вывод результата
    tk.Button(task_window, text="Вычислить", command=calculate_task_1).pack(pady=10)
    global result_label
    result_label = tk.Label(task_window, text="Результат: ", font=("Arial", 12))
    result_label.pack()

# Окно для задания 2
def open_task_2():
    task_window = tk.Toplevel(root)
    task_window.title("Задание 2")

    # Загрузка и отображение изображения формулы 2
    image_path = r"C:\Users\gatal\Desktop\Шарага\Обеспечение качества\Lab_4\formula2.png"
    equation_image = Image.open(image_path)
    equation_image = equation_image.resize((400, 100), Image.Resampling.LANCZOS)
    equation_photo = ImageTk.PhotoImage(equation_image)
    image_label = tk.Label(task_window, image=equation_photo)
    image_label.image = equation_photo
    image_label.pack(pady=10)

    # Поля ввода для задания 2
    tk.Label(task_window, text="Введите значение X:").pack()
    global entry_x
    entry_x = tk.Entry(task_window)
    entry_x.pack()

    tk.Label(task_window, text="Введите значение Y:").pack()
    global entry_y
    entry_y = tk.Entry(task_window)
    entry_y.pack()

    # Кнопка для вычисления и вывод результата
    tk.Button(task_window, text="Вычислить", command=calculate_task_2).pack(pady=10)
    global result_label
    result_label = tk.Label(task_window, text="Результат: ", font=("Arial", 12))
    result_label.pack()

# Главное окно
root = tk.Tk()
root.title("Практическая работа №4")

# Заголовок и кнопки для выбора заданий
tk.Label(root, text="Выберите задание для расчета:", font=("Arial", 14)).pack(pady=20)
tk.Button(root, text="Задание 1", command=open_task_1).pack(pady=10)
tk.Button(root, text="Задание 2", command=open_task_2).pack(pady=10)

# Запуск приложения
root.mainloop()
