from src.Homeworks.homework_6.avl_tree_module.avl_tree import *
from os.path import exists


def validate_files(input_file: str, balance_file: str, logs_file: str):
    if not exists(f"{input_file}"):
        raise ValueError("Command file not Exist")
    if exists(f"{balance_file}"):
        raise ValueError("balance file already exist")
    if exists(f"{logs_file}"):
        raise ValueError("logs file already exist")


def write_data(line, name):
    logs = open(f"{name}", "a")
    logs.write(str(line) + "\n")
    logs.close()


def write_balance(data, name):
    with open(f"{name}", "a") as balance:
        for pair in data:
            balance.write(f"{pair[0]} {pair[1]}" + "\n")


def add_command(stock: Tree, size, count):
    if has_key(stock, size):
        old_value = get(stock, size)
        put(stock, size, count + old_value)
    else:
        put(stock, size, count)


def get_command(stock: Tree, size):
    try:
        return get(stock, size)
    except ValueError:
        return 0


def select_command(stock: Tree, size):
    if size is None:
        return -1
    found_size = get_lower_bound(stock, size)
    if found_size is None:
        return -1
    found_size_value = get(stock, found_size)
    if found_size_value == 0:
        remove(stock, found_size)
        return select_command(stock, size)
    put(stock, found_size, found_size_value - 1)
    return found_size


def command_operator(stock, logs_file, command, *args):
    match command:
        case "ADD":
            if len(args) != 2:
                raise ValueError(f"ADD required 2 arguments, got {len(args)}")
            add_command(stock, *args)
        case "GET":
            if len(args) != 1:
                raise ValueError(f"GET required 1 arguments, got {len(args)}")
            write_data(get_command(stock, *args), logs_file)
        case "SELECT":
            if len(args) != 1:
                raise ValueError(f"SELECT required 1 arguments, got {len(args)}")
            size = select_command(stock, *args)
            write_data(size, logs_file) if size > -1 else write_data("SORRY", logs_file)


def main():
    stock = create_tree_map()
    logs_file = input("Enter names for logs file\n")
    balance_file = input("Enter names for balance file\n")
    input_file = input("Enter command file\n")
    validate_files(input_file, logs_file, balance_file)
    with open(f"{input_file}") as opened_input_file:
        for line in opened_input_file.readlines():
            line = line.split(" ")
            command = line[0]
            args = list(map(int, line[1:]))
            command_operator(stock, logs_file, command, *args)
    write_balance(
        list(filter(lambda pair: pair[1] > 0, traverse(stock, 1))), balance_file
    )


if __name__ == "__main__":
    main()
