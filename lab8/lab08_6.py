# Поляков Андрей ИУ7-12Б
#
# Выполнить транспонирование квадратной матрицы

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
        x = input(f"Введите {j + 1}-й элемент {i + 1}-й строки:")
        MAX_WIDTH = max(len(x), MAX_WIDTH)
        arr[i].append(int(x))

print("Исходная матрица: ")  # Вывод исходной матрицы
for i in range(n):
    for j in range(n):
        print(f"| {str(arr[i][j]).center(MAX_WIDTH)} |", end='')
    print("")

for i in range(n):
    for j in range(i + 1, n):  # Транспонирование
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print("Результат: ")
for i in range(n):
    for j in range(n):
        print(f"| {str(arr[i][j]).center(MAX_WIDTH)} |", end='')
    print("")
