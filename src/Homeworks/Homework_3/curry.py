def curry(func, arity):
    f_args = []

    def sup_func(*args):
        nonlocal f_args
        if len(f_args) < arity:
            f_args += args
            if len(f_args) != arity:
                return sup_func
            else:
                result = func(*f_args)
                f_args = []
                return result

    return sup_func


def uncurry(func, arity):
    def sup_func(*args):
        if len(args) != arity:
            print("Количество параметров превышает арность")
            return False
        result = func
        for arg in args:
            result = func(arg)
        return result

    return sup_func


def check_user_input_arity(arity_input):
    if not arity_input.isdigit():
        print("Арность должна быть числом")
        return False
    if int(arity_input) < 0:
        print("Арность должна быть >= 0")
        return False
    return int(arity_input)


def check_func_args_power(func_args):
    func_args = func_args.split()
    if not all([arg.isdigit() for arg in func_args]):
        print("Введенные значения должны быть числами")
        return False
    return list(map(int, func_args))


def check_func_args(func_args, arity):
    if len(func_args) > arity:
        print("Количество введенных значений больше арности")
        return False
    return func_args


def curry_print_func():
    arity = check_user_input_arity(input("Введите арность \n"))
    func_input = check_func_args(
        input("Введите аргументы через пробел\n").split(), arity
    )

    if False in [arity, func_input]:
        return False

    curry_print = curry(print, arity)
    uncurry_print = uncurry(curry_print, arity)
    print(f"Функция с каррированием:")
    for arg in func_input:
        curry_print(arg)
    print(f"Функция без каррирования:")
    uncurry_print(*func_input)

    return True


def curry_power_func():
    arity, func_input = 2, check_func_args_power(
        input("Введите аргументы через пробел\n")
    )

    if func_input is False or check_func_args(func_input, arity) is False:
        return False

    curry_power = curry(lambda x, y: x**y, arity)
    result = curry_power
    uncurry_power = uncurry(curry_power, arity)
    for arg in func_input:
        result = curry_power(arg)
    print(f"Функция с каррированием: {result}")
    print(f"Функция без каррирования: {uncurry_power(*func_input)}")

    return True


def curry_max_func():
    arity = check_user_input_arity(input("Введите арность \n"))
    func_input = check_func_args(
        input("Введите аргументы через пробел\n").split(), arity
    )

    if False in [arity, func_input]:
        return False

    curry_max = curry(max, arity)
    uncurry_max = uncurry(curry_max, arity)
    print(f"Функция с каррированием: {curry_max(*func_input)}")
    print(f"Функция без каррирования: {uncurry_max(*func_input)}")
    return True


def menu():
    print(
        "Программа-демонстрация каррирования декаррирования \nДоступные функции: \n1.Print \n2.Power \n3.Max"
    )
    user_input = input("Выберете функцию \n")
    match user_input:
        case "1":
            if not curry_print_func():
                menu()
        case "2":
            if not curry_power_func():
                menu()
        case "3":
            if not curry_max_func():
                menu()


def main():
    menu()


if __name__ == "__main__":
    main()
