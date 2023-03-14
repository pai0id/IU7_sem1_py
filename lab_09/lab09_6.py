# Поляков Андрей ИУ7-12Б
#
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V.

while True:
    n = int(input("Введите количество строк матриц А и В: "))
    m = int(input("Введите количество столбцов матриц А и В: "))  # Ввод матриц
    if n <= 0 or m <= 0:
        print("Размером матрицы не может быть отрицательное число или ноль")
    else:
        break

A = []
MAX_WIDTH_A = 0
for i in range(n):
    A.append([])
    for j in range(m):
        x = input(f"Введите {j + 1}-й элемент {i + 1}-й строки A:")
        MAX_WIDTH_A = max(len(x), MAX_WIDTH_A)
        A[i].append(float(x))
print("")
B = []
MAX_WIDTH_B = 0
for i in range(n):
    B.append([])
    for j in range(m):
        x = input(f"Введите {j + 1}-й элемент {i + 1}-й строки D:")
        MAX_WIDTH_B = max(len(x), MAX_WIDTH_B)
        B[i].append(float(x))

V = [0.0] * m  # создание массива V
C = [[0.0] * m for i in range(n)]
MAX_WIDTH_C = 0
for j in range(m):
    for i in range(n):
        C[i][j] = A[i][j] * B[i][j]
        l_c = f"{C[i][j]:.5g}"
        MAX_WIDTH_C = max(MAX_WIDTH_C, len(l_c))
        V[j] += C[i][j]

print("\nМатрица A:")  # Вывод A
for i in range(n):
    for j in range(m):
        l_a = f"{A[i][j]:.5g}"
        print(f"| {l_a.center(MAX_WIDTH_A)} |", end='')
    print("")

print("\nМатрица B:")  # Вывод B
for i in range(n):
    for j in range(m):
        l_b = f"{B[i][j]:.5g}"
        print(f"| {l_b.center(MAX_WIDTH_B)} |", end='')
    print("")

print("\nМатрица C:")  # Вывод C
for i in range(n):
    for j in range(m):
        l_c = f"{C[i][j]:.5g}"
        print(f"| {l_c.center(MAX_WIDTH_C)} |", end='')
    print("")

print("\nМассив V:")
for i in range(m):
    print(f"Элемент {i+1}: {V[i]:.5g}")
