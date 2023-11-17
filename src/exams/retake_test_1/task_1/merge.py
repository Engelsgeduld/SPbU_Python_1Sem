from os.path import exists
from sys import argv


def write_file(sequence, file):
    with open(f"{file}", "w") as output_file:
        for integer in sequence:
            output_file.write(str(integer) + " ")


def valid_files(*args):
    if len(args) != 2:
        raise ValueError("Wrong number of files")
    if not exists(args[0]):
        raise ValueError("Input file not exist")
    if exists(args[1]):
        raise ValueError("Output file exist")
    return args[0], args[1]


def read_data(file):
    with open(f"{file}") as input_file:
        sequences = input_file.readlines()
        sequences = list(map(lambda line: list(map(int, line.split(" "))), sequences))
    return sequences


def sort_sequences(sequences):
    merged_sequences = []
    first_seq, second_seq = sequences
    i = j = 0
    while i < len(first_seq) and j < len(second_seq):
        if first_seq[i] < second_seq[j]:
            merged_sequences.append(first_seq[i])
            i += 1
        else:
            merged_sequences.append(second_seq[j])
            j += 1

    merged_sequences += first_seq[i:]
    merged_sequences += second_seq[j:]
    return merged_sequences


def main():
    files = argv[1:]
    input_file, output_file = valid_files(*files)
    sequences = read_data(input_file)
    merged_sequence = sort_sequences(sequences)
    write_file(merged_sequence, output_file)


if __name__ == "__main__":
    main()
