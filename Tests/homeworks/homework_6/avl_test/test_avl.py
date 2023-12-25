from math import log2
from src.Homeworks.homework_6.avl_tree_module.avl_tree import *
from src.Homeworks.homework_6.avl_tree_module.avl_tree import (
    _insert_main_root,
    _balance_tree,
)
import pytest


@pytest.fixture()
def empy_tree_initialization():
    empty_tree = create_tree_map()
    return empty_tree


@pytest.fixture()
def tree_initialization_with_values():
    keys = [5, 3, 4, 6, 8, 9, 2, 7]
    values = list(map(str, keys))
    tree = create_tree_map()
    for i in range(len(keys)):
        put(tree, keys[i], values[i])
    return tree


def test_creation_tree():
    actual = create_tree_map()
    assert actual == Tree()


@pytest.mark.parametrize("tree_type, key", ((int, 8), (str, "8")))
def test_init_root_type(tree_type, key, empy_tree_initialization):
    put(empy_tree_initialization, key, "smth")
    assert empy_tree_initialization.type is tree_type


@pytest.mark.parametrize(
    "key, tree_type", ((8, str), ([1, 2], tuple), ({2, 3}, list), (1, bool))
)
def test_put_exception(key, tree_type, empy_tree_initialization):
    empy_tree_initialization.type = tree_type
    with pytest.raises(ValueError):
        put(empy_tree_initialization, key, 1)


@pytest.mark.parametrize(
    "key, values", ((5, "5"), (3, "3"), (4, "4"), (6, "6"), (8, "8"), (9, "9"))
)
def test_get_function(key, values, tree_initialization_with_values):
    actual = get(tree_initialization_with_values, key)
    assert actual == values


@pytest.mark.parametrize(
    "key, result",
    (
        (5, True),
        (3, True),
        (4, True),
        (6, True),
        (8, True),
        (9, True),
        (25, False),
        (1024, False),
    ),
)
def test_has_key(key, result, tree_initialization_with_values):
    actual = has_key(tree_initialization_with_values, key)
    assert actual == result


def test_get_exception(tree_initialization_with_values):
    with pytest.raises(ValueError):
        get(tree_initialization_with_values, 12)


def test_get_empty_tree(empy_tree_initialization):
    with pytest.raises(ValueError):
        get(empy_tree_initialization, 20)


def test_insert_main_root(empy_tree_initialization):
    _insert_main_root(empy_tree_initialization, 8, 12)
    assert empy_tree_initialization.root == Node(8, 12)


def test_insert_main_root_exception(empy_tree_initialization):
    with pytest.raises(ValueError):
        _insert_main_root(empy_tree_initialization, None, [1, 2])


@pytest.mark.parametrize(
    "key, order",
    [
        (8, [(2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (9, "9")]),
        (3, [(2, "2"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9")]),
    ],
)
def test_remove(tree_initialization_with_values, key, order):
    remove(tree_initialization_with_values, key)
    actual = traverse(tree_initialization_with_values, 1)
    assert actual == order


def test_remove_empty_tree(empy_tree_initialization):
    with pytest.raises(ValueError):
        remove(empy_tree_initialization, 20)


@pytest.mark.parametrize("key, value", [(8, "8"), (3, "3")])
def test_remove_value(tree_initialization_with_values, key, value):
    actual = remove(tree_initialization_with_values, key)
    assert actual == value


def test_preorder(tree_initialization_with_values):
    actual = traverse(tree_initialization_with_values, 0)
    assert actual == [
        (6, "6"),
        (4, "4"),
        (3, "3"),
        (2, "2"),
        (5, "5"),
        (8, "8"),
        (7, "7"),
        (9, "9"),
    ]


def test_inorder(tree_initialization_with_values):
    actual = traverse(tree_initialization_with_values, 1)
    assert actual == [
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
    ]


def test_traverse_empty_tree(empy_tree_initialization):
    actual = traverse(empy_tree_initialization, 0)
    assert actual is None


def test_extract_max(tree_initialization_with_values):
    actual = get_maximum(tree_initialization_with_values)
    assert actual == 9


def test_extract_min(tree_initialization_with_values):
    actual = get_minimum(tree_initialization_with_values)
    assert actual == 2


split_data_set = [
    (
        5,
        [
            [(3, "3"), (2, "2"), (4, "4")],
            [(8, "8"), (6, "6"), (5, "5"), (7, "7"), (9, "9")],
        ],
    ),
    (
        10,
        [
            [
                (5, "5"),
                (3, "3"),
                (2, "2"),
                (4, "4"),
                (8, "8"),
                (7, "7"),
                (6, "6"),
                (9, "9"),
            ],
            None,
        ],
    ),
]


@pytest.mark.parametrize(
    "key, result",
    split_data_set,
)
def test_split_function(key, result, tree_initialization_with_values):
    actual = list(
        map(lambda tree: traverse(tree, 0), split(tree_initialization_with_values, key))
    )
    assert actual == result


@pytest.mark.parametrize(
    "left, right, result", ((3, 7, [3, 4, 5, 6]), (10, 100, []), (3, 4, [3]))
)
def test_get_all_keys_function(left, right, result, tree_initialization_with_values):
    actual = get_all(tree_initialization_with_values, left, right)
    assert actual == result


@pytest.mark.parametrize(
    "first_tree_args, second_tree_args",
    [([1, 2, 3, 4], [5, 6, 7, 8, 9]), ([1, 2], [5]), ([4, 5, 6], [7, 8, 9])],
)
def test_merge_functions(first_tree_args, second_tree_args):
    first_tree, second_tree = create_tree_map(), create_tree_map()
    all_keys = list(
        zip(first_tree_args + second_tree_args, first_tree_args + second_tree_args)
    )
    for key in first_tree_args:
        put(first_tree, key, key)
    for key in second_tree_args:
        put(second_tree, key, key)
    merged_tree = merge(first_tree, second_tree)
    actual = traverse(merged_tree, 0)
    assert set(actual) == set(all_keys) and merged_tree.root.height == (
        int(log2(len(all_keys))) + 1
    )


def test_split_tree_empty_scenario(empy_tree_initialization):
    actual = split(empy_tree_initialization, 10)
    assert actual == (empy_tree_initialization, empy_tree_initialization)


def test_merge_tree_empty_scenario(empy_tree_initialization):
    actual = merge(empy_tree_initialization, empy_tree_initialization)
    assert actual == empy_tree_initialization


@pytest.mark.parametrize(
    "args, result",
    (
        ([1, 2, 3], [(2, "1"), (1, "1"), (3, "1")]),
        ([1, 2, 0, -1, -2], [(1, "1"), (-1, "1"), (-2, "1"), (0, "1"), (2, "1")]),
    ),
)
def test_balance_function(args, result, empy_tree_initialization):
    for arg in args:
        put(empy_tree_initialization, arg, "1")
    assert traverse(empy_tree_initialization, 0) == result
