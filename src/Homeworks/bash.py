from sys import argv
import os


def wc(file = '',param = None):
    f1 = open(f'{file}')
    f = [a.split() for a in f1]
    match param:
        case '-c':
            return os.path.getsize(f'{file}')
        case '-m':
            chars = 0
            for i in range(len(f)):
                chars += len(''.join(f[i]))
            return chars
        case '-l':
            return len(f)
        case '-w':
            a = [len(b) for b in f]
            return sum(a)
        case _:
            res = " ".join(map(str,[wc(file,'-c'),wc(file,'-m'),wc(file,'-l'),wc(file,'-w')]))
            return res


def head(n, file, param = '-n'):

    try: n =  int(n)
    except: n = 10

    fl = open(f'{file}')
    match param:

        case '-c':
            result = ''
            ff = ''.join([a for a in open(f'{file}')])
            for line in ff:
                if len(result + line) <= n:
                    result += line
                else:
                    break
            return result

        case _:
            f = ''
            for _ in range(n):
                f += fl.readline()
            return f


def tail(file, param = '-n', n = 10):
    match param:

        case '-c':
            result = ''
            ff = ''.join([a for a in open(f'{file}')])
            for line in ff[len(ff) - n:]:
                if len(result + line) <= n:
                    result += line
                else:
                    break
            return result

        case _:
            f = [a.split() for a in open(f'{file}')]
            res = '\n'.join(''.join(a) for a in f[len(f) - n:])
            return res

def main():
    user_input = argv

    match user_input[1]:
        case 'wc':
            try:
                open(f'{user_input[-1]}')
            except FileNotFoundError:
                print("Файл не найден")
                exit()
            res = " ".join([a for a in user_input[1:]] + [str(wc(user_input[-1],user_input[-2]))])
            print(res)
        case 'head':

            try:
                open(f'{user_input[-1]}')
            except FileNotFoundError:
                print("Файл не найден")
                exit()

            res = " ".join([a for a in user_input[1:]] + [str(head(user_input[-2], user_input[-1], user_input[-3]))])
            print(res)
        case 'tail':

            try:
                open(f'{user_input[-1]}')
            except FileNotFoundError:
                print("Файл не найден")
                exit()

            res = " ".join([a for a in user_input[1:]] + [str(head(user_input[-2], user_input[-1], user_input[-3]))])
            print(res)


if __name__ == '__main__':
    main()
