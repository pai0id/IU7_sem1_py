# Поляков Андрей ИУ7-12Б
#
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G.

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

MAX_WIDTH_Z = 0
while True:
    n_z = int(input("Введите количество строк матрицы Z: "))
    m_z = int(input("Введите количество столбцов матрицы Z: "))  # Ввод матрицы Z
    if n_z <= 0 or m_z <= 0:
        print("Размером матрицы не может быть отрицательное число или ноль")
    elif n_z != n_d:
        print("Количество строк матриц должно совпадать")
    else:
        break
Z = []
z_sum_lines = [0.0] * n_z  # Массив сумм элементов каждой строки
for i in range(n_z):
    Z.append([])
    for j in range(m_z):
        x = input(f"Введите {j + 1}-й элемент {i + 1}-й строки Z:")
        MAX_WIDTH_Z = max(len(x), MAX_WIDTH_Z)
        z_sum_lines[i] += float(x)
        Z[i].append(float(x))

G = [0] * n_d
mx_g = 0  # Максимальный элемент G
for i in range(n_d):
    for j in range(m_d):
        if D[i][j] > z_sum_lines[i]:
            G[i] += 1
    mx_g = max(G[i], mx_g)

print("\nМатрица Z:")  # Вывод Z
for i in range(n_z):
    for j in range(m_z):
        l_x = f"{Z[i][j]:.5g}"
        print(f"| {l_x.center(MAX_WIDTH_Z)} |", end='')
    print("")

print("\nМатрица D до преобразования:")  # Вывод D
for i in range(n_d):
    for j in range(m_d):
        l_x = f"{D[i][j]:.5g}"
        print(f"| {l_x.center(MAX_WIDTH_D)} |", end='')
    print("")

for i in range(n_d):
    for j in range(m_d):
        D[i][j] *= mx_g
        l_d = f"{D[i][j]:.5g}"
        MAX_WIDTH_D = max(MAX_WIDTH_D, len(l_d))

print("\nМатрица D после преобразования:")
for i in range(n_d):
    for j in range(m_d):
        l_x = f"{D[i][j]:.5g}"
        print(f"| {l_x.center(MAX_WIDTH_D)} |", end='')
    print("")

print("\nМассив G:")
for i in range(n_d):
    print(f"Количесво в строке {i + 1}: {G[i]}")
