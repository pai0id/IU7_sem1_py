# Поляков Андрей ИУ7-12Б
#
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений.

MAX_WIDTH_D = 0
while True:
    n_d = int(input("Введите количество строк матрицы D: "))
    m_d = int(input("Введите количество столбцов матрицы D: "))  # Ввод матрицы D
    if n_d <= 0 or m_d <= 0:
        print("Размером матрицы не может быть отрицательное число или ноль")
    else:
        break
D = []
for i in range(n_d):
    D.append([])
    for j in range(m_d):
        x = input(f"Введите {j + 1}-й элемент {i + 1}-й строки D:")
        MAX_WIDTH_D = max(len(x), MAX_WIDTH_D)
        D[i].append(float(x))

while True:
    m_i = int(input("Длина массива I: "))  # Ввод длины массива I
    if m_i > 0:
        break
    else:
        print("Длина массива должна быть больше нуля")
list_I = [0] * m_i  # Создание массива I
for i in range(m_i):
    while True:
        list_I[i] = int(input(f"{i + 1}-й элемент I: "))  # Заполнение массива
        if n_d >= list_I[i] > 0:
            break
        else:
            print("Такой строки нет в матрице")

R = []
s_r = 0
for i in list_I:
    mx = D[i-1][0]
    for j in range(m_d):
        mx = max(mx, D[i-1][j])  # Вычисление максимального элемента строки
    s_r += mx
    R.append(mx)
aver = s_r / m_i

print("\nМатрица D:")  # Вывод D
for i in range(n_d):
    for j in range(m_d):
        l_d = f"{D[i][j]:.5g}"
        print(f"| {l_d.center(MAX_WIDTH_D)} |", end='')
    print("")

print("\nМассив I:")
for i in range(m_i):
    print(f"Элемент {i+1}: {list_I[i]}")

print("\nМассив R:")
for i in range(m_i):
    print(f"Элемент {i+1}: {R[i]:.5g}")

print(f"\nСреднее арифметическое: {aver:.5g}")
