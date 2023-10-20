from io import StringIO

import pytest

from src.Practice.Lesson_7.Task_1 import *


def test_len_exception():
    with pytest.raises(ValueError):
        choose_function([1])
        choose_function([1, 2, 3, 4, 5])


def test_raise_exception_type():
    with pytest.raises(ValueError):
        valid("r t y")
        float_check("y")


def test_raise_exception_wrong_args():
    with pytest.raises(ValueError):
        find_real_square_root(0, 1, 1)
        find_linear_solution(0, 1)
        find_linear_solution(0, 0)


def test_raise_exceptions_dis():
    with pytest.raises(ValueError):
        find_real_square_root(120, 1, 1)


@pytest.mark.parametrize("a,b, expected", [(1, 2, (-2))])
def test_linear_root(a, b, expected):
    actual = find_linear_solution(a, b)
    assert actual == expected


@pytest.mark.parametrize(
    "a,b,c,expected", [(2, -1, -15, (-2.5, 3)), (1, 12, 36, [-6.0])]
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
    assert output == "-2.5 3.0\n"


def test_output_scenario(monkeypatch):
    unique_input = ["0 1 1", "0 1", "0 0", "1", "1 1 1 1", "120 1 1", "r t r"]
    unique_output = [
        "Значение параметра а не должно равняться нулю",
        "Значение параметра а не должно быть равно нулю",
        "Решение таких уравнений в данной системе не рассматривается",
        "Количество введенных аргументов не подходит ни к одному типу функции",
        "Количество введенных аргументов не подходит ни к одному типу функции",
        "Дискриминант меньше 0",
        "Аргумент не является числом",
    ]
    for i in range(len(unique_input)):
        monkeypatch.setattr("builtins.input", lambda _: unique_input[i])
        fake_output = StringIO()
        monkeypatch.setattr("sys.stdout", fake_output)
        main()
        output = fake_output.getvalue()
        assert output == unique_output[i] + "\n"
