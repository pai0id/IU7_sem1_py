# Поляков Андрей ИУ7-12Б
#
# Найти наиболее длинную непрерывную последовательность,в которой каждое число,
# начиная с 3-го, являются суммой двух предыдущих.

arr = []
i = 0
while True:  # Ввод списка
    i += 1
    el = input(f"Введите {i}-й элемент: ")
    if el:
        arr.append(int(el))
    else:
        break

result_start_index = -1  # Длина максимальной подпоследовательности
temp_res_start_index = 2  # Длина текущей подпоследовательности
res_cnt = 0  # Длина наибольшей последовательности
curr_cnt = 0  # Длина текущей последовательности
for i in range(2, len(arr)):
    if arr[i - 2] + arr[i - 1] == arr[i]:  # Текущее число принадлежит
        curr_cnt += 1  # Увеличение длины
    else:
        if curr_cnt > res_cnt:  # Поиск наибольшей последовательности
            result_start_index = temp_res_start_index
            res_cnt = curr_cnt
        temp_res_start_index = i+1  # Обновление переменных
        curr_cnt = 0
if curr_cnt > res_cnt:  # Поиск наибольшей последовательности
    result_start_index = temp_res_start_index
    res_cnt = curr_cnt

print("Результат:")
if result_start_index == -1:  # Если no result
    print("Последовательность отсутствует")
else:  # Вывод полученной последовательности
    num = 0
    for i in range(result_start_index - 2, result_start_index + res_cnt):
        print(f"{num + 1}-й элемент подпоследовательности: {arr[i]}")
        num += 1
