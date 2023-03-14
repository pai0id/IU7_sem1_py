# Медиана из наименьшего
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

a1 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
a2 = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
a3 = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
if a1 + a2 > a3 and a2 + a3 > a1 and a3 + a1 > a2:
    s_max = 2*a1**2 + 2*a2**2 + 2*a3**2 - 2 * min(a1,a2,a3)**2
    m = ((s_max - min(a1,a2,a3)**2)**0.5)/2
    print(m)
else:
    print("Треугольник не существует")
