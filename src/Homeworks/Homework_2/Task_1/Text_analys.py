from os.path import exists
import csv

def words_counter(file, counted_words):
    with open(file) as F:
        for line in F:
            '''Не стал оборачивать в list comprehension. Теряется логика кода и выражение излишне длинное'''
            for word in set(line.split()):
                if word in counted_words: counted_words[word] += line.count(word)
                else: counted_words[word] = line.count(word)
    return counted_words

def write_to_csv(file,counted_words):
    with open(file, 'w') as F:
        write = csv.writer(F, delimiter=':')
        write.writerows([word, str(counted_words[word])] for word in counted_words)

    with open(file) as f:
        print(f.read())

def input_check(user_input):
    user_input = user_input.split()
    if len(user_input) !=2:
        print("Не верный ввод файлов")
        exit()
    src, drs = user_input
    if exists(src) and exists(drs) : return src, drs
    else:
        print("Указанные файлы не найдены")
        exit()



def main():
    counted_words = {}
    src, drs = input_check(input("Введите через пробел файлы \n"))
    counted_words = words_counter(src,counted_words)
    write_to_csv(drs,counted_words)

if __name__ == "__main__":
    main()
