from src.Practice.lesson_9.hash_table import *
import pytest
from mimesis import Locale, Code, Person


def dataset_generator():
    person = Person(locale=Locale.EN)
    code = Code().imei()
    names = [person.name() for _ in range(30)]
    codes = [code for _ in range(30)]
    return list(zip(names, codes))


data_set = set(dataset_generator())


@pytest.fixture()
def create_table_with_values():
    table = create_hash_table()
    for obj in data_set:
        put(table, obj[0], obj[1])
    print(table)
    return table


@pytest.fixture()
def create_empty_table():
    table = create_hash_table()
    return table


@pytest.mark.parametrize("key, value", data_set)
def test_get_function(key, value, create_table_with_values):
    table = create_table_with_values
    actual = get(table, key)
    assert actual == value


@pytest.mark.parametrize("key, value", data_set)
def test_has_key_function(key, value, create_table_with_values):
    table = create_table_with_values
    actual = has_key(table, key)
    assert actual is True


@pytest.mark.parametrize("key, value", data_set)
def test_put_function(key, value, create_empty_table):
    table = create_empty_table
    put(table, key, value)
    actual = get(table, key)
    assert actual == value


@pytest.mark.parametrize("key, value", data_set)
def test_remove_return_value(key, value, create_table_with_values):
    table = create_table_with_values
    actual = remove(table, key)
    assert actual == value


@pytest.mark.parametrize("key, value", data_set)
def test_remove_function(key, value, create_table_with_values):
    table = create_table_with_values
    remove(table, key)
    assert has_key(table, key) is False


def test_items_function(create_table_with_values):
    table = create_table_with_values
    assert all([obj in data_set for obj in get_items(table)])


def test_resize_function(create_empty_table):
    table = create_empty_table
    actual = table.capacity
    for data in data_set:
        put(table, data[0], data[1])
    assert actual != table.capacity and all(
        [obj in data_set for obj in get_items(table)]
    )


def test_remove_empty(create_empty_table):
    with pytest.raises(ValueError):
        remove(create_empty_table, 0)


def test_remove_non_exist_key(create_table_with_values):
    with pytest.raises(ValueError):
        remove(create_table_with_values, 5)
