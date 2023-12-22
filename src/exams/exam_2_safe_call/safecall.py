import sys
import traceback
from warnings import warn


def safe_call(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException:
            warn(
                "In function {}\n{}: {}\nAt line {}: {}".format(
                    *traceback_parser(*sys.exc_info())
                ),
                stacklevel=2,
            )
            return 0

    return inner


def traceback_parser(exc_type, exc_value, exc_traceback):
    trase_values = traceback.extract_tb(exc_traceback)[-1]
    print(trase_values)
    return (
        trase_values.name,
        exc_type.__name__,
        exc_value,
        trase_values.lineno,
        trase_values.line,
    )
