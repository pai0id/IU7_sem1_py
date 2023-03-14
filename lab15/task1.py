# Поляков Андрей ИУ7-12Б
# Удалить отрицательные числа

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
x = f.read(size)
changes = False
back_seek_l = 1
front_seek_l = 0
cnt = 0
while x:
    x = struct.unpack(frmt, x)[0]
    if x < 0:
        if not changes:
            changes = True
        back_seek_l += 1
        front_seek_l += 1
        cnt += 1
    elif changes:
        f.seek(-size * back_seek_l, 1)
        f.write(struct.pack(frmt, x))
        f.seek(size * front_seek_l, 1)
    x = f.read(size)
f.seek(-size * cnt,2)
f.truncate()

print("Результат: ")
f = open(file_name, 'rb')
tools.output(f, frmt, size, mx_l)
f.close()
