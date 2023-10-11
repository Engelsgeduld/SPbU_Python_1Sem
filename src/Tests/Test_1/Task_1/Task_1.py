from sys import argv
from os.path import exists


def integer_input_check(a, b):
    if not a.lstrip("-").isdigit() or not b.lstrip("-").isdigit():
        return False
    else:
        return True


def check_file_f_existence(file_f):
    if exists(f"{file_f}.txt"):
        return True
    else:
        return False


def check_file_g_existence(file_g):
    if exists(f"{file_g}.txt"):
        return True
    else:
        return False


def read_input_file(file_f):
    file_f = open(f"{file_f}.txt")
    nums = list(map(int, file_f.readline().split()))
    file_f.close()
    return nums


def file_analyse(nums, a, b):
    first_cat = []
    second_cat = []
    other = []
    for num in nums:
        if num < a:
            first_cat += [num]
        elif a <= num <= b:
            second_cat += [num]
        else:
            other += [num]

    return first_cat, second_cat, other


def write_output(file_g, first, second, other):
    with open(f"{file_g}.txt", "w") as output_file:
        for category in [first, second, other]:
            output_file.write(
                " ".join(list(map(str, [num for num in category]))) + "\n"
            )


def main():
    a, b = argv[1:3]
    if integer_input_check(a, b):
        a, b = int(a), int(b)
    else:
        print("Параметры сортировки должны быть числами")
        exit()

    file_f, file_g = argv[3:5]

    if check_file_f_existence(file_f) is False:
        print("Файл ввода не существует")
        exit()
    '''if check_file_g_existence(file_g):
        print("Файл вывода уже существует")
        exit()'''

    write_output(file_g, *file_analyse(read_input_file(file_f), a, b))


if __name__ == "__main__":
    main()
