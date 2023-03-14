# Поляков Андрей ИУ7-12Б
#
# Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.

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

max_neg_cnt = 0
min_neg_cnt = 0
res_max = -1
res_min = -1
for i in range(n):
    neg_cnt = 0
    for j in range(m):
        if arr[i][j] < 0:
            neg_cnt += 1  # Количество отрицательных в текущей строке
    if neg_cnt > max_neg_cnt:  # Запись максимального
        res_max = i
        max_neg_cnt = neg_cnt
    if (neg_cnt < min_neg_cnt or min_neg_cnt == 0) and neg_cnt != 0:  # Запись минимального
        res_min = i
        min_neg_cnt = neg_cnt
if res_max == -1:
    print("Отрицательных элементов нет ни в одной строке")
elif res_max == res_min:
    print("Всего одна строка с отрицательными элементами")
else:
    for j in range(m):  # Перестановка элементов
        arr[res_min][j], arr[res_max][j] = arr[res_max][j], arr[res_min][j]

print("Результат: ")
for i in range(n):
    for j in range(m):
        print(f"| {str(arr[i][j]).center(MAX_WIDTH)} |", end='')
    print("")
