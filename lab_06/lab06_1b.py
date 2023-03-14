# Поляков Андрей ИУ7-12Б
#
# Добавить элемент в заданное место списка (по индексу) алгоритмически

arr = []
i = 0
while True:  # Ввод списка
    i += 1
    el = input(f"Введите {i}-й элемент: ")
    if el:
        arr.append(int(el))
    else:
        break
new_x = input("Добавить: ")  # Ввод числа, которое нужно добавить
index = int(input("Индекс: "))  # Ввод индекса этого числа

arr.append(None)  # Добавление пустого элемента в конец списка
for i in range(len(arr) - 1, index, -1):  # Поочередный сдвиг элементов
    arr[i] = arr[i-1]
arr[index] = new_x

print("Результат:")  # Вывод получившегося списка
for (i, el) in enumerate(arr):
    print(f"{i + 1}-й элемент: {el}")
