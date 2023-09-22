from sys import argv
import os
from os.path import exists


def wc(file='', param=None):
    if param == '-c': return os.path.getsize(f'{file}')
    with open(f'{file}') as F:
        match param:
            case '-m':
                chars = 0
                for line in F:
                    chars += len(line) + 1
                return chars
            case '-l':
                count = 0
                for _ in F:
                    count += 1
                return count
            case '-w':
                words = 0
                for line in F:
                    words += len(line.split())
                return words
            case _:
                res = [wc(file, '-c'), wc(file, '-m'), wc(file, '-l'), wc(file, '-w')]
                return res


def head(n, file, param):
    n = int(n)
    with open(f'{file}') as F:
        match param:
            case '-c':
                return F.read(n)

            case '-n':
                count = 0
                lines = ''
                for line in F:
                    if count == n: break
                    count += 1
                    lines += line
                return lines


def tail(param, file, n):
    open_file = open(f'{file}')
    match param:
    
        case '-c':
            result = ''
            
            ff = [a for a in open_file]
            for index in range(len(ff)-1,0,-1):
                print(len((result + ff[index]).encode('utf-8')))
                if len((result + ff[index]).encode('utf-8')) <= n:
                    result += ff[index]
                else:
                    break
            open_file.close()
            return result

        case '-n':
            f = [a for a in open_file]
            res = '\n'.join(''.join(a) for a in f[len(f) - n:])
            open_file.close()
            return res


def main():
    user_input = argv

    if not exists(f'{argv[-1]}'):
        print(f'Файл {argv[-1]} не обнаружен')
        exit()

    if user_input[1] ==  'wc':
            res = " ".join([a for a in user_input[1:]]) + ' ' + ' '.join(map(str,wc(user_input[-1], user_input[-2])))
            print(res)
    if len(user_input) == 5:
        if not user_input[-2].isdigit():
            print(f"Некорректное значение N: {user_input[-2]}")
            exit()
        if user_input[1] == 'head':
            res = " ".join([a for a in user_input[1:]] + [str(head(user_input[-2], user_input[-1], user_input[-3]))])
            print(res)
        if user_input[1] == 'tail':
            res = " ".join([a for a in user_input[1:]] + [str(tail(user_input[-3], user_input[-1], int(user_input[-2])))])
            print(res)
    elif user_input[1] == 'head': print("".join([a for a in user_input[1:]]+[str(head(10, user_input[-1],'-n'))]))
    elif user_input[1] == 'tail': print("".join([a for a in user_input[1:]]+[str(tail('-n',user_input[-1],10))]))


if __name__ == '__main__':
    main()
