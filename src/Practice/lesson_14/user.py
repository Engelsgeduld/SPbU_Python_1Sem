from src.Practice.lesson_14.parser import parse, pretty_print


def main():
    line = input("Enter a line\n").split(" ")
    parse_tree = parse(line)
    pretty_print(parse_tree)


if __name__ == "__main__":
    main()
