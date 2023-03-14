# Поляков Андрей ИУ7-12Б
#
# Вариант 5
# Удалить все отрицательные элементы целочисленного списка за один цикл.

arr = []
i = 0
while True:  # Ввод списка
    i += 1
    el = input(f"Введите {i}-й элемент: ")
    if el:
        arr.append(int(el))
    else:
        break

del_step = 0
index = 0
while index < len(arr):  # Поочередный сдвиг элементов
    if arr[index] < 0:
        del_step += 1
        del (arr[index])
        index -= 1
    index += 1

print("Результат:")  # Вывод получившегося списка
if not arr:
    print("Массив пуст")
else:
    for (i, el) in enumerate(arr):
        print(f"{i + 1}-й элемент: {el}")
