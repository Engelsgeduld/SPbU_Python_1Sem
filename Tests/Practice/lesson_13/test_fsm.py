from io import StringIO
from string import digits
from src.Practice.lesson_13.fsm import *
from src.Practice.lesson_13.user import (
    digits_validation,
    abb_validation,
    main,
)

import pytest


@pytest.fixture
def create_fms_abb():
    abb_setup = [
        [{"b": 0, "a": 1}, {"b": 2, "a": 1}, {"b": 3, "a": 1}, {"b": 0, "a": 1}],
        0,
        [3],
    ]
    return create_fs_machine(*abb_setup)


@pytest.fixture
def create_fms_digits():
    digits_setup = [
        [
            {digits: 1, "+-": 5},
            {digits: 1, "E": 3, ".": 6},
            {digits: 2, "E": 3},
            {digits: 4, "+-": 7},
            {digits: 4},
            {digits: 1},
            {digits: 2},
            {digits: 4},
        ],
        0,
        [1, 2, 4],
    ]
    return create_fs_machine(*digits_setup)


def test_fms_creation(create_fms_digits):
    assert type(create_fms_digits) == FSMachine


@pytest.mark.parametrize(
    "line, result",
    [("abb", True), ("bbb", False), ("aaabb", True), ("bbbabb", True), ("ffff", False)],
)
def test_abb_validation(line, result, create_fms_abb):
    actual = validate_string(create_fms_abb, line)
    assert actual == result


@pytest.mark.parametrize(
    "line, result",
    [
        ("-12", True),
        ("12", True),
        ("12.", False),
        ("-12.", False),
        ("12E", False),
        ("12E-", False),
        ("12E12", True),
        ("12.12E12", True),
        ("12.12E-12", True),
        ("12.12E+12", True),
        ("+12.12E+12", True),
        ("abb", False),
    ],
)
def test_digits_validation(line, result, create_fms_digits):
    actual = validate_string(create_fms_digits, line)
    assert actual == result


@pytest.mark.parametrize(
    "state_index, token, next_state", [(0, "f", None), (3, "+", 7), (3, digits, 4)]
)
def test_state_move(state_index, token, next_state, create_fms_digits):
    actual = state_move(state_index, token, create_fms_digits)
    assert actual == next_state


@pytest.mark.parametrize(
    "tokens, result", [(["f"], None), (["1", "2", "."], 6), (["1", "2", "E"], 3)]
)
def test_iterator(tokens, result, create_fms_digits):
    actual = iterator(create_fms_digits, tokens)
    assert actual == result


@pytest.mark.parametrize(
    "line, result",
    [
        ("-12", True),
        ("12", True),
        ("12.", False),
        ("-12.", False),
        ("12E", False),
        ("12E-", False),
        ("12E12", True),
        ("12.12E12", True),
        ("12.12E-12", True),
        ("12.12E+12", True),
        ("+12.12E+12", True),
        ("abb", False),
    ],
)
def test_digits_validation(line, result):
    actual = digits_validation(line)
    assert actual == result


@pytest.mark.parametrize(
    "line, result",
    [("abb", True), ("bbb", False), ("aaabb", True), ("bbbabb", True), ("ffff", False)],
)
def test_add_validation(line, result):
    actual = abb_validation(line)
    assert actual == result


@pytest.mark.parametrize(
    "unique_input, unique_output",
    [
        ("abb", "This is АБОБА ЛАНГУАГЕ"),
        ("12.12E+12", "This is Digits language"),
        ("fff", "This string match no language"),
    ],
)
def test_main_scenario(monkeypatch, unique_input, unique_output):
    monkeypatch.setattr("builtins.input", lambda _: unique_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == unique_output + "\n"
