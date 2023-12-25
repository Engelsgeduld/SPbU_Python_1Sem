import sys
import warnings

import pytest

from src.exams.exam_2_safe_call.safecall import safe_call, traceback_parser


def traceback_test_func():
    def inner():
        raise ValueError("I am inner func")

    inner()


@safe_call
def basic_dummy_func(param):
    if param is True:
        return 1
    else:
        raise ValueError("Wrong parameter")


@safe_call
def list_dummy_function(n):
    values = [1, 2, 3, 4, 5]
    for i in range(n):
        values[i] *= 2
    return values


@safe_call
def dummy_func_with_recursion(param):
    def recursion(param):
        if param == 10:
            return param
        return recursion(param + 1)

    return recursion(param)


@pytest.mark.parametrize(
    "func, param, expected",
    [
        (basic_dummy_func, True, 1),
        (list_dummy_function, 2, [2, 4, 3, 4, 5]),
        (dummy_func_with_recursion, 1, 10),
    ],
)
def test_funcs_normal_scenario(func, param, expected):
    assert func(param) == expected


def test_dummy_func_exception(monkeypatch):
    with warnings.catch_warnings(record=True) as warning:
        basic_dummy_func(False)
        assert (
            str(warning[-1].message)
            == 'In function basic_dummy_func\nValueError: Wrong parameter\nAt line 21: raise ValueError("Wrong parameter")'
        )


def test_list_dummy_function(monkeypatch):
    with warnings.catch_warnings(record=True) as warning:
        list_dummy_function(20)
        assert (
            str(warning[-1].message)
            == "In function list_dummy_function\nIndexError: list index out of range\nAt line 28: values[i] *= 2"
        )


def test_dummy_func_with_recursion_exception(monkeypatch):
    with warnings.catch_warnings(record=True) as warning:
        dummy_func_with_recursion(11)
        assert (
            str(warning[-1].message)
            == "In function recursion\nRecursionError: maximum recursion depth exceeded\nAt line 37: return recursion(param + 1)"
        )


def test_traceback_parser():
    with pytest.raises(ValueError):
        traceback_test_func()
        exc_type, exc_value, exc_traceback = sys.exc_info()
        assert traceback_parser(exc_type, exc_value, exc_traceback) == [
            "inner",
            "ValueError",
            "I am inner function",
            "11",
            'raise ValueError("I am inner func")',
        ]
