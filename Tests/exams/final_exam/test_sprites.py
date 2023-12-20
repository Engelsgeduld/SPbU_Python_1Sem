from io import StringIO

from src.exams.final_exam.sprites import *

import pytest


@pytest.mark.parametrize("input", ["12", "20", "13", "14"])
def test_validation_user_input_normal_scenario(input):
    actual = validate_user_input(input)
    assert actual == int(input)


@pytest.mark.parametrize("input", ["0.12", "abc", "+21", "-12", "12 13", "021", "\n25"])
def test_validation_user_input_invalid_scenario(input):
    with pytest.raises(ValueError):
        validate_user_input(input)


@pytest.mark.parametrize(
    "length, expected",
    [
        (1, ["█ \n"]),
        (3, ["█ █ █ \n", "█ █ █ \n", "█ █ █ \n"]),
        (2, ["█ █ \n", "█ █ \n"]),
        (
            7,
            [
                "█ █ █ █ █ █ █ \n",
                "█ █ █ █ █ █ █ \n",
                "█ █ █ █ █ █ █ \n",
                "█ █ █ █ █ █ █ \n",
                "█ █ █ █ █ █ █ \n",
                "█ █ █ █ █ █ █ \n",
                "█ █ █ █ █ █ █ \n",
            ],
        ),
    ],
)
def test_creation_of_sprites_table(length, expected):
    actual = create_sprites_table(length)
    assert actual == expected


@pytest.mark.parametrize("length", [1, 3, 2, 7])
def test_creation_of_sprites_string(length):
    table = create_sprites_table(length)
    actual = create_sprites_string(table)
    expected = (f"{SPRITE_UNICODE + " "}" * length + "\n") * length
    assert actual == expected


@pytest.mark.parametrize(
    "unique_input",
    [["0.1"], ["2", "55", "42", "0.2"], ["7", "0027"], ["5", "abc"]],
)
def test_main_exception_scenario(monkeypatch, unique_input):
    inputs = iter(unique_input)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stderr", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == "Length must be a integer" + "\n"


@pytest.mark.parametrize(
    "unique_input, unique_output",
    [
        (["1", "STOP"], "█ \n"),
        (
            ["1", "2", "5", "7", "STOP"],
            "█ \n"
            + "\n"
            + "█ █ \n" * 2
            + "\n"
            + "█ █ █ █ █ \n" * 5
            + "\n"
            + "█ █ █ █ █ █ █ \n" * 7,
        ),
    ],
)
def test_main_normal_scenario(monkeypatch, unique_input, unique_output):
    inputs = iter(unique_input)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == unique_output + "\n"
