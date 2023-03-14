# Поляков Андрей ИУ7-12Б Защита 14
# Есть структура вида "имя возраст"
# Заполнить файл
# Cпросить возраст для фильтра
# Вывести в файл всех, кто старше

import struct

F0RMAT = "40s H"


def output(f_name, frmt):
    while True:
        try:
            f = open(f_name, 'rb')
        except OSError:
            print("Некорректный путь к файлу")
            return -1
        except Exception:
            print("Ошибка")
            return -1
        else:
            break
    size = struct.calcsize(frmt)
    if f.read(size) == b'':
        print("Файл пуст")
    else:
        f.seek(0)
        print(f"{'-' * 31}\n{'Имя'.center(20)}|{'Возраст'.center(10)}\n{'-' * 31}")
        line = f.read(size)
        while line:
            p = struct.unpack(frmt, line)
            name = p[0].decode().rstrip('\x00')
            age = str(p[1])
            print(f"{name.center(20)}|{age.center(10)}")
            line = f.read(size)
        print(f"{'-' * 31}")
    f.close()


def enter(file_name, frmt):
    while True:
        try:
            f = open(file_name, 'wb')
            num = int(input("Количество записей: "))
        except OSError:
            print("Некорректный путь к файлу")
            return -1
        except ValueError:
            print("Введите целое число")
        except Exception:
            print("Ошибка")
            return -1
        else:
            break
    for i in range(num):
        print(f"{i + 1}-я запись:")
        p = b""
        while True:
            try:
                name = input("Введите имя: ").encode('utf-8')
                if len(name) > 20:
                    print("Превышен максимальный размер имени")
                    continue
                age = int(input("Введите возраст: "))
                p = struct.pack(frmt, name, age)
                break
            except Exception:
                print("Некорректный формат данных")
        f.write(p)
    f.close()


def filter_n_write(in_file, out_file, frmt):
    size = struct.calcsize(frmt)
    while True:
        try:
            nage = int(input("Введите возраст для фильтра: "))
        except ValueError:
            print("Введите целое число")
        else:
            if nage < 0:
                print("Отрицательный возраст?")
                continue
            break
    while True:
        try:
            f1 = open(in_file, 'rb')
            f2 = open(out_file, 'wb')
        except OSError:
            print("Некорректный путь к файлу")
            return -1
        except Exception:
            print("Ошибка")
            return -1
        else:
            break
    line = f1.read(size)
    while line:
        p = struct.unpack(frmt, line)
        age = p[1]
        if age >= nage:
            f2.write(line)
        line = f1.read(size)
    f1.close()
    f2.close()


def menu(frmt):
    file_name = ""
    out_file = ""
    while True:
        print("1) Инициализировать БД\n"
              "2) Открыть БД как ввод\n"
              "3) Отфильтровать и вывести в другой файл\n"
              "4) Вывести БД\n"
              "0) Конец")
        inp = input("-->")
        if inp == "1":
            file_name = input("Введите имя файла ввода: ")
            enter(file_name, frmt)
        elif inp == "2":
            file_name = input("Файл: ")
        elif inp == "3":
            inp_out_file = input("Введите имя файла вывода ('-', если тот же): ")
            out_file = inp_out_file if inp_out_file != '-' else out_file
            filter_n_write(file_name, out_file, frmt)
        elif inp == "4":
            while True:
                print("1)Исходный файл\n"
                      "2)Полученный файл")
                choice = input("-->")
                if choice == "1":
                    output(file_name, frmt)
                    break
                elif choice == "2":
                    output(out_file, frmt)
                    break
                else:
                    print("Введите 1 или 2")
        elif inp == "0":
            break
        else:
            print("Некорректный ввод")


menu(F0RMAT)
