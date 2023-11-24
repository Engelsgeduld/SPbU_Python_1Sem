import functools
import inspect
import time
from typing import Callable, Iterable


def spy(function: Callable):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        args_name = list(
            map(lambda pair: pair[0], (inspect.signature(function).parameters.items()))
        )
        arguments = dict(zip(args_name, list(args) + list(kwargs.values())))
        start = time.strftime("%H:%M:%S", time.localtime(1347517370))
        function(*args, **kwargs)
        inner.start_args.append([start, arguments])

    inner.start_args = []
    inner.decorated = True
    return inner


def print_usage_statistic(function: Callable) -> Iterable:
    if not getattr(function, "decorated", False):
        raise ValueError("Function must be decorated")
    for pair in getattr(function, "start_args", False):
        yield pair


@spy
def foo(a, b):
    print(a + b)


def main():
    foo(4, 5)
    foo(6, 9)
    foo(30, 50)

    for time, parameters in print_usage_statistic(foo):
        str_parameters = ", ".join(f"{k} = {v}" for k, v in parameters.items())
        print(
            f"function {foo.__name__} was called at {time} "
            f"with parameters:\n{str_parameters}"
        )


if __name__ == "__main__":
    main()
