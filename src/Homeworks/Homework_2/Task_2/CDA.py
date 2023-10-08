from os.path import exists
import itertools


def write_file(dna, file):
    for line in dna:
        file.write(f"{dna.index(line)} : {line} \n")


def insert(dna, arg1, frag):
    line = dna[-1]
    index_of_arg1 = line.index(arg1)
    dna.append(
        line[: index_of_arg1 + len(arg1)] + frag + line[index_of_arg1 + len(arg1) :]
    )
    return dna


def delete(dna, arg1, arg2):
    line = dna[-1]
    index_of_arg1 = line.index(arg1)
    dna.append(
        line[: index_of_arg1 + len(arg1)]
        + line[line.index(arg2, index_of_arg1) + len(arg2) - 1 :]
    )
    return dna


def replace(dna, template, frag):
    line = dna[-1]
    line = line.replace(template, frag, 1)
    dna.append(line)
    return dna


def find_sublist(dna, frag):
    res_begin = -1
    res_end = -1
    for idx in range(len(dna) - len(frag) + 1):
        if list(itertools.islice(dna, idx, idx + len(frag))) == frag:
            res_begin = idx
            res_end = idx + len(frag)
            break
    return [res_begin, res_end]


def command_center(file, dna, n):
    for line in file:
        command, arg1, arg2 = line.split()
        match command:
            case "INSERT":
                dna = insert(dna, arg1, arg2)
            case "DELETE":
                dna = delete(dna, arg1, arg2)
            case "REPLACE":
                dna = replace(dna, arg1, arg2)
    return dna


def read_data(file):
    m = file.readline()
    dna = file.readline()
    n = file.readline()
    return m, dna, n


def valid_existed_file(user_input):
    match user_input:
        case "y":
            return True
        case "n":
            exit()
        case _:
            return valid_existed_file(input())


def valid_user_input(*args):
    if len(args) != 2:
        print("Неверное число файлов")
        return False
    if exists(args[0]):
        if exists(args[1]):
            return valid_existed_file(
                input(
                    "Файл ввода уже существует. Данные будут перезаписаны. Хотите продолжить? [y/n] \n"
                )
            )
        else:
            new_file = open(f"{args[1]}", "a")
            new_file.close()
            return True
    else:
        print("Файл ввода не найдет")
        return False


def main():
    user_input = input("Введите 2 файла \n").split()
    while not valid_user_input(*user_input):
        user_input = input("Введите 2 файла \n").split()
    else:
        file = open(user_input[0])
    m, old_dna, n = read_data(file)
    dna = [old_dna[:-1]]
    dna = command_center(file, dna, n)
    file.close()
    file_write = open(user_input[1], "w")
    write_file(dna, file_write)
    file_write.close()


if __name__ == "__main__":
    main()
