import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def determine_triangle_type(a, b, c):

    # Проверка на существование треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не существует, так как сумма двух сторон \n меньше и/или равна длине третьей стороны."
    elif 0 in [a, b, c]:
        return "Треугольник не существует, так как одна из сторон равна нулю."
    elif a == b == c:
        return "Равносторонний треугольник"
    elif a == b or b == c or a == c:
        return "Равнобедренный треугольник"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Прямоугольный треугольник"
    else:
        sides = sorted([a, b, c])
        largest_side = sides[2]
        other_side1 = sides[0]
        other_side2 = sides[1]
        
        # Вычисление косинуса угла напротив наибольшей стороны
        cos_larg = (other_side1**2 + other_side2**2 - largest_side**2) / (2 * other_side1 * other_side2)
        
        if cos_larg < 0:
            return "Тупоугольный треугольник"
        else:
            return "Остроугольный треугольник"


def on_check_button_click():
    error_entry = []

    try:
        a = float(entry_a.get())
    except ValueError:
        error_entry.append("А")

    try:
        b = float(entry_b.get())
    except ValueError:
        error_entry.append("B")

    try:
        c = float(entry_c.get())
    except ValueError:
        error_entry.append("C")

    if len(error_entry) > 0:
        messagebox.showerror("Ошибка", f"Пожалуйста, введите в поля \'{', '.join(error_entry)}\' числовые значения.")
    else:
        result = determine_triangle_type(a, b, c)
        result_label.config(text=result)
        

def create_context_menu(entry):
    menu = tk.Menu(entry, tearoff=0)
    menu.add_command(label="Копировать", command=lambda: entry.event_generate("<<Copy>>"))
    menu.add_command(label="Вставить", command=lambda: entry.event_generate("<<Paste>>"))
    menu.add_command(label="Вырезать", command=lambda: entry.event_generate("<<Cut>>"))
    return menu

def show_context_menu(event, menu):
    menu.post(event.x_root, event.y_root)


def show_image():
    img = Image.open("circles.png")
    img = img.resize((360, 200), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    
    # Создание нового окна для отображения изображения
    image_window = tk.Toplevel(root)
    image_window.title("well...")
    image_window.resizable(False, False)  

    # Центрирование нового окна
    window_width = 380
    window_height = 220
    screen_width = image_window.winfo_screenwidth()
    screen_height = image_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    image_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Метка для отображения изображения в новом окне
    image_label = tk.Label(image_window, image=img_tk)
    image_label.image = img_tk  # Сохранение ссылки на изображение
    image_label.pack(pady=10)

    image_window.after(7000, image_window.destroy)


# Создание главного окна
root = tk.Tk()
root.iconbitmap("boykisser-spin.ico")
root.title("Определение треугольников")
root.resizable(False, False)  # Запретить изменение размера окна

# Центрирование окна
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Поля ввода для сторон треугольника в горизонтальный ряд
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Сторона A:").grid(row=0, column=0, padx=5)
entry_a = tk.Entry(frame)
entry_a.grid(row=1, column=0, padx=5)

tk.Label(frame, text="Сторона B:").grid(row=0, column=1, padx=5)
entry_b = tk.Entry(frame)
entry_b.grid(row=1, column=1, padx=5)

tk.Label(frame, text="Сторона C:").grid(row=0, column=2, padx=5)
entry_c = tk.Entry(frame)
entry_c.grid(row=1, column=2, padx=5)

# Создание контекстного меню для каждого поля ввода
context_menu_a = create_context_menu(entry_a)
context_menu_b = create_context_menu(entry_b)
context_menu_c = create_context_menu(entry_c)

# Привязка контекстного меню к полям ввода
entry_a.bind("<Button-3>", lambda event: show_context_menu(event, context_menu_a))
entry_b.bind("<Button-3>", lambda event: show_context_menu(event, context_menu_b))
entry_c.bind("<Button-3>", lambda event: show_context_menu(event, context_menu_c))

# Кнопка для проверки типа треугольника
check_button = tk.Button(root, text="Проверить", command=on_check_button_click)
check_button.pack(pady=5)

# Кнопка для вывода круга
circle_button = tk.Button(root, text="🟣", command=show_image)
circle_button.pack(pady=5)

# Метка для отображения результата
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Запуск главного цикла
root.mainloop()