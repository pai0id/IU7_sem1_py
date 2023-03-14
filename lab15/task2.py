# Поляков Андрей ИУ7-12Б
# После каждого нечетного числа добавить его удвоенное значение

import struct
import tools

frmt = "i"
size = struct.calcsize(frmt)

while True:
    try:
        file_name = input("Введите адрес файла: ")
        f = open(file_name, 'wb')
        num = int(input("Введите количество записей: "))
    except ValueError:
        print("Пожалуйста введите целое число")
        continue
    except Exception:
        print("Некорректный путь к файлу")
        continue
    else:
        if num <= 0:
            print("Количество записей должно быть больше нуля")
            continue
        break

mx_l = tools.create(f, num, frmt)
f = open(file_name, 'rb')
tools.output(f, frmt, size, mx_l)
f.close()
f = open(file_name, 'r+b')
step = 0
x = f.read(size)
while x:
    x = struct.unpack(frmt, x)[0]
    if x % 2 == 1:
        step += 1
    x = f.read(size)
for _ in range(step):
    f.write(struct.pack(frmt, 0))
used = False
for _ in range(num + step):
    f.seek((-step - 1) * size, 1)
    tmp = struct.unpack(frmt, f.read(size))[0]
    f.seek((step - 1) * size, 1)
    if tmp % 2 == 1 and not used:
        f.write(struct.pack(frmt, tmp * 2))
        used = True
        step -= 1
    else:
        f.write(struct.pack(frmt, tmp))
        used = False
    f.seek(-size, 1)

print("Результат: ")
f = open(file_name, 'rb')
tools.output(f, frmt, size, mx_l)
f.close()
