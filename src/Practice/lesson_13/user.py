from string import digits

from src.Practice.lesson_13.fsm import create_fs_machine, validate_string, FSMachine


def create_digits_validator() -> FSMachine:
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
    return fms_digits


def create_abb_validator() -> FSMachine:
    table_abb = [{"b": 0, "a": 1}, {"b": 2, "a": 1}, {"b": 3, "a": 1}, {"b": 0, "a": 1}]
    fms_abb = create_fs_machine(table_abb, 0, [3])
    return fms_abb


def language_validator(line: str) -> list[str]:
    pairs = [
        (create_abb_validator(), "АБОБА ЛАНГУАГЕ"),
        (create_digits_validator(), "Digits language"),
    ]
    passed_langs = [pair[1] for pair in pairs if validate_string(pair[0], line)]
    return passed_langs


def output_line_printer(line: str):
    passed_langs = language_validator(line)
    if passed_langs:
        print(f"This is {' '.join(passed_langs)}")
    else:
        print("This string match no language")


def main():
    user_input = input("Input string for validation \n")
    output_line_printer(user_input)


if __name__ == "__main__":
    main()
