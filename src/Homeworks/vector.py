from math import acos


def print_matrix(matrix):
    str_m = ''
    if matrix is None: return ''
    for i in range(len(matrix)):
        matrix_str = " ".join(str(a) for a in matrix[i])
        str_m += '\n' + matrix_str
    return str_m


def xmatrix(matrixs, numer1, numer2):
    if len(matrixs[numer1][0]) != len(matrixs[numer2]):
        print('Количество столбцов 1 матрицы должно совпадать с числом строк 2')
        return None
    new_matrix = [[sum(a * b for a, b in zip(row_numer1, col_numer2)) for col_numer2 in zip(*matrixs[numer2])] for
                  row_numer1 in matrixs[numer1]]
    return new_matrix


def sum_matrix(matrixs, numer1, numer2):
    new_matrix = []
    if len(matrixs[numer1]) != len(matrixs[numer2]) or len(matrixs[numer1][0] != len(matrixs[numer2][0])):
        print('Матрицы должны быть одинакового размера')
        return None
    for j in range(len(matrixs[numer1])):
        row = []
        for i in range(len(matrixs[numer1][0])):
            row += [matrixs[numer1][j][i] + matrixs[numer2][j][i]]
        new_matrix += [row]
    return new_matrix


def transpon(matrixs, numer):
    new_matrix = []
    for i in range(len(matrixs[numer][0])):
        row = []
        for a in range(len(matrixs[numer])):
            row += [matrixs[numer][a][i]]
        new_matrix += [row]
    return new_matrix


def add_vector(vectors):
    vector = [int(a) for a in input().split(' ')]
    vectors += [vector]
    return vectors


def add_matrix(matrixs):
    matrix = [list(map(int, a.split(' '))) for a in input().split(',')]
    matrixs += [matrix]
    return matrixs


def see_vectors(vectors):
    for i in range(len(vectors)):
        print(f'Номер вектора {i + 1}. Вектор: {vectors[i]}')


def see_matrixs(matrixs):
    for i in range(len(matrixs)):
        print(f'Номер матрицы {i + 1}. {matrixs[i]}')


def delete_vector(vectors):
    if len(vectors) == 0:
        print('В списке нет векторов, внесите вектора, чтобы иметь возможность их удалить')
        return None
    see_vectors(vectors)
    chosen = int(input())
    vectors.pop(chosen - 1)
    return vectors


def scalar(vectors, numer1, numer2):
    if len(vectors[numer1]) != len(vectors[numer2]):
        print('Векторы должны иметь равное число координат')
        return None
    result = sum([vectors[numer1][i] * vectors[numer2][i] for i in range(len(vectors[numer1]))])
    return result


def len_vector(vectors, numer):
    result = sum([a * a for a in vectors[numer]]) ** (1 / 2)
    return result


def angle(vectors, numer1, numer2):
    if len(vectors[numer1]) != len(vectors[numer2]):
        print('Векторы должны иметь равное число координат')
        return None
    result = acos(
        scalar(vectors, numer1, numer2) / (len_vector(vectors, numer1) * len_vector(vectors, numer2))) * 57.2958
    return result


def main():
    user_input_data_type = input('Выберите тип данных для работы\n a.Векторы\n b.Матрицы \n')

    vectors = []
    matrixs = []
    while True and user_input_data_type == 'a':
        print(
            'Меню управления приложением: \n1.Добавить вектор\n2.Посмотреть все вектора\n3.Удалить вектор\n4.Посчитать длинну вектора\n5.Посчитать скалярное произведение\n6.Угол между векторами\n0.Выход')
        user_input = input()
        if user_input == '0': break

        match user_input:
            case '1':
                print('Напишите координаты вектора через пробел')
                vectors = add_vector(vectors)
                print('Вектор успешно добавлен')
            case '2':
                see_vectors(vectors)
            case '3':
                print('Введите номер вектора')
                vectors = delete_vector(vectors)
            case '4':
                print('Введите номер вектора')
                imp = int(input()) - 1
                print(f'Длинна вектора под номером {imp + 1}:{len_vector(vectors, imp)}')
            case '5':
                print('Введите номера 2 векторов через пробел')
                imp = [int(a) - 1 for a in input().split(' ')]
                print(f'Скалярное произведение векторов {imp[0] + 1} и {imp[1] + 1}: {scalar(vectors, imp[0], imp[1])}')
            case '6':
                print('Введите номера 2 векторов через пробел')
                imp = [int(a) - 1 for a in input().split(' ')]
                print(f'Угол между векторами {imp[0] + 1} и {imp[1] + 1} в градусах{angle(vectors, imp[0], imp[1])}')
            case '0':
                break

    while True and user_input_data_type == 'b':
        print(
            'Меню управления приложением: \n 1. Добавить матрицу \n 2. Посмотреть все матрицы \n 3. Транспонировать матрицу \n 4. Сложить матрицы \n 5. Умножить матрицы \n 0. Выход')
        user_input = input()
        match user_input:
            case '1':
                print('Введите строки матрицы через запятую, значения через пробел. Пример: 1 2 3,3 2 1')
                matrixs = add_matrix(matrixs)
                print('Матрица успешно добавлена')
            case '2':
                see_matrixs(matrixs)
            case '3':
                see_matrixs(matrixs)
                print('Введите номер матрицы')
                numer = int(input())
                print(f'Результат транспонирования матрицы {numer}' + print_matrix(transpon(matrixs, numer - 1)))
            case '4':
                see_matrixs(matrixs)
                print('Введите номера 2 матриц для суммы через пробел')
                numer1, numer2 = map(int, input().split(' '))
                print(f'Результат сложения матриц {numer1} и {numer2}' + print_matrix(
                    sum_matrix(matrixs, numer1 - 1, numer2 - 1)))
            case '5':
                see_matrixs(matrixs)
                print('Введите номера 2 матриц для умножения через пробел')
                numer1, numer2 = map(int, input().split(' '))
                print(f'Результат умножения матриц {numer1} и {numer2}' + print_matrix(
                    xmatrix(matrixs, numer1 - 1, numer2 - 1)))
            case '0':
                break


if __name__ == '__main__':
    main()
