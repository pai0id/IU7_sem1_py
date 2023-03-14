# Поляков Андрей ИУ7-12Б
#
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования.

ALPH = ['a', 'e', 'i', 'o', 'u', 'y']

while True:
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))  # Ввод матрицы
    if n <= 0 or m <= 0:
        print("Размером матрицы не может быть отрицательное число или ноль")
    else:
        break
arr = [['.'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        while True:
            arr[i][j] = input(f"Введите {j + 1}-й элемент {i + 1}-й строки:")
            if len(arr[i][j]) == 1:
                break
            else:
                print("Матрица должна содержать только символы")

print("Исходная матрица: ")  # Вывод исходной матрицы
for i in range(n):
    for j in range(m):
        print(f"| {arr[i][j]} |", end='')
    print("")

for i in range(n):
    for j in range(m):
        if arr[i][j] in ALPH or arr[i][j].lower() in ALPH:
            arr[i][j] = '.'

print("Итоговая матрица: ")  # Вывод итоговой матрицы
for i in range(n):
    for j in range(m):
        print(f"| {arr[i][j]} |", end='')
    print("")
