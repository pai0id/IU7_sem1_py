# Поляков Андрей ИУ7-12Б
#
# Добавить элемент в заданное место списка (по индексу), используя методы python

arr = []
i = 0
while True:  # Ввод списка
    i += 1
    el = input(f"Введите {i}-й элемент: ")
    if el:
        arr.append(int(el))
    else:
        break
x = input("Добавить: ")  # Ввод числа, которое нужно добавить
index = int(input("Индекс: "))  # Ввод индекса этого числа

arr.insert(index, x)  # Добавление с помощью метода insert

print("Результат:")  # Вывод получившегося списка
for (i, el) in enumerate(arr):
    print(f"{i + 1}-й элемент: {el}")
