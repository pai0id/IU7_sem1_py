# Поляков Андрей Игоревич ИУ7-12Б
#
# Программа, которая для функций y1 = r^2-cos^2(pi*r) и y2 = r^3-4r^2+2 выведет таблицу
# значений этих функций на некотором отрезке и построит график одной из них.
# используя цикл for
# дополнительно: определить количество значений у1 в диапазоне [-0.5;0.5]

import math as m  # добавление модуля math для cos и pi

WIDTH_OF_GRAPH = 80
r_start = float(input("Введите начальное значение аргумента: "))  # ввод начальной позиции r
r_finish = float(input("Введите конечное значение аргумента: "))  # ввод конечной позиции r
step_r = float(input("Введите шаг: "))  # ввод шага разбиения

r_values_num = int((r_finish-r_start)/step_r+1)  # рассчет количества возможных значений r
max_width_r = len("{:.5g}".format(r_start))  # задание базы для вычисления максимальной возможной длины r
base_y1 = r_start**2-m.cos(m.pi*r_start)**2  # задание начального значения y1 от начальной позиции r
base_y2 = r_start**3-4*r_start**2+2  # задание начального значения y2 от начальной позиции r
max_width_y1 = len("{:.5g}".format(base_y1))  # задание базы для вычисления максимальной возможной длины y1
max_width_y2 = len("{:.5g}".format(base_y2))  # задание базы для вычисления максимальной возможной длины y2
r = r_start
y_max = base_y1  # задание базы для вычисления максимального возможного у1
y_min = base_y1  # задание базы для вычисления минимального возможного у1
for _ in range(r_values_num):  # Первый перебор для вычисления значений, необходимых для посторения таблицы
    max_width_r = max(max_width_r, len("{:.5g}".format(r)))  # Вычисление максимальной длины r
    y1 = r**2-m.cos(m.pi*r)**2  # Рассчет у1 и у2 для текущего r
    y2 = r**3-4*r**2+2
    y_max = max(y_max, y1)  # Вычисление наибольшего и наименьшего у1
    y_min = min(y_min, y1)
    max_width_y1 = max(max_width_y1, len("{:.5g}".format(y1)))  # Вычисление максимальной длины у1 и у2
    max_width_y2 = max(max_width_y2, len("{:.5g}".format(y2)))
    r += step_r  # Переход к следующему r

print("-"*(18+max_width_r+max_width_y2+max_width_y1))  # Рассчет ширины таблицы и вывод легенды
sp = " "
print(f"|   r{sp*max_width_r}|   y1{sp*max_width_y1}|   y2{sp*max_width_y2}|")
print("-"*(18+max_width_r+max_width_y2+max_width_y1))
r = r_start
for _ in range(r_values_num):  # Второй перебор для отрисовки таблицы со значениями r, y1, y2 соответственно
    r_length = len("{:.5g}".format(r))  # Длина текущего r
    y1 = r**2-m.cos(m.pi*r)**2  # Вычисление текущего y1
    y1_length = len("{:.5g}".format(y1))  # Длина текущего у1
    y2 = r**3-4*r**2+2  # Вычисление текущего y2
    y2_length = len("{:.5g}".format(y2))  # Длина текущего у2
    print(
        f"|   {r:.5g}{sp*(max_width_r-r_length+1)}|   "  # Столбец r
        f"{y1:.5g}{sp*(max_width_y1-y1_length+1)}|   "  # Столбец y1
        f"{y2:.5g}{sp*(max_width_y2-y2_length+1)}  |")  # Столбец y2
    r += step_r  # Обновление r
print("-"*(18+max_width_r+max_width_y2+max_width_y1))  # Закрытие таблицы

num_of_marks = int(input("Введите количество засечек: "))  # Ввод количества засечек

pix_step_of_marks = int(WIDTH_OF_GRAPH/(num_of_marks-1))  # Рассчет отступов между засечками в клетках таблицы
step_of_marks = (y_max-y_min)/(num_of_marks-1)  # Рассчет шага разбиения между засечками
y_temp_min = y_min  # Создание копий переменных для использования в построении засечек
y_temp_max = y_max
ox_included = ""
pix_to_ox = 0
if y_min < 0 < y_max:  # Рассчет, входит ли ось абсцисс в диапазон графика
    ox_included = "|"
    pix_to_ox = int(-y_min*WIDTH_OF_GRAPH/(y_max-y_min))  # Рассчет расстояния до оси абсцисс

print(f" {sp*max_width_r}|", end='')
for n in range(num_of_marks):  # Третий перебор для отрисовки засечек
    if n == num_of_marks-1:  # Последняя засечка
        print(f"{y_temp_max:.5g}")
        break
    y_min_size = len(f"{y_temp_min:.5g}")
    print(f"{y_temp_min:.5g}{sp*(pix_step_of_marks-y_min_size)}", end='')  # Вывод каждой засечки и отступа
    y_temp_min += step_of_marks  # Переход к следующему значению

r = r_start
cnt_in_range = 0  # Счетчик для значений у в диапазоне [-0.5;0.5]
for _ in range(r_values_num):
    r_length = len("{:.5g}".format(r))
    y = r**2-m.cos(m.pi*r)**2  # Рассчет у для текущего r
    if -0.5 <= y <= 0.5:
        cnt_in_range += 1  # Обновление счетчика
    pix_to_y = int((y-y_min)*WIDTH_OF_GRAPH/(y_max-y_min))  # Рассчет расстояния от наименьшего у до текущего
    if pix_to_y < pix_to_ox:  # Отрисовка графика и оси абсцисс(при наличии)
        print(
            f"{r:.5g}{sp*(max_width_r-r_length+1)}|{sp*pix_to_y}*{sp*(pix_to_ox-pix_to_y-1)}{ox_included}")
    elif pix_to_y == pix_to_ox:
        print(f"{r:.5g}{sp*(max_width_r-r_length+1)}|{sp*pix_to_y}*")
    else:
        print(f"{r:.5g}{sp*(max_width_r-r_length+1)}|{sp*pix_to_ox}{ox_included}{sp*(pix_to_y-pix_to_ox)}*")
    r += step_r  # Переход к следующему значению
print(f"Количество значений y1 в диапазоне: {cnt_in_range}")  # Вывод счетчика
