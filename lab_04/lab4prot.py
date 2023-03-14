# y = tg(x/2)
# Андрей Поляков ИУ7-12Б

import math as m

WIDTH = 50
EPS = 1e-10
x_start = float(input("Начало: "))
x_finish = float(input("Конец: "))
step = float(input("Шаг: "))

x_val_num = int((x_finish - x_start) / step + 1)
x = x_start
if m.cos(x / 2) != 0:
    y = m.tan(x / 2)
else:
    x += step
    y = m.tan(x / 2)
max_x_l = len(f"{x:.5g}")
max_y_l = len(f"{y:.5g}")
y_max = y
y_min = y
for _ in range(x_val_num):
    if abs(x) < EPS:
        x = 0
    if m.cos(x / 2) != 0:
        y = m.tan(x / 2)
    else:
        x += step
        y = m.tan(x / 2)
    max_x_l = max(max_x_l, len(f"{x:.5g}"))
    max_y_l = max(max_y_l, len(f"{y:.5g}"))
    y_max = max(y, y_max)
    y_min = min(y, y_min)
    x += step
oy_in = ""
pix_to_oy = 0
if y_min <= 0 <= y_max:
    oy_in = "|"
    pix_to_oy = int(-y_min * WIDTH / (y_max - y_min))
sp = " "
mark = "-"
l_min_y = len(f"{y_min:.5g}")
l_max_y = len(f"{y_max:.5g}")
print(f"{sp * max_x_l} |{y_min:.5g}{sp * (WIDTH - l_min_y - l_max_y)}{y_max:.5g}")
print(f"{mark * (WIDTH + max_x_l + 2)}")
x = x_start
for _ in range(x_val_num):
    if abs(x) < EPS:
        x = 0
    if m.cos(x / 2) != 0:
        y = m.tan(x / 2)
    else:
        x += step
        y = m.tan(x / 2)
    l_curr_x = len(f"{x:.5g}")
    print(f"{x:.5g}{sp * (max_x_l - l_curr_x)} |", end='')
    pix_to_y = int((y - y_min) * WIDTH / (y_max - y_min))
    if pix_to_y < pix_to_oy:
        print(f"{sp * pix_to_y}*{sp * (pix_to_oy - pix_to_y -1)}{oy_in}")
    elif pix_to_y == pix_to_oy:
        print(f"{sp * pix_to_y}*")
    else:
        print(f"{sp * pix_to_oy}{oy_in}{sp * (pix_to_y - pix_to_oy -1)}*")
    x+=step