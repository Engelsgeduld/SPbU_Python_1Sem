from io import StringIO
from os.path import exists

import pytest
from src.Homeworks.homework_6.task_2_streets.streets import *


def data_set_log_import():
    log_file_name = "streets_res.txt"
    expected, expected_balance, actual, actual_balance = [], [], [], []
    with open("streets_results.txt") as result:
        for line in result.readlines():
            expected.append(line)
    with open(f"{log_file_name}") as result:
        for line in result.readlines():
            actual.append(line)

    return actual, expected


def test_main_scenario_runner(monkeypatch):
    inputs = iter(
        ["2", "../../../../src/Homeworks/homework_6/task_2_streets/streets_logs.txt"]
    )
    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )
    main()
    assert exists(f"streets_res.txt")


def test_main_logs():
    actual, expected = data_set_log_import()
    for i in range(len(actual)):
        assert actual[i] == expected[i]


@pytest.mark.parametrize(
    "command, args",
    (
        ("CREATE", ["aaa", 12, 1]),
        ("GET", ["aaa", 12]),
        ("LIST", ["aaa", "bbb"]),
        ("RENAME", ["aaa", "bbb", "ccc"]),
        ("CREATE", ["AAA", "b", "cd", "y"]),
    ),
)
def test_commands_exceptions(command, args):
    dictionary = create_tree_map()
    with pytest.raises(ValueError):
        command_operator(dictionary, True, command, *args)
