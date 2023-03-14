# у = cosx - 1
# график

import math as m

WIDTH_GRAPH = 60
EPS = 0.000000000000001
x_start = float(input("Начaло: "))
x_finish = float(input("Конец: "))
step = float(input("Шаг: "))

x_val_num = int((x_finish - x_start) / step + 1)
y = m.cos(x_start) - 1
max_x_l = len(f"{x_start:.5g}")
max_y_l = len(f"{y:.5g}")
y_max = y
y_min = y
x = x_start
for _ in range(x_val_num):
    if -EPS < x < EPS:
        x = 0
    y = m.cos(x) - 1
    max_x_l = max(max_x_l, len(f"{x:.5g}"))
    max_y_l = max(max_y_l, len(f"{y:.5g}"))
    y_max = max(y_max, y)
    y_min = min(y_min, y)
    x += step
oy_in = ""
pix_to_oy = 0
if y_min <= 0 <= y_max:
    oy_in = "|"
    pix_to_oy = int(-y_min * WIDTH_GRAPH / (y_max - y_min))
sp = " "
mark = "-"
l_min_y = len(f"{y_min:.0g}")
l_max_y = len(f"{y_max:.0g}")
print(f"{sp * max_x_l} | {y_min:.0g}{sp * (WIDTH_GRAPH - l_min_y - l_max_y - 1)}{y_max:.0g}")
print(f"{mark * (WIDTH_GRAPH + max_x_l + 2)}")
x = x_start
for _ in range(x_val_num):
    if abs(x) < EPS:
        x = 0
    y = m.cos(x) - 1
    l_curr_x = len(f"{x:.5g}")
    print(f"{x:.5g}{sp * (max_x_l - l_curr_x)} |", end='')
    pix_to_y = int((y - y_min) * WIDTH_GRAPH / (y_max - y_min))
    if pix_to_y < pix_to_oy:
        print(f"{sp * pix_to_y}*{sp * (pix_to_oy - pix_to_y - 1)}{oy_in}")
    elif pix_to_y == pix_to_oy:
        print(f"{sp * pix_to_y}*")
    else:
        print(f"{sp * pix_to_oy}{oy_in}{sp * (pix_to_y - pix_to_oy - 1)}*")
    x += step
