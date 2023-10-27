import string
from collections import Counter
from sys import argv


def check_input_file(user_input):
    try:
        return open(f"{user_input}")
    except:
        raise ValueError("Input file not exist")


def check_output_file(user_input):
    try:
        return open(f"{user_input}", "x")
    except:
        raise ValueError("Output file already exist")


def count_letters_from_file(file):
    counted_letters = Counter()
    with file as read_file:
        for line in read_file:
            for sign in string.punctuation:
                line = line.replace(sign, " ")
            letters = sorted(
                [letter for letter in line if letter != " " and letter != "\n"]
            )
            counted_letters.update(count_letters(letters))
    return dict(counted_letters)


def write_file(file, letters):
    file.write("".join([f"{letter}:{letters[letter]}\n" for letter in letters]))
    file.close()


def count_letters(letters):
    counted_letters = dict(Counter([*letters]))
    return counted_letters


def main():
    file_in = argv[1]
    file_out = argv[2]
    try:
        write_file(
            check_output_file(file_out),
            count_letters_from_file(check_input_file(file_in)),
        )
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
