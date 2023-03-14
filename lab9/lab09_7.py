# Поляков Андрей ИУ7-12Б
#
# Ввести трёхмерный массив, вывести из него i-й срез по второму индексу

print("Размеры массива:")
X = int(input("X:"))  # Ввод размеров массива
Y = int(input("Y:"))
Z = int(input("Z:"))
MAX_LEN = 0
arr = [[[0.0 for k in range(Z)] for j in range(Y)] for i in range(X)]  # Создание массива
for i in range(X):
    for j in range(Y):
        for k in range(Z):
            x = input(f"X{i+1} Y{j+1} Z{k+1}: ")  # Ввод элементов
            MAX_LEN = max(MAX_LEN, len(x))
            arr[i][j][k] = float(x)
while True:
    index = int(input("Индекс Y среза: ")) - 1
    if -1 > index > Y-1:
        print("Индекс за граеницами массива")
    else:
        break

for i in range(X):  # Вывод среза
    for k in range(Z):
        print(f"| {str(arr[i][index][k]).center(MAX_LEN)} |", end='')
    print('')
