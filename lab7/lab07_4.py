# Поляков Андрей ИУ7-12Б
#
# Вариант 4
#  Замена всех заглавных гласных английских букв на строчные

arr = []
i = 0
length = int(input("Введите длину списка: "))
while i < length:  # Ввод списка
    i += 1
    arr.append(input(f"Введите {i}-й элемент: "))

alph_upper = "AEIOUY"  # Гласные

for i in range(len(arr)):
    line = arr[i]
    new = ""
    for char in line:
        new += char.lower() if char in alph_upper else char  # Замена строчных гласных
    arr[i] = new

print("Результат:")  # Вывод получившегося списка
for (i, el) in enumerate(arr):
    print(f"{i + 1}-й элемент: {el}")
