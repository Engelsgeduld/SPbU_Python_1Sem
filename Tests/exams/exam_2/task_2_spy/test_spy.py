from src.exams.exam_2.task_2_spy.spy import *
import pytest


@spy
def fake_function(a, b):
    pass


@spy
def another_fake_func(a, b):
    pass


def test_spy_decorator():
    start = time.strftime("%H:%M:%S", time.localtime(1347517370))
    fake_function(5, 6)
    expected = {"a": 5, "b": 6}
    print(getattr(fake_function, "start_args", False))
    actual = [*getattr(fake_function, "start_args", False)]
    print(actual)
    assert actual == [[start, expected]]


def test_print_usage_statistic():
    time1 = time.strftime("%H:%M:%S", time.localtime(1347517370))
    another_fake_func(11, 12)
    time2 = time.strftime("%H:%M:%S", time.localtime(1347517370))
    another_fake_func(7, 8)
    actual = [pair for pair in print_usage_statistic(another_fake_func)]
    assert actual == [[time1, {"a": 11, "b": 12}], [time2, {"a": 7, "b": 8}]]
