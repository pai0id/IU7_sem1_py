# Поляков Андрей ИУ7-12Б
# Сортировка пузырьком с флагом

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
was_swapped = True  # флаг
while was_swapped:
    f.seek(0)
    was_swapped = False
    prv = struct.unpack(frmt, f.read(size))[0]
    nxt = f.read(size)
    while nxt:
        nxt = struct.unpack(frmt, nxt)[0]
        if prv > nxt:
            f.seek(-size * 2, 1)
            f.write(struct.pack(frmt, nxt))
            f.write(struct.pack(frmt, prv))
            was_swapped = True
        else:
            prv = nxt
        nxt = f.read(size)

print("Результат: ")
f = open(file_name, 'rb')
tools.output(f, frmt, size, mx_l)
f.close()
