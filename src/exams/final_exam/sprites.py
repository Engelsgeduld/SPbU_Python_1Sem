import re
import sys

SPRITE_UNICODE = "█"


def validate_user_input(user_input: str):
    if re.fullmatch("[1-9][0-9]*", user_input):
        return int(user_input)
    else:
        raise ValueError("Length must be a integer")


def create_sprites_table(row_length: int):
    sprites_table = list(
        map(lambda _: (SPRITE_UNICODE + " ") * row_length + "\n", range(row_length))
    )
    return sprites_table


def create_sprites_string(sprites_table: list[str]):
    sprites_string = "".join(sprites_table)
    return sprites_string


def main():
    user_input = input("Enter sprite length in pixels \n")
    while user_input != "STOP":
        try:
            valid_user_input = validate_user_input(user_input)
        except ValueError as error:
            print(error, file=sys.stderr)
            break
        sprites_table = create_sprites_table(valid_user_input)
        print(create_sprites_string(sprites_table))
        user_input = input("Enter length or write STOP\n")


if __name__ == "__main__":
    main()
