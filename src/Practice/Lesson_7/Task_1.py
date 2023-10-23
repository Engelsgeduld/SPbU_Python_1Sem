def valid_user_input(user_input):
    [float_check(num) for num in user_input.split()]


def choose_function(args):
    if len(args) == 3:
        return find_real_square_root(*args)
    if len(args) == 2:
        return find_linear_solution(*args)

    raise ValueError(
        "Количество введенных аргументов не подходит ни к одному типу функции"
    )


def find_real_square_root(a, b, c):
    if a == 0:
        return find_linear_solution(b, c)

    dis = b**2 - 4 * a * c

    if dis < 0:
        raise ValueError("Дискриминант меньше 0")

    sqrt_val = dis ** (1 / 2)

    if dis > 0:
        return tuple((-b + sign * sqrt_val) / (2 * a) for sign in (-1, 1))

    if dis == 0:
        return (-b / (2 * a),)


def find_linear_solution(a, b):
    if a == 0 and b == 0:
        raise ValueError("Решение таких уравнений в данной системе не рассматривается")

    if a == 0:
        raise ValueError("Значение параметра k не должно быть равно нулю")
    return (-b / a,)


def float_check(num):
    try:
        float(num)
    except:
        raise ValueError("Аргумент не является числом")


def main():
    user_input = input(
        "Введите значения a, b, c для квадратного уравнения, либо k, b для линейного\n"
    )
    try:
        valid_user_input(user_input)
        args = list(map(float, user_input.split()))
        print(f"Результат вычислений: {' '.join(map(str,choose_function(args)))}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
