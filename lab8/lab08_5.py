# Поляков Андрей ИУ7-12Б
#
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю

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

max_over = None
min_under = None
for i in range(n):
    for j in range(n):
        if j > i:  # Над главной диагональю
            if max_over is None or arr[i][j] > max_over:
                max_over = arr[i][j]
        if i + j > n - 1:  # Под побочной диагональю
            if min_under is None or arr[i][j] < min_under:
                min_under = arr[i][j]

print("Результат:")
print(f"Максимальное значение над главной диагональю: {max_over}")
print(f"Минимальное значение под побочной диагональю: {min_under}")
