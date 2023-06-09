# Поляков Андрей Игоревич ИУ7-12Б
#
# Программа для вычисления суммы ряда с точностью до члена ряда е и построения таблицы значений.
# Ряд: y = 2/5 + 1/2*(2/5)^2 + 1/3*(2/5)^3 ... 1/n*(2/5)^n ...

MARKER = "-"  # Маркер для построения таблицы
precision = float(input("Введите точность: "))  # Ввод точности
max_iterations = int(input("Максимальное количество итераций: "))  # Ввод максимального количества итераций
step = float(input("Шаг: "))  # Ввод шага

n = 0  # Номер итерации
s = 0  # Сумма
curr_x = 0.4
print(f"{MARKER * 40}\n| № Итерации |{'t'.center(12)}|{'s'.center(12)}|\n{MARKER * 40}")  # Вывод легенды
while abs(curr_x) < precision and n <= max_iterations:  # Перебор значений последовательности
    n += 1  # Обновление номера итерации
    curr_x = 0.4 ** n / n  # Обновление текущего значения
    if abs(curr_x) < precision:
        break
    s += curr_x  # Обновление суммы
    l_curr = f"{curr_x:.5g}"  # Вычисление длины текущего значения и суммы
    l_s = f"{s:.5g}"
    if (n-1) % step == 0:  # Пошаговый вывод итераций
        print(f"|{str(n).center(12)}|{l_curr.center(12)}|{l_s.center(12)}|")
print(f"{MARKER * 40}")  # Закрытие таблицы

if precision > 0.4:
    print(f"Сумма бесконечного ряда - {precision:.5g}, вычислена за {n} итераций.")
elif n > max_iterations:  # Вывод итоговой суммы и количества итераций
    print(f"Количество итераций превысило максимальное возможное. Сумма: {s:.5g}")
else:
    print(f"Сумма бесконечного ряда - {s:.5g}, вычислена за {n} итераций.")
