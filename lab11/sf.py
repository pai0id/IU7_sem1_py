# Поляков Андрей ИУ7-12Б
#
# Демонстрация работы метода сортировки пузырьком с флагом


import random as rnd  # Подключение необходимых модулей
import time as tm


def sort_alg(arr):  # Алгоритм сортировки пузырьком с флагом
    was_swapped = True  # флаг
    cnt = 0
    t = tm.time()
    while was_swapped:
        was_swapped = False
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                cnt += 1
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                was_swapped = True
    t = f"{(tm.time() - t):.5g}"
    return t, cnt


def array_creation(length):  # Функция создает 3 вида массива заданной длины, сортирует из и возвращает нужные данные
    arr1 = [0] * length
    for index in range(length):
        arr1[index] = index
    arr2 = [0] * length
    for index in range(length):
        arr2[index] = int(rnd.randint(-127, 128))
    arr3 = [0] * length
    for index in range(length):
        arr3[index] = length - index
    t1, k1 = sort_alg(arr1)  # время сортировки и количество перестановок
    t2, k2 = sort_alg(arr2)
    t3, k3 = sort_alg(arr3)
    return (t1, k1), (t2, k2), (t3, k3)


def output(num, row):  # Вывод данных по рядам
    print(f"{num[0][row][0].center(10)}|{str(num[0][row][1]).center(14)}|", end='')
    print(f"{num[1][row][0].center(10)}|{str(num[1][row][1]).center(14)}|", end='')
    print(f"{num[2][row][0].center(10)}|{str(num[2][row][1]).center(14)}|")


while True:  # Ввод с проверкой
    try:
        n = int(input("Длина массива 1: "))
        arr_p = [0] * n
        for ind in range(n):
            arr_p[ind] = int(input(f"Элемент {ind + 1}: "))
        n1 = int(input("Длина N1: "))
        n2 = int(input("Длина N2: "))
        n3 = int(input("Длина N3: "))
        if n <= 0 or n1 <= 0 or n2 <= 0 or n3 <= 0:
            print("Длина должна быть больше нуля")
            break
    except ValueError:
        print("Пожалуйста, вводите целые числа\n")
    else:
        break

sort_alg(arr_p)  # Сортировка пользовательского массива
print("Отсортированный пользовательский алгоритм:")  # вывод
for i in range(n):
    print(f"{i + 1}-й элемент: {arr_p[i]}")

ns = array_creation(n1), array_creation(n2), array_creation(n3)  # вычисление всех нужных значений

sep = '-'
sp = ' '
print(f"{sep * 98}")  # Вывод таблицы
print(f"{sp * 19}|{str(n1).center(25)}|{str(n2).center(25)}|{str(n3).center(25)}|")
print(f"{sep * 98}")
print(f"{sp * 19}|{' Время(с) | Перестановки |' * 3}")
print(f"{sep * 98}")
print(f"Упорядоченный      |", end='')
output(ns, 0)
print(f"{sep * 98}")
print(f"Случайный          |", end='')
output(ns, 1)
print(f"{sep * 98}")
print(f"Упорядоченный      |", end='')
output(ns, 2)
print(f"в обратном порядке |{sp * 77}|")
print(f"{sep * 98}")
