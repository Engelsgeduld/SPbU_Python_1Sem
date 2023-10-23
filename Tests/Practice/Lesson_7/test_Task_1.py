from io import StringIO

import pytest

from src.Practice.Lesson_7.Task_1 import *


@pytest.mark.parametrize("args", [[1], [1, 2, 3, 4, 5]])
def test_len_exception(args):
    with pytest.raises(ValueError):
        choose_function(args)


def test_raise_exception_type():
    with pytest.raises(ValueError):
        valid_user_input("not integer input")


def test_valid_integer():
    with pytest.raises(ValueError):
        float_check("get string")


@pytest.mark.parametrize("a, b", [(0, 1), (0, 0)])
def test_raise_exception_wrong_args(a, b):
    with pytest.raises(ValueError):
        find_linear_solution(a, b)


def test_raise_exceptions_dis():
    with pytest.raises(ValueError):
        find_real_square_root(120, 1, 1)


@pytest.mark.parametrize(
    "a,b, expected", [(1, 2, (-2.0,)), (2, -2, (1.0,)), (-2, 4, (2.0,))]
)
def test_linear_root(a, b, expected):
    actual = find_linear_solution(a, b)
    assert actual == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [(2, -1, -15, (-2.5, 3)), (1, 12, 36, (-6.0,)), (0, 2, 4, (-2.0,))],
)
def test_square_root(a, b, c, expected):
    actual = find_real_square_root(a, b, c)
    assert [actual[i] == expected[i] for i in range(len(expected))]


def test_main_scenario(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2 -1 -15")
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == "Результат вычислений: -2.5 3.0\n"


@pytest.mark.parametrize(
    "unique_input, unique_output",
    [
        ("0 1", "Значение параметра k не должно быть равно нулю"),
        ("0 0", "Решение таких уравнений в данной системе не рассматривается"),
        ("1", "Количество введенных аргументов не подходит ни к одному типу функции"),
        (
            "1 1 1 1",
            "Количество введенных аргументов не подходит ни к одному типу функции",
        ),
        ("120 1 1", "Дискриминант меньше 0"),
        ("r t r", "Аргумент не является числом"),
    ],
)
def test_output_scenario(monkeypatch, unique_input, unique_output):
    monkeypatch.setattr("builtins.input", lambda _: unique_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == unique_output + "\n"
