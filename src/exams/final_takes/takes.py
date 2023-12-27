from types import UnionType
from typing import get_args, get_origin
import functools


def with_arguments(deco):
    @functools.wraps(deco)
    def inner(*deco_args, **deco_kwargs):
        def decorator(func):
            result = deco(func, *deco_args, **deco_kwargs)
            functools.update_wrapper(result, func)
            return result

        return decorator

    return inner


def check_type(arg, arg_type):
    origin_type = get_origin(arg_type)
    if isinstance(arg_type, UnionType):
        types = get_args(arg_type)
        return any(map(lambda type_: check_type(arg, type_), types))
    if origin_type is not None and isinstance(arg, origin_type):
        types = get_args(arg_type)
        if origin_type in [list, tuple]:
            return all(map(lambda args: check_type(args, types[0]), arg))
        if origin_type is dict:
            keys = list(arg)
            values = list(arg.values())
            keys_valid = all(map(lambda key: check_type(key, types[0]), keys))
            values_valid = all(map(lambda val: check_type(val, types[1]), values))
            return keys_valid and values_valid
    return isinstance(arg, arg_type)


@with_arguments
def takes(func, *type_args):
    def inner(*args, **kwargs):
        typed_args = args + tuple(kwargs.values())[: len(type_args)]
        args_with_type = list(zip(typed_args, type_args))
        validate_args = list(
            map(lambda pair: check_type(pair[0], pair[1]), args_with_type)
        )
        if all(validate_args):
            return func(*args, **kwargs)
        raise TypeError("Type mismatch")

    return inner
