# Поляков Андрей Игоревич ИУ7-12Б
# Список целых чисел
# Заменить макс. эл. на среднее ар. отр. чисел

arr = []
i = 0
while True:
    i += 1
    el = input(f"Введите {i}-й элемент: ")
    if el:
        arr.append(int(el))
    else:
        break

sum_neg_nums = 0
cnt_neg_nums = 0
max_el = arr[0]
i_max_el = 0
for i in range(len(arr)):
    if arr[i] < 0:
        cnt_neg_nums += 1
        sum_neg_nums += arr[i]
    if arr[i] > max_el:
        max_el = arr[i]
        i_max_el = i
# mid_neg = 0 if cnt_neg_nums == 0 else sum_neg_nums // cnt_neg_nums
if cnt_neg_nums == 0:
    print("Отрицательных чисел нет")
else:
    mid_neg = sum_neg_nums // cnt_neg_nums
    arr[i_max_el] = mid_neg
print("Результат:")
for (i, el) in enumerate(arr):
    print(f"{i + 1}-й элемент: {el}")
