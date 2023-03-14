# Поляков Андрей ИУ7-12Б
#
# Вариант 5
# Поиск элемента наибольшей длины, не содержащего цифр.

arr = []
i = 0
length = int(input("Введите длину списка: "))
while i < length:  # Ввод списка
    i += 1
    arr.append(input(f"Введите {i}-й элемент: "))

max_l = 0
result = ""
for line in arr:
    if len(line) > max_l:
        for x in line:
            if x.isdigit():
                break
        else:
            result = line
            max_l = len(line)

print(f"Результат: {result}")
