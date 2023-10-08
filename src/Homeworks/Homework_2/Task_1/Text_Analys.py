from os.path import exists
import csv


def words_counter(file, counted_words):
    with open(file) as opened_file:
        for line in opened_file:
            for word in line.split():
                counted_words[word] = counted_words.get(word, 0) + 1
    return counted_words


def write_to_csv(file, counted_words):
    with open(file, "w") as opened_file:
        write = csv.writer(opened_file, delimiter=":")
        write.writerows([word, str(counted_words[word])] for word in counted_words)


def input_check(*args):
    user_input = args
    if len(user_input) != 2:
        print("Не верное количество файлов")
        return False
    src, drs = user_input
    if exists(src) and exists(drs):
        return True
    else:
        print("Указанные файлы не найдены")
        return False


def main():
    counted_words = {}
    user_input = input("Введите через пробел файлы \n").split()
    while not input_check(*user_input):
        user_input = input("Введите через пробел файлы \n").split()
    else:
        src, drs = user_input
    counted_words = words_counter(src, counted_words)
    write_to_csv(drs, counted_words)


if __name__ == "__main__":
    main()
