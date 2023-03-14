# Поляков Андрей ИУ7-12Б
#
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки.

MAX_WIDTH = 0
while True:
    n = int(input("Введите количество строк и столбцов матрицы: "))  # Ввод матрицы
    if n <= 0:
        print("Размером матрицы не может быть отрицательное число или ноль")
    else:
        break
arr = []
for i in range(n):
    arr.append([])
    for j in range(n):
        x = input(f"Введите {j + 1}-й элемент {i + 1}-й строки: ")
        MAX_WIDTH = max(len(x), MAX_WIDTH)
        arr[i].append(int(x))

print("Исходная матрица: ")  # Вывод исходной матрицы
for i in range(n):
    for j in range(n):
        print(f"| {str(arr[i][j]).center(MAX_WIDTH)} |", end='')
    print("")

print("Промежуточная матрица:")
for i in range(n // 2):
    for j in range(i, n - 1 - i):  # Поворот первых n-1 элементов строки, исключая уже повернутые
        arr[j][n - 1 - i], arr[n - 1 - i][n - 1 - j], arr[n - 1 - j][i], arr[i][j] = \
            arr[i][j], arr[j][n - 1 - i], arr[n - 1 - i][n - 1 - j], arr[n - 1 - j][i]

for i in range(n):  # Вывод
    for j in range(n):
        print(f"| {str(arr[i][j]).center(MAX_WIDTH)} |", end='')
    print("")

print("Итоговая матрица:")
for i in range(n // 2):
    for j in range(i, n - 1 - i):  # Поворот первых n-1 элементов строки, исключая уже повернутые
        arr[n - 1 - j][i], arr[n - 1 - i][n - 1 - j], arr[j][n - 1 - i], arr[i][j] = \
            arr[i][j], arr[n - 1 - j][i], arr[n - 1 - i][n - 1 - j], arr[j][n - 1 - i]

for i in range(n):  # Вывод
    for j in range(n):
        print(f"| {str(arr[i][j]).center(MAX_WIDTH)} |", end='')
    print("")
