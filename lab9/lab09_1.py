# Поляков Андрей ИУ7-12Б
#
# Даны массивы D и F. Сформировать матрицу A по формуле ajk = sin(dj+fk)
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и рядом столбцы AV и L.

import math as mth  # Подключение модуля math для sin

while True:
    n = int(input("Длина массива D: "))  # Ввод длины массива D
    if n > 0:
        break
    else:
        print("Длина массива должна быть больше нуля")
D = [0.0] * n  # Создание массива D
for i in range(n):
    D[i] = float(input(f"{i + 1}-й элемент D: "))  # Заполнение массива

while True:
    m = int(input("Длина массива F: "))  # Ввод длины массива F
    if m > 0:
        break
    else:
        print("Длина массива должна быть больше нуля")
F = [0.0] * m  # Создание массива F
for i in range(m):
    F[i] = float(input(f"{i + 1}-й элемент F: "))  # Заполнение массива

m_length_el = 0  # Для вычисления максимальной длины элемента матрицы
m_length_AV = 0  # Для вычисления максимальной длины среднего арифметического строки
A = [[0.0] * m for i in range(n)]  # Создание матрицы
AV = []  # Создание массива средних арифметических
L = []  # Создание массива количеств элементов, меньших среднего арифметического в строках
for i in range(n):
    s_line = 0  # Сумма положительных
    cnt_pos = 0  # Количество положительных
    for j in range(m):
        x = float(mth.sin(D[i] + F[j]))  # Вычисление текущего элемента матрицы
        A[i][j] = x
        if x > 0:
            s_line += x
            cnt_pos += 1
        l_x = f"{A[i][j]:.5g}"
        m_length_el = max(m_length_el, len(l_x))
    if s_line != 0:
        AV.append(s_line / cnt_pos)  # Среднее арифметическое положительных
        l_av = f"{AV[i]:.5g}"
        m_length_AV = max(m_length_AV, len(l_av))
        cnt_less_av = 0  # Количество элементов, меньших среднего арифметического
        for j in range(m):
            if A[i][j] < AV[i]:
                cnt_less_av += 1
        L.append(cnt_less_av)
    else:
        AV.append("-")
        m_length_AV = max(m_length_AV, 1)
        L.append("-")

sp = " "
print(f"A{sp * ((4 + m_length_el) * m)}# AV{sp * (m_length_AV - 1)}# L")  # Вывод легенды
for i in range(n):
    for j in range(m):  # Вывод матрицы
        x = f"{A[i][j]:.5g}"
        print(f"| {x.center(m_length_el)} |", end='')
    l_av = f"{AV[i]:.5g}" if AV[i] != "-" else "-"
    print(f" # {l_av.center(m_length_AV)} # {L[i]}")  # Вывод массивов D и F
