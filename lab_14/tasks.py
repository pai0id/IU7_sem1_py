import struct
import std

FORMAT = "30s H H  10s"
size = struct.calcsize(FORMAT)


def task1():  # Выбор файла
    name = input("Введите адрес файла: ")
    return name


def task2(file_name):  # Создание БД
    while True:
        try:
            f = open(file_name, 'wb')
            num = int(input("Введите количество записей: "))
        except OSError:
            print("Некорректный путь к файлу")
            return -1
        except ValueError:
            print("Пожалуйста введите целое число")
        else:
            break
    for i in range(num):
        print(f"{i + 1}-я запись:")
        person = std.check_fields(FORMAT)
        f.write(person)
    f.close()


def task3(file_name):  # Вывод БД
    try:
        f = open(file_name, 'rb')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    if std.check_if_bd(f, FORMAT):
        std.prnt(f,FORMAT)
    f.close()


def task4(file_name):  # Вставка в БД
    try:
        f = open(file_name, 'r+b')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    if f.read(size) == b'':
        res_check = (True, 0)
    else:
        f.seek(0)
        res_check = std.check_if_bd(f, FORMAT, True)
    if res_check[0]:
        while True:
            try:
                n = int(input(f"Введите номер позиции(1-{res_check[1] + 1}): ")) - 1
            except ValueError:
                print("Пожалуйста, введите целое число")
            else:
                if not (0 <= n <= res_check[1]):
                    print("Позиция некорректна")
                    continue
                break
        person = std.check_fields(FORMAT)
        f.seek(size * n)
        line = f.read(size)
        while line:
            f.seek(-size, 1)
            f.write(person)
            person = line
            line = f.read(size)
        f.write(person)
    f.close()


def task5(file_name):  # Удаление позиции
    try:
        f = open(file_name, 'r+b')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    res_check = std.check_if_bd(f, FORMAT, True)
    if res_check[0]:
        while True:
            try:
                n = int(input(f"Введите номер позиции(1-{res_check[1]}): "))
            except ValueError:
                print("Пожалуйста, введите целое число")
            else:
                if not (0 < n <= res_check[1]):
                    print("Позиция некорректна")
                    continue
                break
        f.seek(n * size)
        line = f.read(size)
        while line:
            f.seek(-(size * 2), 1)
            f.write(line)
            f.seek(size, 1)
            line = f.read(size)
        f.seek(-size, 1)
        f.truncate()
    f.close()


def task6(file_name):  # Поиск по одному полю
    try:
        f = open(file_name, 'rb')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    if std.check_if_bd(f, FORMAT):
        print("Выберите поле:\n1)Имя\n2)Год рождения\n3)Балл\n4)Допуск")
        while True:
            try:
                u_inp = int(input("-->")) - 1
            except ValueError:
                print("Введите номер поля")
            else:
                if not (0 <= u_inp <= 3):
                    print("Введите номер поля")
                    continue
                break
        val = input("Искомое значение: ")
        print("Результат:")
        was_changed = False
        res = []
        line = f.read(size)
        while line:
            temp = ['', 0, 0, '']
            fields = struct.unpack(FORMAT, line)
            temp[0] = fields[0].decode().rstrip("\x00")
            temp[1] = str(fields[1])
            temp[2] = str(fields[2])
            temp[3] = fields[3].decode().rstrip("\x00")
            if temp[u_inp] == val:
                res.append(temp)
                was_changed = True
            line = f.read(size)
        if not was_changed:
            print("Подходящих записей нет")
        else:
            std.prnt_arr(res)
    f.close()


def task7(file_name):  # Поиск по двум полям
    try:
        f = open(file_name, 'rb')
    except OSError:
        print("Файл не найден")
        return -1
    except Exception:
        print("Некорректный путь к файлу")
        return -1
    if std.check_if_bd(f, FORMAT):
        print("Выберите поле:\n1)Имя\n2)Год рождения\n3)Балл\n4)Допуск")
        while True:
            try:
                u_inp1 = int(input("-->")) - 1
            except ValueError:
                print("Введите номер поля")
            else:
                if not (0 <= u_inp1 <= 3):
                    print("Введите номер поля")
                    continue
                break
        val1 = input("Искомое значение: ")
        print("Выберите второе поле:")
        while True:
            try:
                u_inp2 = int(input("-->")) - 1
            except ValueError:
                print("Введите номер поля")
            else:
                if not (0 <= u_inp2 <= 3):
                    print("Введите номер поля")
                    continue
                if u_inp2 == u_inp1:
                    print("Введите номер отличный от первого")
                    continue
                break
        val2 = input("Искомое значение: ")
        print("Результат:")
        was_changed = False
        res = []
        line = f.read(size)
        while line:
            temp = ['', 0, 0, '']
            fields = struct.unpack(FORMAT, line)
            temp[0] = fields[0].decode().rstrip("\x00")
            temp[1] = str(fields[1])
            temp[2] = str(fields[2])
            temp[3] = fields[3].decode().rstrip("\x00")
            if temp[u_inp1] == val1 and temp[u_inp2] == val2:
                res.append(temp)
                was_changed = True
            line = f.read(size)
        if not was_changed:
            print("Подходящих записей нет")
        else:
            std.prnt_arr(res)
    f.close()
