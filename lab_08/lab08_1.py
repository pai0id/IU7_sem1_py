# Поляков Андрей ИУ7-12Б
#
# Вариант 5
# Найти строку с наибольшим количеством нулевых элементов

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

max_o_cnt = 0
res = -1
for i in range(n):  # Перебор строк
    o_cnt = 0
    for j in range(m):
        if arr[i][j] == 0:  # Подсчет нулевых эл.
            o_cnt += 1
    if o_cnt > max_o_cnt:
        res = i
        max_o_cnt = o_cnt

if res == -1:
    print("Нулевых элементов нет ни в одной строке")
else:
    print(f"Строка {res + 1}")
