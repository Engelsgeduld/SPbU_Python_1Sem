def curry(func, arity):
    if arity < 0:
        raise ValueError("Арность должна быть >= 0")

    def args_collector(*args):
        give_args = len(args)

        if arity > give_args:

            def sup_func(*new_args):
                return func(*(args + new_args))

            return curry(sup_func, arity=arity - len(args))

        return func(*args)

    args_collector.arity = arity
    return args_collector


def uncurry(func, arity):
    if arity < 0:
        raise ValueError("Арность должна быть >= 0")

    def sup_func(*args):
        if len(args) != arity:
            raise ValueError("Количество параметров не соотвествует арности")

        return func(*args)

    return sup_func


def main():
    curry_func = curry(print, 3)
    uncurry_func = uncurry(curry_func, 4)
    curry_func(3)(4)(5)
    uncurry_func(3, 4, 5, 7)


if __name__ == "__main__":
    main()
