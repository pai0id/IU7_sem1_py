# Поляков Андрей ИУ7-12Б
#
# Дана квадратная символьная матрица, повернуть на 180

while True:
    n = int(input("Введите размер матрицы: "))
    if n > 0:
        break
    else:
        print("Размер матрицы должен быть больше нуля")
arr = [['-'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        while True:
            arr[i][j] = input(f"{i+1} строка, {j+1} столбец: ")
            if len(arr[i][j]) != 1:
                print("Строка может содержать только символы")
            else:
                break

print("Матрица до изменений:")
for i in range(n):
    for j in range(n):
        print(f"| {arr[i][j]} |", end='')
    print('')

arr = arr[::-1]
for i in range(n):  # Поворот на 180
    arr[i] = arr[i][::-1]

print("Итоговая матрица:")
for i in range(n):
    for j in range(n):
        print(f"| {arr[i][j]} |", end='')
    print('')
