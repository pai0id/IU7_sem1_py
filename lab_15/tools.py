import struct


def create(f, num, frmt):  # Создание БД
    max_l = 0
    for i in range(num):
        x = input(f"{i + 1}-я запись:")
        while True:
            try:
                max_l = max(max_l, len(x))
                x = int(x)
                person = struct.pack(frmt, x)
            except Exception:
                print("Пожалуйста, введите целое число")
            else:
                break
        f.write(person)
    return max_l


def output(f, frmt, size, max_l):
    if not f.read(size):
        print("Файл пуст")
    else:
        f.seek(0)
        line = f.read(size)
        while line:
            x = struct.unpack(frmt, line)[0]
            print(f"|{str(x).center(max_l)}|")
            line = f.read(size)
