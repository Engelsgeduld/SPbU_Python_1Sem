from os.path import exists
from collections import deque
import itertools

def write_file(CNA, file, command):
    file.write(f'{command} : {"".join(CNA)} \n')
def insert(CDA, arg1, frag):
    index = find_sublist(CDA, arg1)[1]
    for i in range(len(frag)):
        CDA.insert(index + i, frag[i])


def delete(CDA, arg1, arg2):
    if arg1 != arg2:
        index_begin, index_end = [find_sublist(CDA, arg1)[1], find_sublist(CDA, arg2)[0]]

    else:
        index_begin, index_end = find_sublist(CDA, arg1)[0], find_sublist(CDA, arg2)[1]

    for _ in range(index_begin, index_end):
        CDA.remove(CDA[index_begin])


def replace(CDA, template, frag):
    insert(CDA, template, frag)
    delete(CDA, template, template)


def find_sublist(CDA, frag):
    res_begin = -1
    res_end = -1
    for idx in range(len(CDA) - len(frag) + 1):
        if list(itertools.islice(CDA, idx, idx + len(frag))) == frag:
            res_begin = idx
            res_end = idx + len(frag)
            break
    return [res_begin, res_end]


def command_center(file,file_write, CDA, n):
    for line in file:
        command, arg1, arg2 = line.split()
        arg1 = [a for a in arg1]
        arg2 = [a for a in arg2]
        match command:
            case 'INSERT':
                insert(CDA, arg1, arg2)
                write_file(CDA,file_write,line.replace("\n",""))
            case 'DELETE':
                delete(CDA, arg1, arg2)
                write_file(CDA, file_write, line.replace("\n",""))
            case 'REPLACE':
                replace(CDA, arg1, arg2)
                write_file(CDA, file_write, line.replace("\n",""))


def read_data(file):
    m = file.readline()
    CDA = file.readline()
    n = file.readline()
    return m, CDA, n


def main():
    user_input = input("Введите 2 файла \n").split()
    if not(exists(user_input[0])) or not(exists(user_input[1])):exit(print("Неверно введены файлы"))
    file = open(user_input[0])
    file_write = open(user_input[1], 'w')
    m, DNA, n = read_data(file)
    DNA = deque(DNA)
    DNA.remove('\n')
    command_center(file,file_write, DNA, n)


if __name__ == "__main__":
    main()
