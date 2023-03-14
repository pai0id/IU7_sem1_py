from math import sqrt

x1, y1 = [int(i) for i in input("Введите координаты первой точки через пробел: ").split()]
x2, y2 = [int(i) for i in input("Введите координаты второй точки через пробел: ").split()]
x3, y3 = [int(i) for i in input("Введите координаты третьей точки через пробел: ").split()]

side1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
side2 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
side3 = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)

minside = min(side1, side2, side3)
maxside = max(side1, side2, side3)
avside = (side1 + side2 + side3) - maxside - minside
if abs(minside + avside - maxside) < 0.01:
    print("Не треугольник")
    exit()

max_part = maxside * avside / (minside + avside)
mincos = (avside**2 + maxside**2 - minside**2) / (2 * avside * maxside)
biss = sqrt(avside ** 2 + max_part ** 2 - 2 * avside * max_part * mincos)
print(f"Биссектриса наибольшего угла равна: {biss:.7gw}")