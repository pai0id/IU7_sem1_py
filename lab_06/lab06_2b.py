# Поляков Андрей ИУ7-12Б
#
# Удалить элемент с заданным индексом алгоритмически

arr = []
i = 0
while True:  # Ввод списка
    i += 1
    el = input(f"Введите {i}-й элемент: ")
    if el:
        arr.append(int(el))
    else:
        break
index = int(input("Индекс удаления: "))  # Ввод индекса числа, которое надо удалить

for i in range(index, len(arr) - 1):  # Поочередный сдвиг элементов
    arr[i] = arr[i + 1]
arr.pop()  # Уменьшение длины списка

print("Результат:")  # Вывод получившегося списка
for (i, el) in enumerate(arr):
    print(f"{i + 1}-й элемент: {el}")
