from io import StringIO

from src.exams.exam_2.task_1_fibonacci.fibonacci import *
import pytest


def dataset_import():
    data = []
    with open("Tests/exams/exam_2/task_1_fibonacci/fib_numbers") as numbers_input:
        for line in numbers_input.readlines():
            data.append(list(map(int, line.split(". "))))
    return data


@pytest.mark.parametrize("n, expected", dataset_import())
def test_fibonacci_func(n: int, expected):
    actual = fibonacci(n)
    assert actual == expected


@pytest.mark.parametrize("n", ("-1", "100", "abc", "0.34", "+40", "040", "40_0"))
def test_n_validation(n: str):
    with pytest.raises(ValueError):
        validation_fib_input(n)


@pytest.mark.parametrize(
    "unique_input, unique_output",
    [("1", "1th Fibonacci number: 1"), ("9", "9th Fibonacci number: 34")],
)
def test_main_scenario(monkeypatch, unique_input, unique_output):
    monkeypatch.setattr("builtins.input", lambda _: unique_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == unique_output + "\n"


@pytest.mark.parametrize(
    "unique_input, unique_output",
    [
        (
            "-1",
            "Error: N must be a positive integer without any other symbols(+ - . etc)",
        ),
        ("04", "Error: N can not begin with zero"),
        ("100", "Error: N must be in range 0..90"),
    ],
)
def test_error_output(monkeypatch, unique_input, unique_output):
    monkeypatch.setattr("builtins.input", lambda _: unique_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stderr", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == unique_output + "\n"
