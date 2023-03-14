# Поляков Андрей ИУ7-12Б
#
# Вариант 3
# Найти столбец, в котором разница между модулями суммы отрицательных и положительных элементов
# минимальна.

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

min_delta = -1
res_i = -1
for j in range(m):  # Перебор столбцов
    pos_sum = 0
    neg_sum = 0
    for i in range(n):
        if arr[i][j] > 0:
            pos_sum += arr[i][j]  # Сумма положительных
        else:
            neg_sum += arr[i][j]  # Сумма отрицательных
    delta = abs(pos_sum + neg_sum)  # Разница
    if delta < min_delta or min_delta == -1:
        min_delta = delta
        res_i = j

print("Результат:")
print(f"Столбец {res_i + 1}")
