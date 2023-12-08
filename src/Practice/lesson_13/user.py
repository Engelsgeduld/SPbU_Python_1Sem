from string import digits

from src.Practice.lesson_13.fsm import create_fs_machine, validate_string


def digits_validation(line: str):
    table_digits = [
        {digits: 1, "+-": 5},
        {digits: 1, "E": 3, ".": 6},
        {digits: 2, "E": 3},
        {digits: 4, "+-": 7},
        {digits: 4},
        {digits: 1},
        {digits: 2},
        {digits: 4},
    ]
    fms_digits = create_fs_machine(table_digits, 0, [1, 2, 4])
    return validate_string(fms_digits, line)


def abb_validation(line: str):
    table_abb = [{"b": 0, "a": 1}, {"b": 2, "a": 1}, {"b": 3, "a": 1}, {"b": 0, "a": 1}]
    fms_abb = create_fs_machine(table_abb, 0, [3])
    return validate_string(fms_abb, line)


def output_line_constructor(line: str):
    if abb_validation(line):
        print("This is АБОБА ЛАНГУАГЕ")
    elif digits_validation(line):
        print("This is Digits language")
    else:
        print("This string match no language")


def main():
    user_input = input("Input string for validation \n")
    output_line_constructor(user_input)


if __name__ == "__main__":
    main()
