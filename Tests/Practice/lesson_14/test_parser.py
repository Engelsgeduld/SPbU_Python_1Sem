from io import StringIO

from src.Practice.lesson_14.parser import *
from src.Practice.lesson_14.user import main
from Tests.Practice.lesson_14.data_sets import (
    func_set_export,
    output_set_export,
    output_errors_export,
)

import pytest


@pytest.mark.parametrize("line, expected", [*func_set_export()])
def test_parse_functions(line, expected):
    actual = parse(line.split(" ")).root
    assert actual == expected


@pytest.mark.parametrize("line, expected", [*output_errors_export()])
def test_main_errors(line, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: line)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stderr", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected + "\n"


@pytest.mark.parametrize("line, expected", [*output_set_export()])
def test_main_scenario(line, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: line)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected + "\n\n"
