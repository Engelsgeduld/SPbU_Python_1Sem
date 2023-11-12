import string


def validate_user_dna_input(line):
    if line == "":
        raise ValueError("Got an empty line")
    if any(sign not in string.ascii_letters for sign in set(line)):
        raise ValueError("Only latin letters allowed")
    return line


def validate_compress_input(line):
    letters = string.ascii_letters
    digits = string.digits
    if line == "":
        raise ValueError("Got an empty line")
    if line[0] not in letters:
        raise ValueError("Compressed line must begin with latin letter")
    if line[-1] not in digits:
        raise ValueError("Last symbol must be digit")
    if any(sign not in letters + digits for sign in set(line)):
        raise ValueError("Only latin letters and digits allowed")
    if any(line[i] in letters and line[i + 1] in letters for i in range(len(line))):
        raise ValueError("Compress Error 2 letters near by")
    return line


def compress_line(line):
    transfers = list(
        filter(lambda index: line[index - 1] != line[index], range(1, len(line)))
    ) + [len(line)]
    pairs = list(map(lambda x, y: (x, y - x), transfers, transfers[1:]))
    new_line = "".join(list(map(lambda pair: f"{line[pair[0]]}{pair[1]}", pairs)))
    compressed_line = f"{line[0]}{transfers[0]}" + new_line
    return compressed_line


def decode_line(line):
    letters = list(
        filter(lambda index: line[index] in string.ascii_letters, range(len(line)))
    ) + [len(line)]
    new_line = "".join(
        list(map(lambda x, y: line[x] * int(line[x + 1 : y]), letters, letters[1:]))
    )
    return new_line


def encode_dna():
    try:
        valid_line = validate_user_dna_input(input("Enter a DNA: \n"))
        compressed_line = compress_line(valid_line)
        print(f"Compress DNA:{compressed_line}")
    except ValueError as error:
        print(error)


def decode_dna():
    try:
        valid_line = validate_compress_input(input("Enter a compress DNA: \n"))
        decoded_line = decode_line(valid_line)
        print(f"Original DNA:{decoded_line}")
    except ValueError as error:
        print(error)


def menu(user_choice):
    match user_choice:
        case "1":
            encode_dna()
        case "2":
            decode_dna()


def main():
    user_choice = input("Choose option:\n 1.Encode\n 2.Decode\n")
    menu(user_choice)


if __name__ == "__main__":
    main()
