from os.path import exists
from sys import stdout, stderr

from src.Homeworks.homework_6.avl_tree_module.avl_tree import *


def static_mode(dictionary, input_file: str):
    input_file_valid(input_file)
    with open(f"{input_file}") as commands:
        for command in commands.readlines():
            command = command.replace("\n", "")
            command = command.split(" ")
            command_operator(dictionary, False, command[0], *command[1:])


def interactive_mode(dictionary):
    command = input("").split(" ")
    try:
        command_operator(dictionary, True, *command)
    except ValueError as error:
        print(error, file=stderr)
        interactive_mode(dictionary)
    except KeyError as error:
        print(error, file=stderr)
        interactive_mode(dictionary)


def input_file_valid(input_file: str):
    if not exists(f"{input_file}"):
        raise ValueError("Input file not exist")


def write_data(mode: bool, result: list[str]):
    stream = stdout if mode else open(f"streets_res.txt", "a")
    for data in result:
        print(data, file=stream)
    if stream is not stdout:
        stream.close()


def create_command(dictionary: Tree, address: str, index: int):
    put(dictionary, address, index)


def rename_command(dictionary: Tree, street: str, naming: str):
    streets = get_all(dictionary, street, street)
    for old_street in streets:
        houses_and_blocks = " ".join(old_street.split(" ")[1:])
        index = remove(dictionary, old_street)
        put(dictionary, naming + " " + houses_and_blocks, index)


def get_command(dictionary: Tree[Key, Node], address: str):
    try:
        return get(dictionary, address)
    except ValueError:
        return None


def delete_block_command(dictionary: Tree[Key, Value], address: str):
    try:
        remove(dictionary, address)
    except ValueError:
        return


def delete_house_command(dictionary: Tree[Key, Value], street, house):
    try:
        all_houses = get_all(dictionary, street + " " + house, street + " " + house)
    except ValueError:
        return
    for house in all_houses:
        remove(dictionary, house)


def delete_street_command(dictionary: Tree[Key, Value], street: str):
    try:
        all_streets = get_all(dictionary, street, street)
    except ValueError:
        return
    for street in all_streets:
        remove(dictionary, street)


def list_command(
    dictionary: Tree[Key, Value],
    range_of_streets: list[str],
    range_of_houses: list[int],
    range_of_blocks: list[int],
):
    def list_sup_func():
        value = int(str(current_house) + str(current_block))
        if (
            current_street == range_of_streets[0]
            and current_street == range_of_streets[1]
        ):
            if lower_grance <= value < height_grance:
                return [current_street, current_house, current_block]
        elif current_street == range_of_streets[1]:
            if value < height_grance:
                return [current_street, current_house, current_block]

        elif current_street == range_of_streets[0]:
            if lower_grance <= value:
                return [current_street, current_house, current_block]

        else:
            return [current_street, current_house, current_block]

    valid_addresses = []
    all_valid_streets_names = get_all(dictionary, *range_of_streets)
    lower_grance = int(str(range_of_houses[0]) + str(range_of_blocks[0]))
    height_grance = int(str(range_of_houses[1]) + str(range_of_blocks[1]))
    for street in all_valid_streets_names:
        current_street, current_house, current_block = street.split(" ")
        address = list_sup_func()
        if address is not None:
            valid_addresses.append(address)
    valid_addresses.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
    valid_addresses = list(map(" ".join, valid_addresses))
    return valid_addresses


def digits_validation(maybe_digit: str):
    if not maybe_digit.isdigit():
        raise ValueError("Houses, Blocks and Indexes must be positive integers")
    return maybe_digit


def list_input_validation(*args):
    if len(args) != 6:
        raise ValueError(f"Incorrect addresses. Expected 6 positions, got {len(args)}")
    streets = [args[0], args[3]]
    houses = list(map(digits_validation, [args[1], args[4]]))
    blocks = list(map(digits_validation, [args[2], args[5]]))
    return streets, houses, blocks


def get_input_validation(*args):
    if len(args) != 3:
        raise ValueError("Incorrect address")
    street = args[0]
    house, block = list(map(digits_validation, args[1:]))
    return " ".join([street, house, block])


def create_input_validation(*args):
    if len(args) != 4:
        raise ValueError("Incorrect address or index")
    street = args[0]
    house, block, index = list(map(digits_validation, (args[1:])))
    address = " ".join([street, house, block])
    return address, index


def rename_input_validation(*args):
    if len(args) != 2:
        raise ValueError("Expected street and new name")
    return args


def command_operator(dictionary: Tree, mode, command: str, *args):
    match command:
        case "GET":
            result = get_command(dictionary, get_input_validation(*args))
            write_data(mode, [str(result)]) if result is not None else write_data(
                mode, ["None"]
            )
        case "CREATE":
            create_command(dictionary, *create_input_validation(*args))
        case "DELETE_BLOCK":
            delete_block_command(dictionary, get_input_validation(*args))
        case "DELETE_HOUSE":
            street = args[0]
            house = digits_validation(args[1])
            delete_house_command(dictionary, street, house)
        case "DELETE_STREET":
            street = args[0]
            delete_street_command(dictionary, street)
        case "LIST":
            addresses = list_command(dictionary, *list_input_validation(*args))
            write_data(mode, addresses + [""]) if len(addresses) != 0 else write_data(
                mode, [""]
            )
        case "RENAME":
            rename_command(dictionary, *rename_input_validation(*args))
        case "EXIT":
            return
    if mode:
        interactive_mode(dictionary)


def main():
    dictionary = create_tree_map()
    mode = input("Choose operating mode \n1.Interactive\n2.Static\n")
    mode = True if mode == "1" else False
    if not mode:
        input_file = input("Enter input file:\n")
        static_mode(dictionary, input_file)
    else:
        print("0.EXIT\nEnter command:\n")
        interactive_mode(dictionary)


if __name__ == "__main__":
    main()
