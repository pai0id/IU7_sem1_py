# Поляков Андрей ИУ7 - 12Б
# Метод вставок с бинарным поиском

n = int(input("Введите длину массива: "))  # Ввод массива
arr = [0] * n
for i in range(n):
    arr[i] = int(input(f"{i + 1}-й элемент: "))

for i in range(1, n):
    tmp = arr[i]
    lo, hi = 0, i
    while lo < hi:  # Бинарный поиск нужного элемента в отсортированной части массива
        mid = (hi + lo) // 2
        if tmp < arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    for j in range(i, lo, -1):  # Сдвиг и вставка
        arr[j] = arr[j - 1]
    arr[lo] = tmp

print("\nОтсортированный массив:")  # Вывод массива
for i in range(n):
    print(f"{i + 1}-й элемент: {arr[i]}")
