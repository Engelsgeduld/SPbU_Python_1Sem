from math import log2
from src.Homeworks.homework_6.avl_tree_module.avl_tree import *
from src.Homeworks.homework_6.avl_tree_module.avl_tree import (
    _insert_main_root,
    _get_balance_factor,
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


def balance_validator(root: Node[Key, Value], balance=[]):
    if root is None:
        return [0]

    def recursion(node: Node[Key, Value]):
        if node.right_children is not None:
            recursion(node.right_children)
        if node.left_children is not None:
            recursion(node.left_children)
        balance.append(_get_balance_factor(root))

    recursion(root)
    return balance


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


@pytest.mark.parametrize(
    "args",
    (
        [1, 2, 3],
        [1, 2, 0, -1, -2, -99, 100],
    ),
)
def test_put_balance_function(args, empy_tree_initialization):
    for arg in args:
        put(empy_tree_initialization, arg, "1")
        balance = balance_validator(empy_tree_initialization.root)
        assert len(list(filter(lambda val: val in [-1, 0, 1], balance))) == len(balance)


def test_delete_balance_function(tree_initialization_with_values):
    keys = traverse(tree_initialization_with_values, 0)
    for key in keys:
        remove(tree_initialization_with_values, key[0])
        balance = balance_validator(tree_initialization_with_values.root)
        assert len(list(filter(lambda val: val in [-1, 0, 1], balance))) == len(balance)
