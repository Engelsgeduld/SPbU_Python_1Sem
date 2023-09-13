def rev(array,m):
    array = array[::-1]
    n = len(array) - m
    return array

if __name__ == '__main__':
    input_user = [int(a) for a in input('Введите массив').split(' ')]
    m = int(input('Введите m'))
    res = rev(input_user,m, len(input_user)-m)
    print(res)

