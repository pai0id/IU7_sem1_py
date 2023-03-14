# Поляков Андрей ИУ7-12Б
#
# Поменять местами первый нулевой и минимальный отрицательный элементы

arr = []
i = 0
while True:  # Ввод списка
    i += 1
    el = input(f"Введите {i}-й элемент: ")
    if el:
        arr.append(int(el))
    else:
        break

min_neg = 1
f_min_neg_index = -1
null_index = -1
o_in_seq = False
for i in range(len(arr)):  # Нахождение минимального отрицательного элемента
    if arr[i] == 0 and not o_in_seq:
        null_index = i
        o_in_seq = True
    elif arr[i] < 0 and arr[i] < min_neg:  # Сохранение индекса минимального отрицательного элемента
        min_neg = arr[i]
        f_min_neg_index = i

if f_min_neg_index == -1:
    print(f"Отрицательных элементов нет")
elif not o_in_seq:
    print(f"Нулевого элемента нет")
else:  # Перестановка
    arr[null_index], arr[f_min_neg_index] = arr[f_min_neg_index], arr[null_index]
    print("Результат:")
    for (i, el) in enumerate(arr):
        print(f"{i + 1}-й элемент: {el}")
