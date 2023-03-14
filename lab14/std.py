import struct
import tasks


def check_if_bd(f, frmt, count_lines=False):  # Проверка БД на правильность
    cnt = 0
    if f.read(44) == b'':
        print("Файл пуст")
        if count_lines:
            return False, cnt
        return False
    f.seek(0)
    try:
        line = f.read(44)
        while line:
            struct.unpack(frmt, line)
            cnt += 1
            line = f.read(44)
    except Exception:
        print("Неверный формат базы данных")
        if count_lines:
            return False, cnt
        return False
    else:
        f.seek(0)
        if count_lines:
            return True, cnt
        return True


def prnt(f,frmt):  # Вывод файла
    if f.read(44) == b'':
        print("Файл пуст")
    else:
        f.seek(0)
        print(f"{'-' * 64}\n{'Имя'.center(20)}|{'Год рождения'.center(15)}|"
              f"{'Балл'.center(15)}|{'Допущен'.center(10)}\n{'-' * 64}")
        line = f.read(44)
        while line:
            fields = struct.unpack(frmt, line)
            name = fields[0].decode().rstrip("\x00")
            year = str(fields[1])
            res = str(fields[2])
            passd = fields[3].decode().rstrip("\x00")
            print(f"{name.center(20)}|{year.center(15)}|{res.center(15)}|{passd.center(10)}")
            line = f.read(44)
        print(f"{'-' * 64}")


def prnt_arr(arr):  # Вывод массива
    print(f"{'-' * 64}\n{'Имя'.center(20)}|{'Год рождения'.center(15)}|"
          f"{'Балл'.center(15)}|{'Допущен'.center(10)}\n{'-' * 64}")
    for line in arr:
        name = line[0]
        year = line[1]
        res = line[2]
        passd = line[3]
        print(f"{name.center(20)}|{year.center(15)}|{res.center(15)}|{passd.center(10)}")
    print(f"{'-' * 64}")


def check_fields(frmt):  # Ввод полей
    while True:
        try:
            pname = input("Введите имя (Имя Ф.): ").encode('utf-8')
            if len(pname) > 30:
                print("Превышена максимальная длина строки")
                continue
            pyear = int(input("Введите год рождения: "))
            pres = int(input("Введите результат экзамена: "))
            ppassed = input("Допущен (Да/Нет): ").encode('utf-8')
            if len(ppassed) > 10:
                print("Превышена максимальная длина строки")
                continue
            person = struct.pack(frmt, pname, pyear, pres, ppassed)
        except Exception:
            print("Некорректные данные, повторите ввод")
        else:
            return person


def menu():
    file_name = ""
    while True:
        print("\nМеню")
        print("1) Выбрать файл для работы\n"
              "2) Инициализировать базу данных\n"
              "3) Вывести содержимое базы данных\n"
              "4) Добавить запись в произвольное место базы данных\n"
              "5) Удалить произвольную запись из базы данных\n"
              "6) Поиск по одному полю\n"
              "7) Поиск по двум полям\n"
              "9) Очистить ввод\n"
              "0) Выход")
        user_input = input("Ввод-->")
        if user_input == "1":
            file_name = tasks.task1()
        elif user_input == "2":
            tasks.task2(file_name)
        elif user_input == "3":
            tasks.task3(file_name)
        elif user_input == "4":
            tasks.task4(file_name)
        elif user_input == "5":
            tasks.task5(file_name)
        elif user_input == "6":
            tasks.task6(file_name)
        elif user_input == "7":
            tasks.task7(file_name)
        elif user_input == "9":
            clear = "\n" * 100
            print(clear)
        elif user_input == "0":
            break
        else:
            print("Некорректный ввод, пожалуйста введите номер операции\n")
