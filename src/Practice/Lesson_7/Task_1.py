def parse_user_input(user_input):
    split_user_input = user_input.split()
    if len(split_user_input) not in [2, 3]:
        raise ValueError(
            "Количество введенных аргументов не подходит ни к одному типу функции"
        )
    try:
        return [float(num) for num in split_user_input]
    except ValueError:
        raise ValueError("Введеные значения не являются числами")


def solve_function(args):
    if len(args) == 3:
        if args[0] == 0:
            return find_linear_solution(*args[1:])
        return find_real_square_root(*args)
    if len(args) == 2:
        return find_linear_solution(*args)


def find_real_square_root(a, b, c):
    dis = b**2 - 4 * a * c

    if dis < 0:
        raise ValueError("Дискриминант меньше 0")

    sqrt_val = dis ** (1 / 2)

    if dis > 0:
        return tuple((-b + sign * sqrt_val) / (2 * a) for sign in (-1, 1))

    if dis == 0:
        return (-b / (2 * a),)


def find_linear_solution(k, b):
    if k == 0 and b == 0:
        raise ValueError("Решение таких уравнений в данной системе не рассматривается")

    if k == 0:
        raise ValueError("Значение параметра k не должно быть равно нулю")
    return (-b / k,)


def main():
    user_input = input(
        "Введите значения a, b, c для квадратного уравнения, либо k, b для линейного\n"
    )
    try:
        args = parse_user_input(user_input)
        print(f"Результат вычислений: {' '.join(map(str,solve_function(args)))}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
