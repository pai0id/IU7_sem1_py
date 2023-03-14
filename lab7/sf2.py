# Поляков Андрей ИУ7-12Б
#
# Вариант 3
# После каждого нечетного элемента целочисленного списка добавить его удвоенное значение.

arr = []
i = 0
while True:  # Ввод списка
    i += 1
    el = input(f"Введите {i}-й элемент: ")
    if el:
        arr.append(int(el))
    else:
        break

step = 0
for x in arr:
    if x % 2 == 1:
        step += 1
        arr.append(0)
used = False
for index in range(len(arr) - 1, -1, -1):
    if arr[index - step] % 2 == 1 and not used:
        arr[index] = arr[index - step] * 2
        used = True
        step -= 1
    else:
        arr[index] = arr[index - step]
        used = False

print("Результат:")  # Вывод получившегося списка
for (i, el) in enumerate(arr):
    print(f"{i + 1}-й элемент: {el}")
