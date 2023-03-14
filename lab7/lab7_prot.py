# Поляков Андрей Игоревич ИУ7-12Б
# Список строк
# Найти строку содержащую наиб. кол-во слов, разд. пробелами

arr = []
length = int(input("Введите длину списка строк: "))
for i in range(length):
    arr.append(input(f"Строка {i+1}: "))

l_res = ""
max_wrd_cnt = -1
for line in arr:
    curr_wrd_cnt = len(line.split())
    if curr_wrd_cnt > max_wrd_cnt:
        max_wrd_cnt = curr_wrd_cnt
        l_res = line

print(f'Результат: "{l_res}"')
# Список целых чисел. Заменить макс эл на среднее ар отр чисел