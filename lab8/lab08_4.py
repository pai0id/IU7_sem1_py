# Поляков Андрей ИУ7-12Б
#
# Переставить местами столбцы с максимальной и минимальной суммой элементов.

MAX_WIDTH = 0
while True:
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))  # Ввод матрицы
    if n <= 0 or m <= 0:
        print("Размером матрицы не может быть отрицательное число или ноль")
    else:
        break
arr = []
for i in range(n):
    arr.append([])
    for j in range(m):
        x = input(f"Введите {j + 1}-й элемент {i + 1}-й строки:")
        MAX_WIDTH = max(len(x), MAX_WIDTH)
        arr[i].append(int(x))

print("Исходная матрица: ")  # Вывод исходной матрицы
for i in range(n):
    for j in range(m):
        print(f"| {str(arr[i][j]).center(MAX_WIDTH)} |", end='')
    print("")

min_sum = None
max_sum = None
min_j = -1
max_j = -1
for j in range(m):
    sum_j = 0
    for i in range(n):
        sum_j += arr[i][j]
    if max_sum is None or sum_j > max_sum:  # Максимальная сумма элементов
        max_j = j
        max_sum = sum_j
    if min_sum is None or sum_j < min_sum:  # Миниммальная сумма элементов
        min_j = j
        min_sum = sum_j
for i in range(n):  # Перестановкка столбцов
    arr[i][min_j], arr[i][max_j] = arr[i][max_j], arr[i][min_j]

print("Результат: ")
for i in range(n):
    for j in range(m):
        print(f"| {str(arr[i][j]).center(MAX_WIDTH)} |", end='')
    print("")
