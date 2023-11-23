from os.path import exists

import pytest
from src.Homeworks.homework_6.avl_tree_module.avl_tree import *
from src.Homeworks.homework_6.task_1_shopping.shopping import main, command_operator


def data_set_log_import():
    log_file_name = "logs.txt"
    expected, expected_balance, actual, actual_balance = [], [], [], []
    with open("Tests/homeworks/homework_6/task_1_shopping/shop_results.txt") as result:
        for line in result.readlines():
            expected.append(line)
    with open(f"{log_file_name}") as result:
        for line in result.readlines():
            actual.append(line)

    return actual, expected


def test_file_validation(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "src/Homeworks/homework_6/task_1_shopping/wrong_name.txt",
    )
    with pytest.raises(ValueError):
        main()


@pytest.mark.parametrize(
    "command, args",
    (("ADD", ("5", "3", "4")), ("GET", ("1", "2")), ("SELECT", ("4", "5"))),
)
def test_command_operator_exceptions(command, args):
    with pytest.raises(ValueError):
        command_operator(Tree(), command, *args)


def data_set_balance_import():
    balance_file_name = "balance.txt"
    actual_balance, expected_balance = [], []
    with open("Tests/homeworks/homework_6/task_1_shopping/shop_balance.txt") as balance:
        for line in balance.readlines():
            expected_balance.append(line)
    with open(f"{balance_file_name}") as real_balance:
        for line in real_balance.readlines():
            actual_balance.append(line)
    return actual_balance, expected_balance


def test_main_scenario_runner(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "src/Homeworks/homework_6/task_1_shopping/shop_logs.txt",
    )
    main()
    assert exists(f"logs.txt")
    assert exists(f"balance.txt")


def test_main_logs():
    actual, expected = data_set_log_import()
    for i in range(len(actual)):
        assert actual[i] == expected[i]


def test_main_balance():
    actual_balance, expected_balance = data_set_balance_import()
    for i in range(len(actual_balance)):
        assert actual_balance[i] == expected_balance[i]
