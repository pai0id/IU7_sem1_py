# Поляков Андрей Игоревич ИУ7-12Б
# Вариант 98

EPS = float(input("Введите точность: "))
x = float(input("Введите х: "))

n = 1
curr_x = 1
s = 1
print(f"{n}-я итерация: {curr_x:.7g}")
while True:
    n += 1
    curr_x *= -x ** 2 / (n - 1)
    if abs(curr_x) < EPS:
        break
    s += curr_x
    print(f"{n}-я итерация: {curr_x:.7g}")

print(f"Сумма ряда: {s:.7g}")
