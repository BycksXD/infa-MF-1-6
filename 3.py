# Заданные значения x и y
x = 2
y = 3

# Вычисление max и min с использованием функций max() и min()
max_val = max(x + 6*y, x - y)
min_val = min(x + y, x - 3*y)

# Вычисление u
if min_val != 0:
    u = max_val / min_val
    print(f"Максимальное значение: {max_val}")
    print(f"Минимальное значение: {min_val}")
    print(f"Значение u: {u}")
else:
    print("Деление на ноль!")
