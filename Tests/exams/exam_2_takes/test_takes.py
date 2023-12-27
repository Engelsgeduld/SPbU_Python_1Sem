import pytest

from src.exams.final_takes.takes import *


@takes(int, str, list, int)
def dummy_func(a, b, c, e=1):
    return True


@takes(int)
def dummy_func_two(a, b, c, e):
    return True


@pytest.mark.parametrize(
    "value, type_, result",
    (
        [1, int, True],
        ["a", str, True],
        [[1, 2, 3], list[int], True],
        [["2", 1, 1], list[int | str], True],
        [[(2, "3", "1")], list[tuple[int | str]], True],
        [[1, 2, ("2", "3")], list[int | tuple[str]], True],
        [{"a": 1}, dict[str, int], True],
        [("2", "1"), tuple[int], False],
    ),
)
def test_check_type(value, type_, result):
    assert check_type(value, type_) == result


def test_main_scenario():
    assert dummy_func(1, "2", [1, 2, 3], 3)


def test_main_scenario_with_kwargs():
    assert dummy_func(1, "2", c=[1, 2, 3], e=3)


def test_main_scenario_with_more_args():
    assert dummy_func_two(1, 2, "3", [1, 2, 3])


def test_exception_scenario():
    with pytest.raises(TypeError):
        dummy_func("2", 1, (2, 3), "3")
