# Поляков Андрей ИУ7-12Б
#
# Найти значение K-го экстремума в списке

arr = []
i = 0
while True:  # Ввод списка
    i += 1
    el = input(f"Введите {i}-й элемент: ")
    if el:
        arr.append(int(el))
    else:
        break
k = int(input("Номер экстремума: "))

index = 1
cnt = 0
for i in range(index, len(arr) - 1):
    curr = arr[i]  # Текущее рассматриваемое число
    prev = arr[i - 1]  # Предыдущее число
    nxt = arr[i + 1]  # Следующее число
    if (curr > nxt and curr > prev) or (curr < nxt and curr < prev):  # Проверка, является ли число экстремумом
        cnt += 1
    if cnt == k:  # Вывод экстремума №К
        print(f"{k}-й экстремум: {curr}")
        break  # Выход из цикла
if cnt < k:
    print(f"{k} экстремума нет")
